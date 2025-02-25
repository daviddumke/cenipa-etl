from cenipa_etl.extractor import Extractor

class Etl:
    def __init__(self, params):
        self.params = self.is_valid_params(params)
        self.extracted_data = None

        self.extract_data()

    def is_valid_params(self, params):        
        valid_params = ["source", "target", "limit"]
        invalid_params = [p for p in params if p not in valid_params]
        if invalid_params:
            raise ValueError(f"Invalid parameters: {', '.join(invalid_params)}")
        else:
            return params

    def extract_data(self):
        extractor = Extractor(self.params["source"], self.params["limit"])
        self.extracted_data = extractor.extract()
        print(self.extracted_data)
        return self.extracted_data

    def transform_data(self):
        pass

    def load_data(self):
        pass
