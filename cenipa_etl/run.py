import sys
from cenipa_etl.helper import HelpHandler
from cenipa_etl.etl import Etl

class Run:
    def __init__(self):
        self.action, self.params = self.parse_args() # Get parameters

        valid_actions = {
            "help": self.print_help,
            "etl": self.etl
        }

        # Get the function from the dictionary, defaulting to an error handler
        action_function = valid_actions.get(self.action, self.invalid_action)

        # Call the selected function
        action_function()

    def parse_args(self):
        action = sys.argv[2]
        args = sys.argv[3:]  # Exclude script name
        arg_dict = {}  # Initialize dictionary with script name

        # Loop through arguments with index
        for i, arg in enumerate(args):
            if arg.startswith("--"):  # Argument name (e.g., --source)
                key = arg[2:]  # Remove "--"
                if i + 1 < len(args) and not args[i + 1].startswith("--"):
                    arg_dict[key] = args[i + 1]
                else:
                    arg_dict[key] = True  # Handle flags (e.g., --verbose)

        return action, arg_dict

    def invalid_action(self):
        print("Error: Invalid action. Use 'help' for available options.")

    def print_help(self):
        help_text = HelpHandler()
        help_text.print_help()

    def etl(self):
        etl = Etl(self.params)
        etl.run_etl()
        return etl
