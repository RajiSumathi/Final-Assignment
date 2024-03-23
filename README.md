# Final-Assignment

FLASK APPLICATION FOR QUERY COUNTING:
This Flask application counts queries from a log file based on a provided date prefix. It provides a simple REST API endpoint to retrieve query counts.

Table of Contents:
Overview,
prerequisites,
Setup,
Explanation,
Usage,
Error Handling

Overview:
The Query Counter Flask Application is built to analyze logs containing query information and count the number of queries based on a specified date prefix. The application utilizes Flask, a micro web framework for Python, to provide a RESTful API for accessing query counts.

Prerequisites:
Before running the application, make sure you have the following installed:

Python 3.x,
Flask,
pandas

Setup:
To set up the application, follow these steps:

1)Clone this repository to your local machine:
 git clone <repository-url>
 
2)Install the required dependencies using pip:
 pip install Flask pandas
 
3)Place your log file (hn_logs.tsv) in the project directory.

Explanation:

1)Import Libraries: It imports necessary libraries such as pandas for data manipulation, urllib.parse for URL decoding, datetime for handling date and time, and Flask for creating the web application.

2)Set Constants: It defines constants such as the path to the log file (LOG_FILE_PATH) and a list of date formats (DATE_FORMATS) to be used for parsing dates.

3)Define Functions:

 *preprocess_logs: Reads the log file into a DataFrame and converts the first column to datetime format.

 *decode_url: Decodes a URL to extract the domain name.

 *get_count: Counts the number of queries in the log file for a given date prefix using various date formats.

4)API Endpoint: Defines a Flask route (/1/queries/count/<date_prefix>) that handles HTTP GET requests. When a request is received, it preprocesses the log file, counts the queries for the specified date prefix, and returns the count as a JSON response.

5)Run the Application: If the script is executed directly (i.e., not imported as a module), the Flask application is started in debug mode.

Usage:
To start the Flask application, run the following command:
 python app.py,
 This will start the Flask development server, and you can access the API endpoint to retrieve query counts.

Error Handling:
If an error occurs during query counting (e.g., invalid date prefix or log file not found), the API will return an error message along with a status code of 500.

Output:

<img width="695" alt="Screenshot 2024-03-23 at 11 08 13 PM" src="https://github.com/RajiSumathi/Final-Assignment/assets/164464238/e025d33b-3d2a-42e0-b80d-967b51ea43fd">
<img width="923" alt="Screenshot 2024-03-23 at 11 09 52 PM" src="https://github.com/RajiSumathi/Final-Assignment/assets/164464238/643e6dd1-4248-4521-a739-f2653f27e7e3">
<img width="733" alt="Screenshot 2024-03-23 at 11 10 31 PM" src="https://github.com/RajiSumathi/Final-Assignment/assets/164464238/89d5fc9a-83c1-4b34-973f-1eaa5a40345e">
<img width="699" alt="Screenshot 2024-03-23 at 11 11 24 PM" src="https://github.com/RajiSumathi/Final-Assignment/assets/164464238/13332d67-7466-407f-b6f6-3fb79bc5d800">
<img width="718" alt="Screenshot 2024-03-23 at 11 12 27 PM" src="https://github.com/RajiSumathi/Final-Assignment/assets/164464238/4c41ab9c-0752-45b5-b95b-b061e668b656">


