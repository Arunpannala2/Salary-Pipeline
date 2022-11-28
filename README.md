# Salary-Pipeline
Pipeline that extracts salaries and locations from Salary.com's website for various analyst and engineering positions, such as data analyst, data engineer, software engineer and data scientist. The reason behind this pipeline is to essentially have transformed/structured data which I can use to create an application with Replit, to let users estimate salaries based on position, experience level and location. 

![architecture (2)](https://user-images.githubusercontent.com/98634240/204208972-de1a9dc3-b00d-4ed4-926a-042c22b9698d.png)


Below are the steps followed: 
1. Scrape data from Salary.com which is returned as CSV files
2. Send CSV files to the first S3 bucket, which is the Bronze Zone
3. Trigger a Lambda function to merge all files together
4. Merged file is loaded to the second S3 bucket, the Silver Zone
5. Perform transformations within AWS Glue using PySpark, to transform data into a structured format
6. Data is crawled with AWS Glue to Athena where SQL queries can be performed for insights
7. Load data into AWS RDS to store data for future use
8. Generate a Power BI dashboard for insights based on Athena queries, and use machine learning techniques to create a Streamlit app
