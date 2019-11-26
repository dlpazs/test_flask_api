class Config:
    DEBUG = False


class ProdConfig(Config):
    DEBUG = False
    CACHE_TYPE = "simple"
    CACHE_DEFAULT_TIMEOUT = 50


class DevConfig(Config):
    DEBUG = True
    CACHE_TYPE = "simple"
    CACHE_DEFAULT_TIMEOUT = 300
