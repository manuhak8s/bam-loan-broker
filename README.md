# bam-loan-broker-gui

## Configure Interfaces to Loan Broker
Coming soon ..

## Running with Python
The GUI contains two main components. **Please ensure that Python3, Flask and Streamlit are installed.**
**Best case:** Open a commandline for each component
It is recommended to start the FLASK-Server at first:
```bash
# navigate to your project
cd /location/to/your/project/location

# run 
python3 flask/server.py 
```

After the serverside component started successfully run the streamlit component:
```bash
# navigate to your project
cd /location/to/your/project/location

# create a python env 
pipenv shell

# run
streamlit run streamlit/form.py
```

**Trobleshooting:** In case of uninstalled modules, install them manually to the pipenv. 

## Running with Docker
Coming soon ..