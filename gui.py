from utils import helper

##########################################################
# pipenv shell

# Running
# python -m streamlit run form.py

# is equivalent to:
# streamlit run form.py
##########################################################

import streamlit as st
import streamlit_authenticator as stauth
import yaml, time
from yaml.loader import SafeLoader
from utils import data_controller, helper, request_controller

group_username: str = helper.get_group_username()
group_password: str = helper.get_group_password()
request_url: str = helper.get_group_interface_route()

# formular of the streamlit app
st.header("Welcome to the BAM Loan Broker")
with st.form("lb_form"):
    st.write("Please fill the required fields for accessing the best credit conditions")

    # form inputs
    ## forename and lastname
    fname: str = st.text_input("Forename", max_chars=15)
    lname: str = st.text_input("Lastname", max_chars=15)
        
    ## ssn - gets generated for easier testing
    randomSSN: str = helper.generate_ssn()
    social_security_number: str = st.text_input("Social Security Number", value=randomSSN, disabled=True)

    rating_level: str = st.text_input("Rating Level", max_chars=1)

    delay_min_val: int = 0
    delay_in_milliseconds: int = st.number_input("Delay in Milliseconds", min_value=delay_min_val, value=delay_min_val)
        
    ## amount
    amount_min_val: int = 1000
    amount_count_step: int = 100
    amount_in_euros: int = st.number_input('Desired Amount in €', min_value=amount_min_val, value=amount_min_val, step=amount_count_step)

        ## term 
    term_min_val: int = 6
    term_count_step: int = 1
    term_in_months: int = st.number_input('Desired Term in Months', min_value=term_min_val, value=term_min_val, step=term_count_step)

    # Every form must have a submit button.
    submitted: bool = st.form_submit_button("Submit")
    if submitted:
        # post validaiton

        # request handling
        #request_object = request_controller.Loan_Broker_Request(
        #    social_security_number, rating_level, 
        #    delay_in_milliseconds, 
        #    group_username, 
        #    group_password, 
        #    amount_in_euros, 
        #    term_in_months
        #    )
        #request_data = request_controller.translate_object_to_dict(request_object)
        #request_controller.fire_loan_broker_request(request_url, request_data)

        time.sleep(2)

        demo_result: dict = {
            "Deutsche Bank": 3.6,
            "Commerzbank": 7.1,
            "Volksbank": 7.2
        }

        st.sidebar.header("Best Lending Rates for " + fname + " " + lname)
        st.sidebar.write("Your SSN: " + social_security_number)
        st.sidebar.write("Desired Amount : " + str(amount_in_euros) + '€')
        st.sidebar.write("Desired Term: " + str(term_in_months) + ' months')

        st.sidebar.header("Recommended Credit Offers:")
        rank_count: int = 0
        for bank, lending_rate in demo_result.items():
            rank_count = rank_count + 1
            if rank_count == 1:
                st.sidebar.success(str(rank_count) + " - " + bank + " " + bank + " " + str(lending_rate))
            else:
                st.sidebar.info( str(rank_count) + " - " + bank + " " + bank + " " + str(lending_rate))

                # response visualization
                # sidebar of the streamlit app
                #st.sidebar.header("Your Data:")
                #st.sidebar.write("Name: " + fname + " " + lname)
                #st.sidebar.write("SSN: " + ssn)
                #st.sidebar.write("Credit Amount: " + str(amount) + "€")
                #st.sidebar.write("Credit Term: " + str(term) + " months")
                #st.sidebar.header("Recommended Credit Offers:")
                #st.sidebar.write(sorted_data)    