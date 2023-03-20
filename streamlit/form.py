##########################################################
# pipenv shell

# Running
# python -m streamlit run form.py

# is equivalent to:
# streamlit run form.py
##########################################################

import streamlit as st
import requests, time, yaml, helper, sys

# formular of the streamlit app
st.header("Welcome to the BAM Loan Broker")
with st.form("lb_form"):
   st.write("Please fill the required fields for accessing the best credit conditions")

   # form inputs
   ## forename and lastname
   fname = st.text_input("Forename", max_chars=15)
   lname = st.text_input("Lastname", max_chars=15)
   
   ## ssn - gets generated for easier testing
   randomSSN = helper.generate_ssn()
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
        helper.clear_fshare()

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
        with open(helper.fshare_path) as fh:
            read_data = yaml.load(fh, Loader=yaml.FullLoader)
        # Print YAML data before sorting
        print(read_data)
        # Sort YAML data based on keys
        sorted_data = yaml.dump(read_data)
        # sidebar of the streamlit app
        st.sidebar.header("Your Data:")
        st.sidebar.write("Name: " + fname + " " + lname)
        st.sidebar.write("SSN: " + ssn)
        st.sidebar.write("Credit Amount: " + str(amount) + "€")
        st.sidebar.write("Credit Term: " + str(term) + " months")
        st.sidebar.header("Recommended Credit Offers:")
        st.sidebar.write(sorted_data)