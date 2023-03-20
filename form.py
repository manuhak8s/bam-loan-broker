##########################################################
# pipenv shell

# Running
# python -m streamlit run form.py

# is equivalent to:
# streamlit run form.py
##########################################################

import streamlit as st
import random, string, requests, time, os, yaml
import config

# shared result file for presentation rendering
resultFilePath = 'result.yaml'
open(resultFilePath, 'w').close()

# generateSSN generates a social security number based on german syntax
# (dd-dddddd-l-ddd)
# each chunk gets generated seperatly 
# the return value represents a concatination of all chunks
def generateSSN():
    chunk1 = random.randint(10,99)
    chunk2 = random.randint(100000, 999999)
    chunk3 = random.choice(string.ascii_letters)
    chunk4 = random.randint(100, 999)

    return str(chunk1) + str(chunk2) + chunk3.upper() + str(chunk4)

# sidebar of the streamlit app
st.sidebar.header("Your Results:")

# formular of the streamlit app
st.header("Welcome to the BAM Loan Broker")
with st.form("lb_form"):
   st.write("Please fill the required fields for accessing the best credit conditions")

   # form inputs
   ## forename and lastname
   fname = st.text_input("Forename", max_chars=15)
   lname = st.text_input("Lastname", max_chars=15)
   
   ## ssn - gets generated for easier testing
   randomSSN = generateSSN()
   ssn = st.text_input("Social Security Number", value=randomSSN, disabled=True)

   ## amount
   amount_min_val = 1000
   amount_count_step = 100
   amount = st.number_input('Desired Amount in €', min_value=amount_min_val, value=amount_min_val, step=amount_count_step)

   ## term 
   term_min_val = 6
   term_count_step = 1
   term = st.number_input('Desired Term in Months', min_value=term_min_val, value=term_min_val, step=term_count_step)

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       # input validation
       ## forename and lastname
       if len(fname) == 0 or len(fname) == 0:
        st.error("Both name fields are required!")
       ## amount and ter
       elif amount < amount_min_val or term < term_min_val:
        st.error("Amount or Term are invalid!")
       # request fireing
       else:
        st.write("fname", fname, "lname", lname, "amount", amount, "term", term)

        # url of the Rest-API route - flask server
        apiURL = "http://127.0.0.1:5000/api/v1/formdata"
        requestData = {
            'forename': fname,
            'lastname': lname,
            'ssn': ssn,
            'amount': amount,
            'term': term
        }
        requests.post(apiURL, json = requestData)

        # just for  result testing 
        apiURL = "http://127.0.0.1:5000/api/v1/result"
        requestData = {
            'test': 1,
        }
        requests.post(apiURL, json = requestData)

        time.sleep(2)
        # Load YAML data from the file
        with open(resultFilePath) as fh:
            read_data = yaml.load(fh, Loader=yaml.FullLoader)
        # Print YAML data before sorting
        print(read_data)
        # Sort YAML data based on keys
        sorted_data = yaml.dump(read_data)
        st.sidebar.write(sorted_data)