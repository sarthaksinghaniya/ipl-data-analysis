import pandas as pd
import os
from typing import Tuple


class DataLoader:
    """Handles loading and initial data validation for IPL datasets."""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self.matches = None
        self.deliveries = None
    
    def load_data(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """Load matches and deliveries datasets."""
        matches_path = os.path.join(self.data_dir, "matches.csv")
        deliveries_path = os.path.join(self.data_dir, "deliveries.csv")
        
        self.matches = pd.read_csv(matches_path)
        self.deliveries = pd.read_csv(deliveries_path)
        
        return self.matches, self.deliveries
    
    def get_data_info(self) -> dict:
        """Get basic information about the datasets."""
        if self.matches is None or self.deliveries is None:
            self.load_data()
        
        return {
            'matches_shape': self.matches.shape,
            'deliveries_shape': self.deliveries.shape,
            'matches_nulls': self.matches.isnull().sum().to_dict(),
            'deliveries_nulls': self.deliveries.isnull().sum().to_dict()
        }
    
    def get_sample_data(self, n: int = 5) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """Get sample data from both datasets."""
        if self.matches is None or self.deliveries is None:
            self.load_data()
        
        return self.matches.head(n), self.deliveries.head(n)
