import os
import pandas as pd

class Extractor:
    def __init__(self, stream):
        self.source_stream = stream
        self.extracted_data_df = None
        self.limit = os.getenv("CENIPA_SOURCE_LIMIT")
        self.source_format = os.getenv("CENIPA_SOURCE_FORMAT")
        self.source_url_base = os.getenv("CENIPA_SOURCE_URL_BASE")
        self.source_stream = stream

    def extract(self):
        print(f"Extracting data from {self.source_stream}...")
        self.extracted_data_df = pd.read_csv(f'{self.source_url_base}{self.source_stream}.{self.source_format}',
                nrows=int(self.limit),
                sep = ';',
                encoding='latin-1',
                on_bad_lines='skip')

        return self.extracted_data_df
