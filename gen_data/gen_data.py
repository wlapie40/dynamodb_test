import json
import random
from uuid import uuid4

from random_data import (
    gen_random_record,
    gen_phone_number,
)
from read_csv import (
    read_csv_address,
    read_csv_name_surname, )

FIGHT_STYLE = [
    'Boxing', 'Muay Thai/Kickboxing',
    'Brazilian jiu-jitsu / Grappling',
    'Wrestling']

CATEGORY_WEIGHT = [
    'Strawweight', 'Flyweight', 'Bantamweight', 'Featherweight', 'Lightweight',
    'Welterweight',
    'Middleweight', 'Light Heavyweight', 'Heavyweight']

MMA_CLUBS = [
    'Alliance MMA', 'American Top Team',
    'Jackson-Wink MMA',
    'SBG Ireland', 'Team Alpha Male', 'Tristar Gym']


def gen_data_fighter_table_data(file_name, num_records=100):
    addresses_list = read_csv_address()*5
    names_surnames_list = read_csv_name_surname()*5

    container = []
    for el in range(num_records):
        names_surnames = names_surnames_list[el]
        addresses = addresses_list[el]
        obj={
            "FighterId": str(uuid4()),
            "Name": names_surnames[0],
            "Surname": names_surnames[1],
            "Address": {
                "Continent": addresses[0],
                "Country": addresses[1],
                "State": f"{'none' if addresses[2]=='' else addresses[2]}",
                "City": addresses[3]
            },
            "Contact": {
                "PhoneNumber": gen_phone_number(),
                "Email": f"{names_surnames[0]+'.'+names_surnames[1]}@gmail.com"
            },
            "Health": {
                "HealthStatus": random.choice([True, False]),
                "ReadyToFight": "2019-20-10",
                "Descritpion": "none"
            },
            "FighterProfile":{
                "Born": "1984-06-17",
                "Class": random.choice(CATEGORY_WEIGHT),
                "PreferredStyle": random.choice(FIGHT_STYLE),
                "Height": "6'2",
                "WeightLBS": 185,
                "WeightKG": 83.91,
                "Association": random.choice(MMA_CLUBS),
                "Record": {"Wins": gen_random_record(), "Losses": gen_random_record()}
            },
            "Fights": {},
            "LookingForFights": random.choice([True, False]),
            "Managers": gen_random_record()
        }
        container.append(obj)

    with open(f'{file_name}.json', 'w') as outfile:
        json.dump(container, outfile, indent=4)


gen_data_fighter_table_data('test', 10)
