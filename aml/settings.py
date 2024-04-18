import os

from dotenv import load_dotenv

# Import dotenv and load environment variables from file
load_dotenv(".env")

# Workspace
SUBSCRIPTION_ID = os.getenv("SUBSCRIPTION_ID")
RESOURCE_GROUP = os.getenv("RESOURCE_GROUP")
WORKSPACE_NAME = os.getenv("WORKSPACE_NAME")

# Compute
COMPUTE_NAME = os.getenv("COMPUTE_NAME")
COMPUTE_TYPE = os.getenv("COMPUTE_TYPE")
COMPUTE_MIN_INSTANCES = os.getenv("COMPUTE_MIN_INSTANCES")
COMPUTE_MAX_INSTANCES = os.getenv("COMPUTE_MAX_INSTANCES")
COMPUTE_SIZE = os.getenv("COMPUTE_SIZE")
COMPUTE_IDLE_TIME = os.getenv("COMPUTE_IDLE_TIME")
COMPUTE_TIER = os.getenv("COMPUTE_TIER")

# Data
DATA_NAME = os.getenv("DATA_NAME")
DATA_DESCRIPTION = os.getenv("DATA_DESCRIPTION")
DATA_VERSION = os.getenv("DATA_VERSION")
DATA_PATH = os.getenv("DATA_PATH")

# Environment
ENVIRONMENT_NAME = os.getenv("ENVIRONMENT_NAME")
ENVIRONMENT_DESCRIPTION = os.getenv("ENVIRONMENT_DESCRIPTION")
ENVIRONMENT_YAML = os.getenv("ENVIRONMENT_YAML")
ENVIRONMENT_IMAGE = os.getenv("ENVIRONMENT_IMAGE")

# Experiment
EXPERIMENT_NAME = os.getenv("EXPERIMENT_NAME")
EXPERIMENT_DISPLAY_NAME = os.getenv("EXPERIMENT_DISPLAY_NAME")

# Model
MODEL_NAME = os.getenv("MODEL_NAME")

# Job
JOB_TEST_TRAIN_RATIO = os.getenv("JOB_TEST_TRAIN_RATIO")
JOB_LEARNING_RATE = os.getenv("JOB_LEARNING_RATE")
