# Data Pipelines with Airflow

## Set up container
You should configure the container following [Running AIrflow in Docker](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html).

This container supports AMD64/ARM64(*).

## Set up Airflow and AWS
You should follow the lessons of the [Airflow and AWS](https://learn.udacity.com/nanodegrees/nd027/parts/cd12380/lessons/06b794a9-945f-4a5f-bfd5-128a73501f1d/concepts/feb969b4-cf3b-450f-a6cb-73cd97c3e56b) in Automate Data Pipelines. 

### Create an IAM User in AWS
* Follow the steps on the page *[Create an IAM User in AWS](https://learn.udacity.com/nanodegrees/nd027/parts/cd12380/lessons/06b794a9-945f-4a5f-bfd5-128a73501f1d/concepts/feb969b4-cf3b-450f-a6cb-73cd97c3e56b)* in the lesson *Airflow and AWS*.

### Configure Redshift Serverless in AWS
* Follow the steps on the page *[Configure Redshift Serverless](https://learn.udacity.com/nanodegrees/nd027/parts/cd12380/lessons/06b794a9-945f-4a5f-bfd5-128a73501f1d/concepts/b9f7ebab-5112-4645-9a45-095d3643400e)* in the lesson *Airflow and AWS*.

### Connect Airflow and AWS
* Follow the steps on the page *Connections - AWS Credentials* in the lesson *Airflow and AWS*.
* Use the workspace provided on the page *Project Workspace* in this lesson.

### Connect Airflow to AWS Redshift Serverless
* Follow the steps on the page *Add Airflow Connections to AWS Redshift* in the lesson *Airflow and AWS*.
