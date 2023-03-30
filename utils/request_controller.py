import requests

# class of loanbroker request
# conatains all necessary attributes for a request to the loanbroker
# social security number
# rating level
# delay in milliseconds
# username
# password
# amount in euros
# term in months
class Loan_Broker_Request:
  def __init__(self, social_security_number, rating_level, delay_in_milliseconds, username, password, amount_in_euros, term_in_months):
    self.social_security_number = social_security_number
    self.rating_level = rating_level
    self.delay_in_milliseconds = delay_in_milliseconds
    self.username = username
    self.password = password
    self.amount_in_euros = amount_in_euros
    self.term_in_months = term_in_months

# translation of a python class instance to a dict
def translate_object_to_dict(object) -> dict:
    return object.__dict__

# fire_loan_broker_request sends a request based on dict data to a target url
# the return value is a response in json
def fire_loan_broker_request(loan_broker_interface_route, request_dict):
    response = requests.post(loan_broker_interface_route, json = request_dict)
    return response.json()