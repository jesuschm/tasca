import argparse
from src.application.users_service import create_user

def main():
    """Main function
    """
    try:
        # Initiate the parser
        parser = argparse.ArgumentParser()

        # Add long and short argument
        parser.add_argument("user", help="Tasca username")

        # Read arguments from the command line
        args = parser.parse_args()
        create_user(args.user)
        
    except Exception as err:
        print("[-] Unexpected error: {}".format(err))
    
if __name__ == "__main__":
    """Entry point
    """
    main()