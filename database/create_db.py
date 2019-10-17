from __future__ import print_function # Python 2/3 compatibility
import boto3
from pprint import pprint


class DockerizeDynamoDB:
    def __init__(self, db_name, endpoint_url="http://localhost:8000"):
        self.endpoint_url = endpoint_url
        self.db_name = db_name
        self.dynamodb = boto3.resource('dynamodb', endpoint_url=self.endpoint_url)
        self.client = boto3.client('dynamodb', endpoint_url="http://localhost:8000")

    def create_db(self):
        table = self.dynamodb.create_table(
            TableName=self.db_name,
            KeySchema=[
                {
                    'AttributeName': 'FighterId',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'Surname',
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {'AttributeName': 'FighterId',
                  'AttributeType': 'S'
                },
                {
                    'AttributeName': 'Surname',
                    'AttributeType': 'S'
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )
        print("Table status:", table.table_status)

    def get_table(self):
        return self.client.list_tables()['TableNames']

    def drop_table(self):
        response = self.client.delete_table(TableName=self.db_name)
        return pprint(response)

    def insert_fighters_table_data(self):
        pass