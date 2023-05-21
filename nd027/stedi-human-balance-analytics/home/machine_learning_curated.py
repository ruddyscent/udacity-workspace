import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
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

# Script generated for node Step Trainer Trusted
StepTrainerTrusted_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="stedi",
    table_name="step_trainer_trusted",
    transformation_ctx="StepTrainerTrusted_node1",
)

# Script generated for node Accelerometer Trusted
AccelerometerTrusted_node1682824927371 = glueContext.create_dynamic_frame.from_catalog(
    database="stedi",
    table_name="accelerometer_trusted",
    transformation_ctx="AccelerometerTrusted_node1682824927371",
)

# Script generated for node Join
StepTrainerTrusted_node1DF = StepTrainerTrusted_node1.toDF()
AccelerometerTrusted_node1682824927371DF = AccelerometerTrusted_node1682824927371.toDF()
Join_node2 = DynamicFrame.fromDF(
    StepTrainerTrusted_node1DF.join(
        AccelerometerTrusted_node1682824927371DF,
        (
            StepTrainerTrusted_node1DF["sensorreadingtime"]
            == AccelerometerTrusted_node1682824927371DF["timestamp"]
        ),
        "outer",
    ),
    glueContext,
    "Join_node2",
)

# Script generated for node SQL Query
SqlQuery0 = """
select * from myDataSource
where sensorreadingtime is not null 
and timestamp is not null
"""
SQLQuery_node1682833505543 = sparkSqlQuery(
    glueContext,
    query=SqlQuery0,
    mapping={"myDataSource": Join_node2},
    transformation_ctx="SQLQuery_node1682833505543",
)

# Script generated for node Drop Fields
DropFields_node1682793491334 = DropFields.apply(
    frame=SQLQuery_node1682833505543,
    paths=["user"],
    transformation_ctx="DropFields_node1682793491334",
)

# Script generated for node Machine Learning Curated
MachineLearningCurated_node3 = glueContext.getSink(
    path="s3://stedi-lakehouse-us-west-2/machine_learning/curated/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    enableUpdateCatalog=True,
    transformation_ctx="MachineLearningCurated_node3",
)
MachineLearningCurated_node3.setCatalogInfo(
    catalogDatabase="stedi", catalogTableName="machine_learning_curated"
)
MachineLearningCurated_node3.setFormat("json")
MachineLearningCurated_node3.writeFrame(DropFields_node1682793491334)
job.commit()
