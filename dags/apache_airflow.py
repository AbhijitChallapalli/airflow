import logging
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import uuid
import requests
import json

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO)

def get_data():
    response = requests.get("https://randomuser.me/api/")
    response = response.json()
    user_data = response['results'][0]
    return user_data

def format_data(user_data):
    location = user_data['location']
    formatted_data = {
        'id': str(uuid.uuid4()),
        'first_name': user_data['name']['first'],
        'last_name': user_data['name']['last'],
        'gender': user_data['gender'],
        'address': f"{location['street']['number']} {location['street']['name']}, {location['city']}, {location['state']}, {location['country']}",
        'post_code': location['postcode'],
        'email': user_data['email'],
        'username': user_data['login']['username'],
        'dob': user_data['dob']['date'],
        'registered_date': user_data['registered']['date'],
        'phone': user_data['phone'],
        'picture': user_data['picture']['medium']
    }
    return formatted_data

def stream_data():
    user_data = get_data()
    formatted_data = format_data(user_data)
    logging.info(json.dumps(formatted_data, indent=3))

default_args = {
    'owner': 'Abhijit',
    'start_date': datetime(2024, 6, 19, 1, 35)
}

with DAG('automation', default_args=default_args, schedule_interval='@daily', catchup=False) as dag:
    streaming_task = PythonOperator(
        task_id='stream_data_from_api',
        python_callable=stream_data
    )

stream_data()