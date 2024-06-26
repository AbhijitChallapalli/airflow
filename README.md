Real-Time Data Processing with Apache Airflow
This repository contains the Apache Airflow DAGs designed to fetch and process real-time data from a public API, demonstrating a simple yet powerful use-case of Airflow in data engineering.

https://github.com/AbhijitChallapalli/airflow/assets/83178772/dfd60c54-b7cd-43fe-9dbb-393b988d62a6

## Project Structure
The pipeline is structured as follows:

  API ➡️ Fetch Data ➡️ Process Data ➡️ Log Results

## Prerequisites
Python 3.7+
Apache Airflow 2.0+

## Installation
Set Up Environment

Ensure Python and Apache Airflow are installed on your machine.
Install required Python packages:
```bash
pip install requirements.txt
```
Initialize Airflow

Set up the Airflow environment:
```bash
airflow db init
```

Start Airflow

Run the following command to start the Airflow web server:
```bash
airflow webserver -p 8080
```

Running the DAG
The DAG automation is scheduled to run daily. It fetches user data from the API and processes it to log structured information including user details and demographics.

Contributing
Contributions are welcome! Please feel free to submit pull requests or open issues to suggest improvements or additional features.

