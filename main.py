import sys
from cenipa_etl.run import Run

def parse_args():
    action = sys.argv[1]
    args = sys.argv[2:]  # Exclude script name
    arg_dict = {}  # Initialize dictionary with script name

    # Loop through arguments with index
    for i, arg in enumerate(args):
        if arg.startswith("--"):  # Argument name (e.g., --source)
            key = arg[2:]  # Remove "--"
            if i + 1 < len(args) and not args[i + 1].startswith("--"):  # Check if there's a value
                arg_dict[key] = args[i + 1]
            else:
                arg_dict[key] = True  # Handle flags (e.g., --verbose)

    return action, arg_dict

def main():
    action, params = parse_args() # Get parameters
    running = Run(action, params)

if __name__ == "__main__":
    main()
