##########################################################
# to run: FLASK_APP=server.py flask run
# or python3 server.py
##########################################################

import json, yaml
import requests
import config
from flask import Flask, request
app = Flask(__name__)

# dummy result for testing
dummy_result = {
    'result': ['bank a', 'bank b', 'bank c']
}

# main route (unecessary)
@app.route("/")
def main():
    return '<h1>BAM Loan Broker Proxy</h1>'

# recieves form data from the streamlit app
@app.route("/api/v1/formdata", methods=['POST'])
def get_formdata():
    req_data = request.get_json()
    print(req_data)
    # TODO: send data to the loan broker component (not implemented yet)
    return req_data

# recieves result from the loan broker component (at the moment only with dummy data)
# saves the result in a file share with streamlit access
@app.route("/api/v1/result", methods=['POST'])
def get_result():
    # coming soon ...
    req_data = request.get_json()
    print(req_data)
    # writes the result to a shared yaml file
    with open('result.yaml', 'w') as outfile:
       yaml.dump(dummy_result, outfile, default_flow_style=False)

    return {
        'result': dummy_result
    }

if __name__ == '__main__':
	app.run(debug=True)