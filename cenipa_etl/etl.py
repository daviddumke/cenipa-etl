from cenipa_etl.extractor import Extractor
from cenipa_etl.loader import Loader
from cenipa_etl.transformer import Transformer

class Etl:
    def __init__(self, params):
        self.params = self.is_valid_params(params)
        self.extracted_data = None
        self.transformed_data = None
        self.sent_data = None

        self.extract_data()
        self.transform_data()
        self.load_data()

    def is_valid_params(self, params): 
        required_params = ["source", "target"]
        valid_params = required_params + ["limit"]
        invalid_params = [p for p in params if p not in valid_params]
        missing_params = set(required_params) - set(params)

        if invalid_params:
            raise ValueError(f"Invalid parameters: {', '.join(invalid_params)}")
        if missing_params:
            raise ValueError(f"Missing required parameters: {', '.join(missing_params)}")
        else:
            return params

    def extract_data(self):
        extractor = Extractor(self.params["source"], self.params["limit"])
        self.extracted_data = extractor.extract()
        return self.extracted_data

    def transform_data(self):
        transformer = Transformer(self.extracted_data)
        self.transformed_data = transformer.transform()
        return self.transformed_data

    def load_data(self):
        loader = Loader(self.transformed_data)
        self.sent_data = loader.load()
        print(self.sent_data)
