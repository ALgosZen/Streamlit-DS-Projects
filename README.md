# Streamlit-DS-Projects
This project demostrates how to create data science web apps real fast and depoly to cloud servers, in this precisely AWS EC2 and ECS. Streamlit is a python library very popular to build and share datascience applications.

Lets proceed and create python virtual env
## python3 -m venv env && source ./env/bin/activate 
If any trouble with the command above, make sure you have python installed.
Install additional packages as follows
### pip install streamlit pandas plotly psycopg2

Create a dashboard.py file and enter
st.title("Streamlit DataScience Project Dashboard")
## save and run the project
### streamlit run dashboard.py

application will start in browser :
## http://localhost:8501/

few commands to activate, deactivate, freeze requirement and install project in another machine.
## pip list - to list all packages
## deactivate the virtual env
## pip freeze requirement.txt(you have to activate env first)
## pip install -r requirement.txt (you have to activate the env first)


