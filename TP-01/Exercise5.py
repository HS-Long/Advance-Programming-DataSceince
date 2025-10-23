from abc import ABC, abstractmethod
from Exercise1 import CSVReader
from Exercise2 import DataCleaner
from Exercise4 import TransformFactory

class DataPipeline(ABC):
    """
    Abstract class that defines the template for a data pipeline.
    Subclasses should implement load(), clean(), transform(), and save().
    """

    def run(this):
        """Template method — defines the pipeline sequence."""
        print("Starting Data Pipeline...\n")
        df = this.load()
        df = this.clean(df)
        df = this.transform(df)
        this.save(df)
        print("\n Data Pipeline completed successfully!")

    @abstractmethod
    def load(this):
        pass

    @abstractmethod
    def clean(this, df):
        pass

    @abstractmethod
    def transform(this, df):
        pass

    @abstractmethod
    def save(this, df):
        pass



import pandas as pd

class CSVDataPipeline(DataPipeline):
    def __init__(this, input_path, output_path, cleaning_strategy, transform_type):
        this.input_path = input_path
        this.output_path = output_path
        this.cleaning_strategy = cleaning_strategy
        this.transform_type = transform_type

    # Load Step (using CSVReader)
    def load(this):
        print(" Loading data...")
        reader = CSVReader(this.input_path)
        reader.read()
        df = pd.read_csv(this.input_path)  # Retrieve data
        print(f" Loaded dataset with shape: {df.shape}")
        return df

    # Clean Step (using DataCleaner + strategy)
    def clean(this, df):
        print("\n Cleaning data using strategy:", this.cleaning_strategy.__class__.__name__)
        cleaner = DataCleaner(this.cleaning_strategy)
        df = cleaner.clean(df)
        print(f" After cleaning: {df.shape} rows remaining")
        return df

    # Transform Step (using TransformFactory)
    def transform(this, df):
        print("\n Applying transformation:", this.transform_type)
        transform = TransformFactory.get_transform(this.transform_type)
        df = transform.apply(df)
        print(f" Transformation complete. Final shape: {df.shape}")
        return df

    # Save Step
    def save(this, df):
        print("\n Saving cleaned data...")
        df.to_csv(this.output_path, index=False)
        print(f" Data saved to {this.output_path}")
