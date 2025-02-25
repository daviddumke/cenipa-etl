import pandas as pd


class Extractor:
    def __init__(self, filename, limit = None):
        self.filename = filename
        self.limit = limit
        self.extracted_data_df = None

    def extract(self):

        self.extracted_data_df = pd.read_csv(f'https://dedalo.sti.fab.mil.br/dadosabertos/{self.filename}.csv',
                nrows=int(self.limit),
                sep = ';',
                encoding='latin-1',
                on_bad_lines='skip')

        return self.extracted_data_df