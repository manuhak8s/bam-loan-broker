import random, string
import configparser

# generateSSN generates a social security number based on german syntax
# (dd-dddddd-l-ddd)
# each chunk gets generated seperatly 
# the return value represents a concatination of all chunks
def generate_ssn():
    chunk1 = random.randint(10,99)
    chunk2 = random.randint(100000, 999999)
    chunk3 = random.choice(string.ascii_letters)
    chunk4 = random.randint(100, 999)

    return str(chunk1) + str(chunk2) + chunk3.upper() + str(chunk4)

#Get the configparser object
config_path = 'global.cfg'
config = configparser.ConfigParser()
config.read(config_path, encoding='utf-8')

def get_group_username():
    return config.get('groupdata', 'username')

def get_group_password():
    return config.get('groupdata', 'password')

def get_group_interface_route():
    return config.get('groupdata', 'interface_route')