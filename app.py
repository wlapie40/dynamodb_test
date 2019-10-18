from __future__ import print_function  # Python 2/3 compatibility

from config.config import get_config
from database.create_db import DynamoDB

config = get_config()
db = DynamoDB(table_name=config.TABLE_NAME, client=config.CLIENT, region=config.AWS_REGION, resource = config.RESOURCE)
db.create_db()
db.populate_fighters_table()
#
# db.check_if_table_exists()