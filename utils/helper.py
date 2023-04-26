import random, string
import configparser

# generateSSN generates a social security number based on german syntax
# (dd-dddddd-l-ddd)
# each chunk gets generated seperatly 
# the return value represents a concatination of all chunks
def generate_ssn() -> str:
    chunk1: int = random.randint(10,99)
    chunk2: int = random.randint(100000, 999999)
    chunk3: str = random.choice(string.ascii_letters)
    chunk4: int = random.randint(100, 999)

    return str(chunk1) + str(chunk2) + chunk3.upper() + str(chunk4)

# Reading global config
# Get the configparser object
config_path: str = 'global.cfg'
config: configparser.ConfigParser = configparser.ConfigParser()
config.read(config_path, encoding='utf-8')

# get global group usernmae
def get_group_username() -> str:
    return config.get('groupdata', 'username')

# get global group password
def get_group_password() -> str:
    return config.get('groupdata', 'password')

# get global mule esb interface
def get_group_interface_route() -> str:
    return config.get('groupdata', 'interface_route')