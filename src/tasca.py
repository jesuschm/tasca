import sys
from application.commands_service import post, read, follow, wall
from infra.databases.mongo import MongoRepository

_repo = MongoRepository()
_verbose = False

def main():
    try:
        command = None
        if _repo.client:
            print("[+] Hello friend! Welcome to the Tasca. Get fun! ")
            print("[+] Control + C to exit.\n")
            while command != "^C":
                command = str(input("> "))
                
                # Posting command
                if '->' in command:
                    data = command.split(" -> ")    
                    if len(data) == 2:
                        post(_repo, user = data[0], message = data[1])
                    else:
                        print("[-] Bad post command. Correct format: [username] -> [message].")
                        
                elif 'follows' in command:
                    data = command.split(" follows ")
                    if len(data) == 2:
                        follow(user = data[0], follow = data[1])
                    else:
                        print("[-] Bad follow command. Correct format: [username] -> [username].")
                        
                elif 'wall' in command:
                    data = command.split(" wall")
                    if len(data) == 1:
                        wall(user = data[0])
                    else:
                        print("[-] Bad wall command. Correct format: [username] wall.")
                        
                else:
                    data = command.split(" ")
                    if len(data) == 1:
                        read(user = command)
                    else:
                        print("[-] Bad username to read. Usernames don't contain spaces.")
                        
        else:
            raise("Database not connected.")
    except KeyboardInterrupt:
        print(f"\n[+] Quitting.. Bye!")
        sys.exit(0)
    except Exception as e:
        print(f"[-] Error: {e}. Quitting.")
        sys.exit(1)
    
if __name__ == "__main__":
    """Entry point
    """
    main()