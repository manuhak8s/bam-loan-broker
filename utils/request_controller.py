import requests
import aiohttp
import json

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

# sending a async post request during a http session based on aiohttp package
# returning an awaiting json response
async def send_request(url, data):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as response:
            response_text = await response.text()
            return json.loads(response_text)

# calling send_request based on goven url and given request data
async def async_main(url, data):
    response_json = await send_request(url, data)
    return response_json