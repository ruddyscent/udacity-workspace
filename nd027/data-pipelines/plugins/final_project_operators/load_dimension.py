from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 # Define your operators params (with defaults) here
                 # Example:
                 # conn_id = your-connection-name
                redshift_conn_id="",
                table="",
                sql_statement="",
                append_data=False,
                 *args, **kwargs):
        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        # Map params here
        # Example:
        # self.conn_id = conn_id
        self.redshift_conn_id = redshift_conn_id
        self.table = table
        self.sql_statement = sql_statement
        self.append_data = append_data

    def execute(self, context):
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)

        if self.append_data:
            self.log.info(f"Appending data to {self.table} dimension table")
        else:
            self.log.info(f"Clearing data from {self.table} dimension table")
            # redshift.run(f"DELETE FROM {self.table}")
            redshift.run(f"TRUNCATE TABLE {self.table}")

        self.log.info(f"Inserting data to {self.table} dimension table")
        formatted_sql = f"INSERT INTO {self.table} ({self.sql_statement})"
        redshift.run(formatted_sql)
