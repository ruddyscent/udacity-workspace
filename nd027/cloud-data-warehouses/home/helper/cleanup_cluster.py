import argparse
import boto3
import configparser

parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument(dest="config", type=str, default="dwh.cfg",
                    help="configuration file with DWH params")
args = parser.parse_args()

# Load DWH Params from a file
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

# Create Clients
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

# STEP 5: Clean up resources
redshift.delete_cluster(ClusterIdentifier=DWH_CLUSTER_IDENTIFIER,  SkipFinalClusterSnapshot=True)
iam.detach_role_policy(RoleName=DWH_IAM_ROLE_NAME, PolicyArn="arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess")
iam.delete_role(RoleName=DWH_IAM_ROLE_NAME)
