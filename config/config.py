import os
from dotenv import load_dotenv
import boto3

load_dotenv()


class Config:
    PORT = os.getenv("PORT")
    HOST = os.getenv("HOST")
    AWS_REGION = os.getenv("AWS_REGION")
    TABLE_NAME = os.getenv("TABLE_NAME")


class DevConfig(Config):
    CLIENT = boto3.client('dynamodb', endpoint_url=f"http://{Config.HOST}:{Config.PORT}")
    RESOURCE = boto3.resource('dynamodb', endpoint_url=f"http://{Config.HOST}:{Config.PORT}")


class ProdConfig(Config):
    CLIENT = boto3.client('dynamodb', region_name=f'{Config.AWS_REGION}')
    RESOURCE = boto3.resource('dynamodb', region_name=f'{Config.AWS_REGION}')


def get_config():
    app_env = {"dev": DevConfig,
               "prod": ProdConfig}

    print(f"Current env: {os.getenv('APP_ENV')}")
    return app_env[os.getenv('APP_ENV')]
