import streamlit as st
import asyncio
import streamlit as st
from utils import helper, request_controller


group_username: str = helper.get_group_username()
group_password: str = helper.get_group_password()
request_url: str = helper.get_group_interface_route()


def main():
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

        rating_level: str = st.text_input("Rating Level", max_chars=1, value='A')

        delay_min_val: int = 0
        delay_step: int = 1000
        delay_in_milliseconds: int = st.number_input("Delay in Milliseconds", min_value=delay_min_val, value=delay_step, step=delay_step)
            
        ## amount
        amount_min_val: int = 1000
        amount_count_step: int = 1000
        amount_in_euros: int = st.number_input('Desired Amount in €', min_value=amount_min_val, value=amount_min_val, step=amount_count_step)

        ## term 
        term_min_val: int = 6
        term_count_step: int = 1
        term_in_months: int = st.number_input('Desired Term in Months', min_value=term_min_val, value=term_min_val, step=term_count_step)

        # Every form must have a submit button.
        submitted: bool = st.form_submit_button("Submit")
        if submitted:

            try: 
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)

                # request handling
                request_object = request_controller.Loan_Broker_Request(
                    social_security_number, rating_level, 
                    delay_in_milliseconds, 
                    group_username, 
                    group_password, 
                    amount_in_euros, 
                    term_in_months
                )
                request_data = request_controller.translate_object_to_dict(request_object)
                response_json = loop.run_until_complete(request_controller.async_main(request_url, request_data))

                #response_data = json.loads(response_json)
                lending_rate = response_json['lendingRate']



                st.sidebar.header("Best Credit Offers for " + fname + " " + lname)
                st.sidebar.write("Your SSN: " + social_security_number)
                st.sidebar.write("Desired Amount : " + str(amount_in_euros) + '€')
                st.sidebar.write("Desired Term: " + str(term_in_months) + ' months')

                st.sidebar.success("Your Lending Rate of Deutsche Bank: " + str(lending_rate))
            except:
                st.error("Connection error while reaching the ESB.")
                st.warning("Did you start the Mule App or do you have internet connection problems?")

if __name__ == '__main__':
    main()