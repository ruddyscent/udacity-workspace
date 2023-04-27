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

# Script generated for node Step Trainer Landing
StepTrainerLanding_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://stedi-lakehouse-us-west-2/step_trainer/landing/"],
        "recurse": True,
    },
    transformation_ctx="StepTrainerLanding_node1",
)

# Script generated for node Customer Curated
CustomerCurated_node1682588034460 = glueContext.create_dynamic_frame.from_catalog(
    database="stedi",
    table_name="customer_curated",
    transformation_ctx="CustomerCurated_node1682588034460",
)

# Script generated for node Join
StepTrainerLanding_node1DF = StepTrainerLanding_node1.toDF()
CustomerCurated_node1682588034460DF = CustomerCurated_node1682588034460.toDF()
Join_node2 = DynamicFrame.fromDF(
    StepTrainerLanding_node1DF.join(
        CustomerCurated_node1682588034460DF,
        (
            StepTrainerLanding_node1DF["serialNumber"]
            == CustomerCurated_node1682588034460DF["serialnumber"]
        ),
        "leftsemi",
    ),
    glueContext,
    "Join_node2",
)

# Script generated for node Drop Fields
DropFields_node1682578792205 = DropFields.apply(
    frame=Join_node2,
    paths=[
        "serialnumber",
        "sharewithfriendsasofdate",
        "sharewithpublicasofdate",
        "registrationdate",
        "sharewithresearchasofdate",
        "email",
        "lastupdatedate",
    ],
    transformation_ctx="DropFields_node1682578792205",
)

# Script generated for node Step Trainer Trusted
StepTrainerTrusted_node3 = glueContext.getSink(
    path="s3://stedi-lakehouse-us-west-2/step_trainer/trusted/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    enableUpdateCatalog=True,
    transformation_ctx="StepTrainerTrusted_node3",
)
StepTrainerTrusted_node3.setCatalogInfo(
    catalogDatabase="stedi", catalogTableName="step_trainer_trusted"
)
StepTrainerTrusted_node3.setFormat("json")
StepTrainerTrusted_node3.writeFrame(DropFields_node1682578792205)
job.commit()
