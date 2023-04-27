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

# Script generated for node Accelerometer Landing
AccelerometerLanding_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://stedi-lakehouse-us-west-2/accelerometer/landing/"],
        "recurse": True,
    },
    transformation_ctx="AccelerometerLanding_node1",
)

# Script generated for node Customer Trusted
CustomerTrusted_node1682555347507 = glueContext.create_dynamic_frame.from_catalog(
    database="stedi",
    table_name="customer_trusted",
    transformation_ctx="CustomerTrusted_node1682555347507",
)

# Script generated for node Join
AccelerometerLanding_node1DF = AccelerometerLanding_node1.toDF()
CustomerTrusted_node1682555347507DF = CustomerTrusted_node1682555347507.toDF()
Join_node2 = DynamicFrame.fromDF(
    AccelerometerLanding_node1DF.join(
        CustomerTrusted_node1682555347507DF,
        (
            AccelerometerLanding_node1DF["user"]
            == CustomerTrusted_node1682555347507DF["email"]
        ),
        "leftsemi",
    ),
    glueContext,
    "Join_node2",
)

# Script generated for node Drop Fields
DropFields_node1682577758236 = DropFields.apply(
    frame=Join_node2,
    paths=[
        "email",
        "serialnumber",
        "sharewithfriendsasofdate",
        "sharewithpublicasofdate",
        "registrationdate",
        "sharewithresearchasofdate",
        "lastupdatedate",
    ],
    transformation_ctx="DropFields_node1682577758236",
)

# Script generated for node Accelerometer Trusted
AccelerometerTrusted_node3 = glueContext.getSink(
    path="s3://stedi-lakehouse-us-west-2/accelerometer/trusted/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    enableUpdateCatalog=True,
    transformation_ctx="AccelerometerTrusted_node3",
)
AccelerometerTrusted_node3.setCatalogInfo(
    catalogDatabase="stedi", catalogTableName="accelerometer_trusted"
)
AccelerometerTrusted_node3.setFormat("json")
AccelerometerTrusted_node3.writeFrame(DropFields_node1682577758236)
job.commit()
