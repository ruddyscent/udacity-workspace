from typing import List

from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 # Define your operators params (with defaults) here
                 # Example:
                 # conn_id = your-connection-name
                 redshift_conn_id: str = '',
                 tests: List[str] = [],
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        # Map params here
        # Example:
        # self.conn_id = conn_id
        self.redshift_conn_id = redshift_conn_id
        self.tests = tests

    def execute(self, context):
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)

        for test in self.tests:
            sql = test.get('sql')
            expected_result = test.get('expected_result')
            records = redshift.get_records(sql)[0]
            if records[0] != expected_result:
                raise ValueError(f'Data quality check failed. {records[0]} does not equal {expected_result}')
            else:
                self.log.info(f'Data quality on {sql} check passed with expected result {expected_result}')
