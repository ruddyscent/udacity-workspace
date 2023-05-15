import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries, validate_table_queries


def load_staging_tables(cur, conn):
    '''Load data from S3 into staging tables.'''
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    '''Insert data from staging tables into fact and dimension tables.'''
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()

def validate_tables(cur, conn):
    '''Validate that the data was inserted correctly.'''
    for query in validate_table_queries:
        print(query)
        cur.execute(query)
        conn.commit()
        try:
            print(cur.fetchall())
        except:
            print('No results to fetch.')

def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)    
    validate_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()