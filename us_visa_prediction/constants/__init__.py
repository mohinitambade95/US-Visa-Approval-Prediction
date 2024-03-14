import os
from datetime import date

DATABASE_NAME = "US_VISA"
COLLECTION_NAME = "VISA_DATA"

MONGODB_URL_KEY = "mongodb+srv://mohinitambade95:Mona1234@cluster0.gjdgjvq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

PIPELINE_NAME: str = "usvisa"
ARTIFACT_DIR : str = "artifact"

MODEL_FILE_NAME = "model.pkl"

TARGET_COLUMN = "case_status"
CURRENT_YEAR = date.today().year
PREPROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"

FILE_NAME: str = "usvisa.csv"
TRAIN_FILE_NAME : str = "train.csv"
TEST_FILE_NAME : str =  "test.csv"

"""
Data ingestion related constants starts with DATA_INGESTION var name

"""
DATA_INGESTION_COLLECTION_NAME :str = "VISA_DATA"
DATA_INGESTION_DIR_NAME :str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR :str = "feature_store"
DATA_INGESTION_INGESTED_DIR :str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO : float = 0.2


"""
Data Validation realted contant start with DATA_VALIDATION VAR NAME
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"