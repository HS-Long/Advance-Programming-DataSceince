# main.py
import pandas as pd
import logging
from config import (
    CSV_FILE_PATH, 
    OUTPUT_FILE_PATH, 
    LOG_FILE_PATH,
    ADULT_AGE_THRESHOLD,
    ENCODING,
    DATE_FORMAT,
    LOG_LEVEL,
    LOG_FORMAT
)

def setup_logging():
    """Configure logging using constants from config"""
    logging.basicConfig(
        level=LOG_LEVEL,
        format=LOG_FORMAT,
        handlers=[
            logging.FileHandler(LOG_FILE_PATH),
            logging.StreamHandler()
        ]
    )

def load_employee_data():
    """Load employee data from CSV file using configured path"""
    try:
        logging.info(f"Loading employee data from {CSV_FILE_PATH}")
        df = pd.read_csv(CSV_FILE_PATH, encoding=ENCODING)
        logging.info(f"Successfully loaded {len(df)} employee records")
        return df
    except FileNotFoundError:
        logging.error(f"CSV file not found at {CSV_FILE_PATH}")
        return None
    except Exception as e:
        logging.error(f"Error loading CSV file: {e}")
        return None

def filter_adult_employees(df):
    """Filter employees who are adults using configured threshold"""
    if df is None:
        return None
    
    adult_employees = df[df['age'] >= ADULT_AGE_THRESHOLD]
    logging.info(f"Found {len(adult_employees)} adult employees (age >= {ADULT_AGE_THRESHOLD})")
    return adult_employees

def save_adult_employees(df):
    """Save adult employees to output file using configured path"""
    if df is None or df.empty:
        logging.warning("No adult employees to save")
        return False
    
    try:
        df.to_csv(OUTPUT_FILE_PATH, index=False, encoding=ENCODING)
        logging.info(f"Adult employees saved to {OUTPUT_FILE_PATH}")
        return True
    except Exception as e:
        logging.error(f"Error saving to {OUTPUT_FILE_PATH}: {e}")
        return False

def calculate_average_age(df):
    """Calculate average age of employees"""
    if df is None or df.empty:
        return 0
    return df['age'].mean()

def display_employee_summary(df):
    """Display a summary of employee data"""
    if df is None:
        return
    
    total_employees = len(df)
    adult_count = len(df[df['age'] >= ADULT_AGE_THRESHOLD])
    minor_count = len(df[df['age'] < ADULT_AGE_THRESHOLD])
    avg_age = df['age'].mean()
    
    print("\n=== EMPLOYEE SUMMARY ===")
    print(f"Total employees: {total_employees}")
    print(f"Adult employees (≥{ADULT_AGE_THRESHOLD}): {adult_count}")
    print(f"Minor employees: {minor_count}")
    print(f"Average age: {avg_age:.1f} years")
    print(f"Departments: {', '.join(df['department'].unique())}")

def main():
    """Main function to process employee data"""
    setup_logging()
    
    print("Starting employee data processing...")
    
    # Load data
    employees_df = load_employee_data()
    
    if employees_df is not None:
        # Display original data summary
        display_employee_summary(employees_df)
        
        # Filter adult employees
        adult_employees = filter_adult_employees(employees_df)
        
        # Save results
        if adult_employees is not None:
            save_success = save_adult_employees(adult_employees)
            
            if save_success:
                print(f"\nAdult employees saved to: {OUTPUT_FILE_PATH}")
                print(f"Log file created at: {LOG_FILE_PATH}")
                
                # Display adult employees summary
                print("\n=== ADULT EMPLOYEES ===")
                print(adult_employees[['name', 'age', 'department']].to_string(index=False))

if __name__ == "__main__":
    main()