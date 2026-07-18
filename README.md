Ecommerce Data Pipeline

An end-to-end data engineering project that builds a data pipeline using Apache Airflow, Python, PostgreSQL, and Docker. The pipeline extracts, transforms, and loads ecommerce transaction data into a star schema data warehouse for analytics.

Project Overview

This project demonstrates a modern data engineering workflow by orchestrating ETL tasks with Apache Airflow. The entire environment is containerized using Docker Compose, making it easy to deploy and reproduce.

Features
Automated ETL workflow using Apache Airflow
Data cleaning and transformation with Python (Pandas)
PostgreSQL data warehouse with star schema
Dockerized environment for reproducibility
Airflow DAG scheduling and monitoring
Modular project structure for scalability
Tech Stack
Python
Apache Airflow 3.3
PostgreSQL
Docker & Docker Compose
Pandas
SQLAlchemy
psycopg2
SQL

Architecture
                Raw Ecommerce Dataset
                        │
                        ▼
                  Extract (Python)
                        │
                        ▼
               Transform & Clean Data
                        │
                        ▼
              Load into PostgreSQL
                        │
                        ▼
           Star Schema Data Warehouse
                        │
                        ▼
          Apache Airflow DAG Orchestration
          
Project Structure
ecommerce-data-pipeline/
│
├── dags/                  # Airflow DAG definitions
├── scripts/               # ETL scripts
├── sql/                   # SQL scripts
├── data/                  # Sample dataset (optional)
├── logs/                  # Airflow logs
├── plugins/
├── config/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
Data Warehouse Schema
Dimension Tables
dimCustomer
dimProduct
Fact Table
factSales

The warehouse follows a simple star schema to support analytical queries.

Pipeline Workflow
Extract raw ecommerce transaction data.
Clean missing and invalid records.
Transform data into dimensional format.
Load data into PostgreSQL.
Airflow orchestrates and monitors the workflow.


Getting Started

Prerequisites
Docker Desktop
Git

Clone the repository
git clone https://github.com/<your-username>/ecommerce-data-pipeline.git
cd ecommerce-data-pipeline
Configure environment variables

Copy the example environment file:

cp .env.example .env

Update the values in .env as needed.

Start Docker desktop

Build the Docker custom images: docker compose build
Initialize Airflow: docker compose up airflow-init
Start the project: docker compose up -d
Access Airflow

Open:

http://localhost:8080

Login using the credentials configured in your .env file.

Skills Demonstrated
Data Engineering
ETL Pipeline Development
Apache Airflow
Workflow Orchestration
PostgreSQL
SQL
Python
Docker
Data Modeling
Star Schema Design
Environment Management
Version Control with Git

Future Improvements
Integrate cloud object storage (AWS S3)
Add automated data quality validation
Implement incremental data loading
Add unit and integration tests
Create a BI dashboard (Power BI or Tableau)
Deploy using cloud infrastructure
Notes

This project was developed as a portfolio project to demonstrate practical data engineering concepts, including workflow orchestration, containerization, and relational data modeling.
