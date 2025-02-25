import pandas as pd
from google.cloud import bigquery

class Loader:
    def __init__(self, data):
        self.transformed_data_df = data
        print(self.transformed_data_df)

    def load(self):
        # Define your dataset and table
        project_id = "cenipa"
        dataset_id = "data_lake"
        table_id = "aeronaves"

        # Define the full table path
        table_ref = f"{project_id}.{dataset_id}.{table_id}"
        # Initialize the BigQuery client
        client = bigquery.Client()

        # Load the DataFrame into BigQuery
        job = client.load_table_from_dataframe(self.transformed_data_df, table_ref)

        job_config = bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE")

        # Wait for the job to complete
        job.result()

        print(f"DataFrame uploaded to {table_ref} successfully!")
        return self.transformed_data_df
