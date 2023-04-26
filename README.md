# bam-loan-broker-gui
This repository is based on a master's degree business integration lesson. 
The aim is to develop a loan broker ESB that communicates with different external systems.
A GUI is necessary for testing the loan broker component and is referenced in this repository.
The GUI is developed with Python-Streamlit as a single page application. The setup is described below.

## Setup - Configure Interfaces to Loan Broker
**Please ensure that Python3 and Streamlit are installed.**

**Step1:** Clone the repository

**Step2:** Modify the **/global.cfg**-file and set the groupname, group password and mule esb interface

**Step3:** Run your mule app if not done yet

**Step4:** Run the streamlit app as described below

```bash
# navigate to your project
cd /location/to/your/cloned/project

# (createing a python env could be necessary only if streamlit is not installed on host)
pipenv shell

# run
streamlit run streamlit/form.py
```

## Running with Docker
Coming soon ..