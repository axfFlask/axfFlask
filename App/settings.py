def get_db_uri(dbinfo):
    user = dbinfo.get("USER") or "root"
    password = dbinfo.get("PASSWORD") or "rock1204"
    host = dbinfo.get("HOST") or "localhost"
    port = dbinfo.get("PORT") or "3306"
    name = dbinfo.get("NAME") or "nihao"
    db = dbinfo.get("DB") or "mysql"
    driver = dbinfo.get("DRIVER") or "pymysql"

    return "{}+{}://{}:{}@{}:{}/{}".format(db, driver, user, password, host, port, name)


class Config():
    DEBUG = False
    TESTING = False
    SECRET_KEY = "110"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = 'redis'


class DevelopConfig(Config):
    DEBUG = True
    DATABASE = {
        "USER": 'root',
        "PASSWORD": 'rock1204',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'nihao',
        'DB': 'mysql',
        'DRIVER': 'pymysql'
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class TestingConfig(Config):
    TESTING = True
    DATABASE = {
        "USER": 'root',
        "PASSWORD": 'rock1204',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'nihao',
        'DB': 'mysql',
        'DRIVER': 'pymysql'
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class StaggingConfig(Config):
    DEBUG = True
    DATABASE = {
        "USER": 'root',
        "PASSWORD": 'rock1204',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'nihao',
        'DB': 'mysql',
        'DRIVER': 'pymysql'
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class ProductConfig(Config):
    DEBUG = True
    DATABASE = {
        "USER": 'root',
        "PASSWORD": 'rock1204',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'nihao',
        'DB': 'mysql',
        'DRIVER': 'pymysql'
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


env = {
    "develop": DevelopConfig,
    "testing": TestingConfig,
    "stagging": StaggingConfig,
    "product": ProductConfig,
    "default": DevelopConfig
}
