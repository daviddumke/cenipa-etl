class HelpHandler:

    @staticmethod
    def print_help():
        help_text = """
    ===================== HELP MENU =====================
    Usage: package_name <action> <args>

    Available Actions:
    1. etl <source> <destination> [options]
    - Runs an ETL (Extract, Transform, Load) process.

    Arguments for `etl`:
    - <source>: The data source (e.g., 'csv', 'database', 'api').
    - <destination>: The target destination (e.g., 'bigquery', 'postgres', 'csv').
    - [options]: Optional flags for processing, such as:
        --limit <num>    -> Limit the number of rows processed.
        --filter <key=value> -> Apply filtering on the extracted data.
        --format <type>  -> Specify output format (e.g., 'json', 'parquet').

    Example:
    package_name etl csv bigquery --limit 1000 --filter "status=active"

    Additional Notes:
    - Ensure dependencies are installed: `pip install package_name`
    - Supported sources: CSV, JSON, APIs, PostgreSQL, MySQL, BigQuery.
    - Supported destinations: PostgreSQL, BigQuery, CSV, Parquet.

    =====================================================
        """
        print(help_text)
