from __future__ import print_function  # Python 2/3 compatibility

import decimal
import json
from pprint import pprint


class DynamoDB:
    def __init__(self, table_name, client=None, region=None, resource=None):
        self.table_name = table_name
        self.dynamodb = resource
        self.region = region
        self.client = client

    def check_if_table_exists(self):
        response = self.client.list_tables()['TableNames']
        print(f'tables: {response}')
        return True if self.table_name in response else False

    def create_db(self):
        exists = self.check_if_table_exists()
        if not exists:
            table = self.client.create_table(
                TableName=self.table_name,
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
        else:
            print(f'Table {self.table_name} already exists')

    def get_table(self):
        return self.client.list_tables()['TableNames']

    def drop_table(self):
        response = self.client.delete_table(TableName=self.table_name)
        return pprint(response)

    def insert_fighters_table_data(self):
        pass

    def populate_fighters_table(self):
        table = self.dynamodb.Table(self.table_name)

        with open(r"gen_data/test.json") as json_file:
         fighters = json.load(json_file, parse_float=decimal.Decimal)

         for enu, fighter in enumerate(fighters, 1):
          FighterId = fighter['FighterId']
          Name = fighter['Name']
          Surname = fighter['Surname']
          Address = fighter['Address']
          Contact = fighter['Contact']
          Health = fighter['Health']
          FighterProfil = fighter['FighterProfile']
          Fights = fighter['Fights']
          LookingForFights = fighter['LookingForFights']
          Managers = fighter['Managers']
          print(f"{enu} Adding fighter:", FighterId, Name, Surname)
          table.put_item(
           Item={
            'FighterId': FighterId,
            'Name': Name,
            'Surname': Surname,
            'Address': Address,
            'Contact': Contact,
            'Health': Health,
            'FighterProfil': FighterProfil,
            'Fights': Fights,
            'LookingForFights': LookingForFights,
            'Managers': Managers,
           }
          )