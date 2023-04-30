import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

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

# Script generated for node Renamed keys for Join
RenamedkeysforJoin_node1682789140659 = ApplyMapping.apply(
    frame=AccelerometerTrusted_node1682584724137,
    mappings=[
        ("serialnumber", "string", "`(accelerometer) serialnumber`", "string"),
        ("z", "double", "`(accelerometer) z`", "double"),
        (
            "sharewithpublicasofdate",
            "long",
            "`(accelerometer) sharewithpublicasofdate`",
            "long",
        ),
        ("timestamp", "long", "`(accelerometer) timestamp`", "long"),
        (
            "sharewithresearchasofdate",
            "long",
            "`(accelerometer) sharewithresearchasofdate`",
            "long",
        ),
        ("registrationdate", "long", "`(accelerometer) registrationdate`", "long"),
        (
            "sharewithfriendsasofdate",
            "long",
            "`(accelerometer) sharewithfriendsasofdate`",
            "long",
        ),
        ("user", "string", "`(accelerometer) user`", "string"),
        ("y", "double", "`(accelerometer) y`", "double"),
        ("x", "double", "`(accelerometer) x`", "double"),
        ("lastupdatedate", "long", "`(accelerometer) lastupdatedate`", "long"),
    ],
    transformation_ctx="RenamedkeysforJoin_node1682789140659",
)

# Script generated for node Join
Join_node2 = Join.apply(
    frame1=CustomerTrusted_node1682584556895,
    frame2=RenamedkeysforJoin_node1682789140659,
    keys1=["email"],
    keys2=["`(accelerometer) user`"],
    transformation_ctx="Join_node2",
)

# Script generated for node Drop Fields
DropFields_node1682577647921 = DropFields.apply(
    frame=Join_node2,
    paths=[
        "email",
        "`(accelerometer) lastupdatedate`",
        "`(accelerometer) serialnumber`",
        "`(accelerometer) z`",
        "`(accelerometer) sharewithpublicasofdate`",
        "`(accelerometer) timestamp`",
        "`(accelerometer) sharewithresearchasofdate`",
        "`(accelerometer) registrationdate`",
        "`(accelerometer) sharewithfriendsasofdate`",
        "`(accelerometer) user`",
        "`(accelerometer) y`",
        "`(accelerometer) x`",
    ],
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
