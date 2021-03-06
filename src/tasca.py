import sys
import logging
from application.commands_service import post, read, follow, wall
from infra.databases.mongo import MongoRepository

_repo = MongoRepository()
_verbose = False

def main():
    try:
        command = None
        if _repo.client:
            logging.info("[+] Hello friend! Welcome to the Tasca. Get fun! ")
            logging.info("[+] Control + C to exit.\n")
            
            while command != "^C":
                try:
                    command = str(input("> "))
                    
                    # Posting command
                    if '->' in command:
                        data = command.split(" -> ")    
                        if len(data) == 2:
                            post(_repo, username = data[0], message = data[1])
                        else:
                            logging.error("[-] Bad post command. Correct format: [username] -> [message].")
                            
                    elif 'follows' in command:
                        data = command.split(" follows ")
                        if len(data) == 2:
                            user = data[0]
                            follow_user = data[1]
                            
                            rc = follow(_repo, username = user, follow_username = follow_user)
                            if rc:
                                logging.debug(f"[+] {user} is now following {follow_user}.")
                            else:
                                logging.error(f"[-] Error trying to follow {follow_user}")
                        else:
                            logging.error("[-] Bad follow command. Correct format: [username] -> [username].")
                            
                    elif 'wall' in command:
                        data = command.split(" wall")
                        if len(data) == 2 and data[1] == '':
                            wall(_repo, username = data[0])
                        else:
                            logging.error("[-] Bad wall command. Correct format: [username] wall.")
                            
                    else:
                        data = command.split(" ")
                        if len(data) == 1:
                            read(_repo, username = command)
                        else:
                            logging.error("[-] Bad username to read. Usernames don't contain spaces.")
                except Exception as e:
                    logging.error(f"[-] Error: {e}.")
        else:
            raise("Database not connected.")
    except KeyboardInterrupt:
        logging.info(f"\n[+] Quitting.. Bye!")
        sys.exit(0)
    except Exception as e:
        logging.error(f"[-] Error: {e}. Quitting.")
        sys.exit(1)
    
if __name__ == "__main__":
    """Entry point
    """
    main()