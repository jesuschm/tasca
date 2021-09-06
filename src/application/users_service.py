import logging 
from src.domain.users.user import User

def create_user(repo, username):
    res = False
    logging.debug(f"[+] Creating the user {username}")
    
    user = User(username=username)
    if user:
        res = repo.create_user(user = user.to_dict())
        
    return res

def get_user(repo, username):
    res = repo.get_user(username= username)
    return res