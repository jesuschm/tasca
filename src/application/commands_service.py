from src.domain.messages.message import Message
from src.domain.users.user import User

def post(repo, user: str, message: str):
    res = False
    print(f"[+] {user} user is posting: {message}.")
    
    user = repo.get_user(username = user)
    if user:
        message = Message(content = message, user_id = user.id)
        res = repo.insert_message(message= message.to_dict())
        
    return res

def read(repo, user: str):
    res = None
    print(f"[+] Reading {user}'s timeline")
    
    user = repo.get_user(username = user)
    if user:
        res = repo.get_messages(user_ids = [user.id])
        # TODO: print messages
        
    return res

def follow(repo, user: str, follow: str):
    res = False
    print(f"[+] User {user} is following user {follow}.")
    
    user = repo.get_user(username = user)
    follow_user = repo.get_user(username = follow)
    if user and follow_user:
        rc = user.add_follow(follow_user)
        if rc:
            res = repo.update_user(user = user.to_dict())
            
    return res

def wall(repo, user: str):
    res = None
    print(f"[+] Reading user {user} wall.")
    
    user = repo.get_user(username = user)
    if user:
        ids = [user.id]
        ids.extend(user.follows)
        
        res = repo.get_messages(user_ids = ids)
        # TODO: print messages
        
    return res