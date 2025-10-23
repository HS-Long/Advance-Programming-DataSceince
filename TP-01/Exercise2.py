import pandas as pd
from abc import ABC, abstractmethod

# Abstract Strategy Class
class MissingValueStrategy(ABC):
    @abstractmethod
    def handle(this, df: pd.DataFrame) -> pd.DataFrame:
        """Handle missing values in the given DataFrame."""
        pass

class DropMissing(MissingValueStrategy):
    def handle(this, df: pd.DataFrame) -> pd.DataFrame:
        print(" Dropping rows with missing values...")
        return df.dropna()


class FillMean(MissingValueStrategy):
    def handle(this, df: pd.DataFrame) -> pd.DataFrame:
        print(" Filling missing numeric values with column mean...")
        return df.fillna(df.mean(numeric_only=True))


class FillMode(MissingValueStrategy):
    def handle(this, df: pd.DataFrame) -> pd.DataFrame:
        print(" Filling missing values with column mode...")
        for col in df.columns:
            mode_val = df[col].mode()
            if not mode_val.empty:
                df[col].fillna(mode_val[0], inplace=True)
        return df


class DataCleaner:
    def __init__(this, strategy: MissingValueStrategy):
        """
        Initialize DataCleaner with a specific missing value handling strategy.
        """
        this._strategy = strategy

    def set_strategy(this, strategy: MissingValueStrategy):
        """
        Change the missing value handling strategy at runtime.
        """
        print(f" Strategy changed to {strategy.__class__.__name__}")
        this._strategy = strategy

    def clean(this, df: pd.DataFrame) -> pd.DataFrame:
        """
        Apply the chosen strategy to handle missing values.
        """
        return this._strategy.handle(df)
