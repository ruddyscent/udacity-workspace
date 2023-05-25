import boto3
import configparser
import psycopg2

from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    '''Drop tables if they exist.'''
    for query in drop_table_queries:
        print(query)
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    '''Create tables.'''
    for query in create_table_queries:
        print(query)
        cur.execute(query)
        conn.commit()


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    print(f"roleArn is {config['IAM_ROLE']['ARN']}")

    redshift = boto3.client('redshift',
                           region_name=config['AWS']['REGION'],
                           aws_access_key_id=config['AWS']['KEY'],
                           aws_secret_access_key=config['AWS']['SECRET']
                           )
    myClusterProps = redshift.describe_clusters(ClusterIdentifier=config['DWH']['DWH_CLUSTER_IDENTIFIER'])['Clusters'][0]
    if myClusterProps['ClusterStatus'] == 'available':
        print("Cluster is available")

    print(f"Endpoint is {myClusterProps['Endpoint']['Address']}")

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
