# Salary-Pipeline
Pipeline that extracts salaries and locations from Salary.com's website for various analyst and engineering positions, such as data analyst, data engineer, software engineer and data scientist. The reason behind this pipeline is to essentially have transformed/structured data which I can use to create an application with Replit, to let users estimate salaries based on position, experience level and location. 

Pipeline Architecture:
![architecture (1)](https://user-images.githubusercontent.com/98634240/204114502-b41096a3-c501-4fa8-b704-a0353d3600fa.png)

Below are the steps followed: 
1. Scrape data from Salary.com which is returned as CSV files
2. Send CSV files to the first S3 bucket, which is the Bronze Zone
3. Trigger a Lambda function to merge all files together
4. Merged file is loaded to the second S3 bucket, the Silver Zone
5. Perform transformations within AWS Glue using PySpark, to create data into a structured format
6. Data is crawled from AWS Glue to Athena where SQL queries can be performed for insights
7. Load data into AWS RDS to store data for future use
8. Generate a Tableau dashboard for insights based on Athena queries, and use machine learning techniques to create a Streamlit app
