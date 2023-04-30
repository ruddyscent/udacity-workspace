import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
import re
from pyspark.sql import functions as SqlFuncs

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Customer Landing
CustomerLanding_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://stedi-lakehouse-us-west-2/customer/landing/"],
        "recurse": True,
    },
    transformation_ctx="CustomerLanding_node1",
)

# Script generated for node Privacy Opt-In
PrivacyOptIn_node2 = Filter.apply(
    frame=CustomerLanding_node1,
    f=lambda row: (not (row["shareWithResearchAsOfDate"] == 0)),
    transformation_ctx="PrivacyOptIn_node2",
)

# Script generated for node Drop Duplicated Account
DropDuplicatedAccount_node1682785868953 = DynamicFrame.fromDF(
    PrivacyOptIn_node2.toDF().dropDuplicates(["email"]),
    glueContext,
    "DropDuplicatedAccount_node1682785868953",
)

# Script generated for node Drop PII
DropPII_node1682600262207 = DropFields.apply(
    frame=DropDuplicatedAccount_node1682785868953,
    paths=["birthDay", "phone", "customerName"],
    transformation_ctx="DropPII_node1682600262207",
)

# Script generated for node Customer Trusted
CustomerTrusted_node3 = glueContext.getSink(
    path="s3://stedi-lakehouse-us-west-2/customer/trusted/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    enableUpdateCatalog=True,
    transformation_ctx="CustomerTrusted_node3",
)
CustomerTrusted_node3.setCatalogInfo(
    catalogDatabase="stedi", catalogTableName="customer_trusted"
)
CustomerTrusted_node3.setFormat("json")
CustomerTrusted_node3.writeFrame(DropPII_node1682600262207)
job.commit()
