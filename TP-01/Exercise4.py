from abc import ABC, abstractmethod
import pandas as pd

class DataTransform(ABC):
    @abstractmethod
    def apply(this, df: pd.DataFrame) -> pd.DataFrame:
        """Apply a transformation to the given DataFrame."""
        pass
    
# NormalizeColumns — scale numeric columns between 0 and 1
class NormalizeColumns(DataTransform):
    def apply(this, df: pd.DataFrame) -> pd.DataFrame:
        print(" Normalizing numeric columns...")
        numeric_cols = df.select_dtypes(include=["number"]).columns
        df[numeric_cols] = (df[numeric_cols] - df[numeric_cols].min()) / (df[numeric_cols].max() - df[numeric_cols].min())
        return df


class RemoveDuplicates(DataTransform):
    def apply(this, df: pd.DataFrame) -> pd.DataFrame:
        print(" Removing duplicate rows...")
        return df.drop_duplicates()


# StandardizeText — convert all text columns to lowercase
class StandardizeText(DataTransform):
    def apply(this, df: pd.DataFrame) -> pd.DataFrame:
        print(" Standardizing text columns to lowercase...")
        text_cols = df.select_dtypes(include=["object"]).columns
        for col in text_cols:
            df[col] = df[col].str.lower()
        return df


class TransformFactory:
    """
    Factory class that returns a transformation object based on input string.
    """
    @staticmethod
    def get_transform(transform_type: str) -> DataTransform:
        transform_type = transform_type.lower()
        
        if transform_type == "normalize":
            return NormalizeColumns()
        elif transform_type == "remove_duplicates":
            return RemoveDuplicates()
        elif transform_type == "standardize_text":
            return StandardizeText()
        else:
            raise ValueError(f" Unknown transformation type: {transform_type}")

