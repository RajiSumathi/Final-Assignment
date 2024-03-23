# Final-Assignment

FLASK APPLICATION FOR QUERY COUNTING
This Flask application counts queries from a log file based on a provided date prefix. It provides a simple REST API endpoint to retrieve query counts.

Table of Contents:
Overview
Setup
Usage
API Endpoint
Error Handling

Overview:
The Query Counter Flask Application is built to analyze logs containing query information and count the number of queries based on a specified date prefix. The application utilizes Flask, a micro web framework for Python, to provide a RESTful API for accessing query counts.

Setup:
To set up the application, follow these steps:

1.Clone this repository to your local machine:
 git clone <repository-url>
2.Install the required dependencies using pip:
 pip install Flask pandas
3.Place your log file (hn_logs.tsv) in the project directory.

Usage:
To start the Flask application, run the following command:
 python app.py
 This will start the Flask development server, and you can access the API endpoint to retrieve query counts.

API Endpoint:
The API endpoint for retrieving query counts is:
 GET /1/queries/count/<date_prefix>
 Replace <date_prefix> with the date prefix you want to count queries for. The endpoint returns a JSON response containing the count of queries for the specified date prefix.

Example usage:
 GET http://localhost:5000/1/queries/count/2015-08
 This will return a JSON response with the count of queries for August 2015.

Error Handling:
If an error occurs during query counting (e.g., invalid date prefix or log file not found), the API will return an error message along with a status code of 500.
