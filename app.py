from __future__ import print_function  # Python 2/3 compatibility

import decimal
import json

import boto3

from database.create_db import DockerizeDynamoDB

db = DockerizeDynamoDB("Fighters")
# db.create_db()
# print(db.get_table())
#
# db.drop_table()
# print(db.get_table())

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

table = dynamodb.Table('Fighters')

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