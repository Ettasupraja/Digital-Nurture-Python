import configparser

class Config:
    pass

class DatabaseConfig(Config):
    pass

config = configparser.ConfigParser()
config.read("db.ini")

db = config["DATABASE"]

print("Host:", db["host"])
print("User:", db["user"])
print("Database:", db["database"])
