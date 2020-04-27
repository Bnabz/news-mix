 
import os

class Config:
   
    NEWS_API_KEY = '4d2a9b72117b4ae0a28523b8a5a092e2'

class ProdConfig(Config):
 
    pass


class DevConfig(Config):
   

    DEBUG = True

config_options = {
    "development": DevConfig,
    "production": ProdConfig
}