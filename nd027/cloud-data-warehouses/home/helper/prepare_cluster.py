import argparse
import boto3
import configparser
import json
import psycopg2
import time


parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument(dest="config", type=str, default="dwh.cfg",
                    help="configuration file with DWH params")
args = parser.parse_args()

config = configparser.ConfigParser()
config.read_file(open(args.config))

KEY                    = config.get("AWS", "KEY")
SECRET                 = config.get("AWS", "SECRET")
REGION                 = config.get("AWS", "REGION")

DWH_CLUSTER_TYPE       = config.get("DWH", "DWH_CLUSTER_TYPE")
DWH_NUM_NODES          = config.get("DWH", "DWH_NUM_NODES")
DWH_NODE_TYPE          = config.get("DWH", "DWH_NODE_TYPE")

DWH_CLUSTER_IDENTIFIER = config.get("DWH", "DWH_CLUSTER_IDENTIFIER")
DWH_DB                 = config.get("DWH", "DWH_DB")
DWH_DB_USER            = config.get("DWH", "DWH_DB_USER")
DWH_DB_PASSWORD        = config.get("DWH", "DWH_DB_PASSWORD")
DWH_PORT               = config.get("DWH", "DWH_PORT")

DWH_IAM_ROLE_NAME      = config.get("DWH", "DWH_IAM_ROLE_NAME")

ec2 = boto3.resource("ec2",
                     aws_access_key_id=KEY,
                     aws_secret_access_key=SECRET,
                     region_name=REGION
                     )

iam = boto3.client("iam",
                   aws_access_key_id=KEY,
                   aws_secret_access_key=SECRET,
                   region_name=REGION
                   )

redshift = boto3.client("redshift",
                        aws_access_key_id=KEY,
                        aws_secret_access_key=SECRET,
                        region_name=REGION
                        )

# STEP 1: IMA Role
# 1.1 Create the role, 
try:
    print("1.1 Creating a new IAM Role") 
    dwhRole = iam.create_role(
        Path="/",
        RoleName=DWH_IAM_ROLE_NAME,
        Description = "Allows Redshift clusters to call AWS services on your behalf.",
        AssumeRolePolicyDocument=json.dumps(
            {"Statement": [{"Action": "sts:AssumeRole",
               "Effect": "Allow",
               "Principal": {"Service": "redshift.amazonaws.com"}}],
             "Version": "2012-10-17"})
    )    
except Exception as e:
    print(e)
    
    
print("1.2 Attaching Policy")

iam.attach_role_policy(RoleName=DWH_IAM_ROLE_NAME,
                       PolicyArn="arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
                      )["ResponseMetadata"]["HTTPStatusCode"]

print("1.3 Get the IAM role ARN")
roleArn = iam.get_role(RoleName=DWH_IAM_ROLE_NAME)["Role"]["Arn"]

# print(roleArn)

# STEP 2: Create Redshift cluster
print("2 Create Redshift cluster")
try:
    response = redshift.create_cluster(        
        #HW
        ClusterType=DWH_CLUSTER_TYPE,
        NodeType=DWH_NODE_TYPE,
        NumberOfNodes=int(DWH_NUM_NODES),

        #Identifiers & Credentials
        DBName=DWH_DB,
        ClusterIdentifier=DWH_CLUSTER_IDENTIFIER,
        MasterUsername=DWH_DB_USER,
        MasterUserPassword=DWH_DB_PASSWORD,
        
        #Roles (for s3 access)
        IamRoles=[roleArn]  
    )
except Exception as e:
    print(e)

# Wait until the cluster status becomes 'Available'
print("2.1 Wait until the cluster status becomes 'Available'")
myClusterProps = redshift.describe_clusters(ClusterIdentifier=DWH_CLUSTER_IDENTIFIER)["Clusters"][0]
while myClusterProps["ClusterStatus"] != "available":
    time.sleep(5)
    myClusterProps = redshift.describe_clusters(ClusterIdentifier=DWH_CLUSTER_IDENTIFIER)["Clusters"][0]

# 2.2 Take note of the cluster endpoint and role ARN
print("2.2 Take note of the cluster endpoint and role ARN")
DWH_ENDPOINT = myClusterProps["Endpoint"]["Address"]
DWH_ROLE_ARN = myClusterProps["IamRoles"][0]["IamRoleArn"]
print("DWH_ENDPOINT ::", DWH_ENDPOINT)
print("DWH_ROLE_ARN ::", DWH_ROLE_ARN)

# STEP 3: Open an incoming TCP port to access the cluster ednpoint
print("3. Open an incoming TCP port to access the cluster ednpoint")
try:
    vpc = ec2.Vpc(id=myClusterProps["VpcId"])
    defaultSg = list(vpc.security_groups.all())[0]
    print(defaultSg)
    defaultSg.authorize_ingress(
        GroupName=defaultSg.group_name,
        CidrIp="0.0.0.0/0",
        IpProtocol="TCP",
        FromPort=int(DWH_PORT),
        ToPort=int(DWH_PORT)
    )
except Exception as e:
    print(e)

# STEP 4: Make sure you can connect to the cluster
print("4 Verify of connection to the cluster")
try:
    conn_string = f"postgresql://{DWH_DB_USER}:{DWH_DB_PASSWORD}@{DWH_ENDPOINT}:{DWH_PORT}/{DWH_DB}"
    # print(conn_string)
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()
    cur.close()
    conn.close()
except Exception as e:
    print(e)
