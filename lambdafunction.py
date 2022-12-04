import boto3
import pandas as pd

def lambda_handler(event, context):
    # Get the S3 resource
    s3 = boto3.resource('s3')
    source_bucket = s3.Bucket('')

    destination_bucket = s3.Bucket('salary-pipeline-dev')

    # Get a list of CSV files in the source bucket
    csv_files = [obj.key for obj in source_bucket.objects.filter(Suffix='.csv')]

    # Load the data from each CSV file into a DataFrame
    dfs = [pd.read_csv(f"s3://cleansed-salary-dev/{file}") for file in csv_files]

    # Merge the DataFrames
    df = pd.concat(dfs, axis=0)

    # Write the DataFrame to a new CSV file
    csv_data = df.to_csv(index=False)

    # Upload the new CSV file to the destination bucket
    destination_bucket.upload_file(
        Filename='merged_data.csv',
        Key='merged_data.csv',
        Body=csv_data
    )