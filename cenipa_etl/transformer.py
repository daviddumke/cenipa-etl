import pandas as pd


class Transformer:
    def __init__(self, data):
        self.extracted_data_df = data
        self.transformed_data_df = None

    def transform(self):
        self.transformed_data_df = self.extracted_data_df.replace('***', None)
        return self.transformed_data_df
