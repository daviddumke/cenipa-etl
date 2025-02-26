import os
import pandas as pd
from google.cloud import bigquery

class Loader:
    def __init__(self, stream, data):
        self.transformed_data_df = data
        # Define your dataset and table
        self.prefix = os.getenv("CENIPA_SOURCE_NAME")
        self.project_id = os.getenv("CENIPA_TARGET_PROJECT")
        self.dataset_id = os.getenv("CENIPA_TARGET_DATASET")
        self.table_id = self.prefix + "_" + stream

    def load(self):
        # Define the full table path
        table_ref = f"{self.project_id}.{self.dataset_id}.{self.table_id}"
        # Initialize the BigQuery client
        client = bigquery.Client(project=self.project_id)

        # Load the DataFrame into BigQuery
        job = client.load_table_from_dataframe(self.transformed_data_df, table_ref)

        job_config = bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE")

        # Wait for the job to complete
        job.result()

        print(f"DataFrame uploaded to {table_ref} successfully!")
        return self.transformed_data_df
