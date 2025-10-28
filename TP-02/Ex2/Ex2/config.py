# config.py

# File paths
CSV_FILE_PATH = "employees.csv"
OUTPUT_FILE_PATH = "adult_employees.csv"
LOG_FILE_PATH = "employee_processing.log"

# Age threshold
ADULT_AGE_THRESHOLD = 18

# Data processing constants
ENCODING = "utf-8"
DATE_FORMAT = "%Y-%m-%d"

# Validation constants
MIN_AGE = 0
MAX_AGE = 120
VALID_DEPARTMENTS = ["HR", "Engineering", "Marketing", "Sales", "Finance"]

# Logging configuration
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"