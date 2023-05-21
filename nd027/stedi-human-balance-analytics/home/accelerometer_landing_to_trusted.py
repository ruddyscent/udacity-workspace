import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame


def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)


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
Join_node2 = Join.apply(
    frame1=AccelerometerLanding_node1,
    frame2=CustomerTrusted_node1682555347507,
    keys1=["user"],
    keys2=["email"],
    transformation_ctx="Join_node2",
)

# Script generated for node SQL Query
SqlQuery0 = """
select * from myDataSource
where myDataSource.sharewithresearchasofdate <= myDataSource.timeStamp
"""
SQLQuery_node1682610897864 = sparkSqlQuery(
    glueContext,
    query=SqlQuery0,
    mapping={"myDataSource": Join_node2},
    transformation_ctx="SQLQuery_node1682610897864",
)

# Script generated for node Drop Fields
DropFields_node1682577758236 = DropFields.apply(
    frame=SQLQuery_node1682610897864,
    paths=[
        "email",
        "serialnumber",
        "lastupdatedate",
        "sharewithpublicasofdate",
        "registrationdate",
        "sharewithresearchasofdate",
        "sharewithfriendsasofdate",
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
