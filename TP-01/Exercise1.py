# import library
import pandas as pd

class CSVReader:
    def __init__(this, file_path):
        """
        Initialize the CSVReader with the path to the CSV file.
        
        Parameters:
        file_path (str): The path to the CSV file.
        """
        this.__file_path = file_path   # Private attribute for encapsulation
        this.__data = None             

    def read(this):
        """
        Reads the CSV file and stores it in the __data attribute.
        """
        try:
            this.__data = pd.read_csv(this.__file_path)
            print("CSV file loaded successfully.")
        except FileNotFoundError:
            print("Error: File not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def preview(this, n=5):
        """
        Displays the first n rows of the loaded CSV data.
        
        Parameters:
        n (int): Number of rows to display (default = 5)
        """
        if this.__data is not None:
            print(this.__data.head(n))
        else:
            print("Please load the CSV file first using the read() method.")

