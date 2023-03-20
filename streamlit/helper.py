##########################################################
# streamlit frontend helpers
##########################################################

import random, string

# path to fileshare
fshare_path = 'fshare/result.yaml'

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

# clears the shared file for reading and visualizing the latest result
def clear_fshare():
    open(fshare_path, 'w').close()