import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Customer Trusted
CustomerTrusted_node1682584556895 = glueContext.create_dynamic_frame.from_catalog(
    database="stedi",
    table_name="customer_trusted",
    transformation_ctx="CustomerTrusted_node1682584556895",
)

# Script generated for node Accelerometer Trusted
AccelerometerTrusted_node1682584724137 = glueContext.create_dynamic_frame.from_catalog(
    database="stedi",
    table_name="accelerometer_trusted",
    transformation_ctx="AccelerometerTrusted_node1682584724137",
)

# Script generated for node Join
CustomerTrusted_node1682584556895DF = CustomerTrusted_node1682584556895.toDF()
AccelerometerTrusted_node1682584724137DF = AccelerometerTrusted_node1682584724137.toDF()
Join_node2 = DynamicFrame.fromDF(
    CustomerTrusted_node1682584556895DF.join(
        AccelerometerTrusted_node1682584724137DF,
        (
            CustomerTrusted_node1682584556895DF["email"]
            == AccelerometerTrusted_node1682584724137DF["user"]
        ),
        "leftsemi",
    ),
    glueContext,
    "Join_node2",
)

# Script generated for node Drop Fields
DropFields_node1682577647921 = DropFields.apply(
    frame=Join_node2,
    paths=["user", "timestamp", "x", "y", "z"],
    transformation_ctx="DropFields_node1682577647921",
)

# Script generated for node Customer Curated
CustomerCurated_node3 = glueContext.getSink(
    path="s3://stedi-lakehouse-us-west-2/customer/curated/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    enableUpdateCatalog=True,
    transformation_ctx="CustomerCurated_node3",
)
CustomerCurated_node3.setCatalogInfo(
    catalogDatabase="stedi", catalogTableName="customer_curated"
)
CustomerCurated_node3.setFormat("json")
CustomerCurated_node3.writeFrame(DropFields_node1682577647921)
job.commit()
