from cenipa_etl.helper import HelpHandler
from cenipa_etl.etl import Etl

class Run:
    def __init__(self, action, params): # Instance of HelpHandler        
        self.params = params

        actions = {
            "help": self.print_help,
            "etl": self.etl
        }

        # Get the function from the dictionary, defaulting to an error handler
        action_function = actions.get(action, self.invalid_action)

        # Call the selected function
        action_function()

    def invalid_action(self):
        print("Error: Invalid action. Use 'help' for available options.")

    def print_help(self):
        help_text = HelpHandler() 
        help_text.print_help()

    def etl(self):
        etl = Etl(self.params)
        return etl
