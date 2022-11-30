import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
## @type: DataSource
## @args: [database = "default", table_name = "merged_salaries", transformation_ctx = "datasource0"]
## @return: datasource0
## @inputs: []
datasource0 = glueContext.create_dynamic_frame.from_catalog(database = "default", table_name = "merged_salaries", transformation_ctx = "datasource0")
## @type: ApplyMapping
## @args: [mapping = [("title", "string", "title", "string"), ("location", "string", "location", "string"), ("ntile10", "long", "ntile10", "long"), ("ntile25", "long", "ntile25", "long"), ("ntile50", "long", "ntile50", "long"), ("ntile75", "long", "ntile75", "long"), ("ntile90", "long", "ntile90", "long")], transformation_ctx = "applymapping1"]
## @return: applymapping1
## @inputs: [frame = datasource0]
applymapping1 = ApplyMapping.apply(frame = datasource0, mappings = [("title", "string", "title", "string"), ("location", "string", "location", "string"), ("ntile10", "long", "ntile10", "long"), ("ntile25", "long", "ntile25", "long"), ("ntile50", "long", "ntile50", "long"), ("ntile75", "long", "ntile75", "long"), ("ntile90", "long", "ntile90", "long")], transformation_ctx = "applymapping1")
## @type: ResolveChoice
## @args: [choice = "make_struct", transformation_ctx = "resolvechoice2"]
## @return: resolvechoice2
## @inputs: [frame = applymapping1]
resolvechoice2 = ResolveChoice.apply(frame = applymapping1, choice = "make_struct", transformation_ctx = "resolvechoice2")
## @type: DropNullFields
## @args: [transformation_ctx = "dropnullfields3"]
## @return: dropnullfields3
## @inputs: [frame = resolvechoice2]
dropnullfields3 = DropNullFields.apply(frame = resolvechoice2, transformation_ctx = "dropnullfields3")
## @type: DataSink
## @args: [connection_type = "s3", connection_options = {"path": "s3://cleansed-salary-dev/parquet-files/"}, format = "parquet", transformation_ctx = "datasink4"]
## @return: datasink4
## @inputs: [frame = dropnullfields3]

datasink1 = dropnullfields3.toDF().coalesce(1)
df_final_output = DynamicFrame.fromDF(datasink1, glueContext, "transformed_output")
datasink4 = glueContext.write_dynamic_frame.from_options(frame = dropnullfields3, connection_type = "s3", connection_options = {"path": "s3://cleansed-salary-dev/parquet-files/", "partitionKeys": ["location"]}, format = "parquet", transformation_ctx = "datasink4")
job.commit() 
