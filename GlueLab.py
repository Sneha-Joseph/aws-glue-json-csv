import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql import functions as SqlFuncs

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node Amazon S3
AmazonS3_node1757834560482 = glueContext.create_dynamic_frame.from_options(format_options={"multiLine": "false"}, connection_type="s3", format="json", connection_options={"paths": ["s3://mybuckinput0hjyfuukdtuiutgjtu/emp_json.json"], "recurse": True}, transformation_ctx="AmazonS3_node1757834560482")



# Script generated for node Drop Duplicates
DropDuplicates_node1757834696666 =  DynamicFrame.fromDF(AmazonS3_node1757834560482.toDF().dropDuplicates(), glueContext, "DropDuplicates_node1757834696666")

# Script generated for node Select Fields
SelectFields_node1757835877601 = SelectFields.apply(frame=DropDuplicates_node1757834696666, paths=["emp_id", "name", "salary", "address"], transformation_ctx="SelectFields_node1757835877601")
SelectFields_node1757835877601 = SelectFields_node1757835877601.repartition(1)
# Script generated for node AmazonS3out
EvaluateDataQuality().process_rows(frame=SelectFields_node1757835877601, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1757834555861", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3out_node1757836358609 = glueContext.write_dynamic_frame.from_options(frame=SelectFields_node1757835877601, connection_type="s3", format="csv", connection_options={"path": "s3://mybuckoutputcvhdjkgj", "partitionKeys": []}, transformation_ctx="AmazonS3out_node1757836358609")

job.commit()