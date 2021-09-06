import logging
from src.domain.messages.message import Message
from src.domain.users.user import User
from src.domain.messages.message import Message

def post(repo, username: str, message: str):
    res = False
    logging.debug(f"[+] {username} user is posting: {message}.")
    
    user = User.from_dict(repo.get_user(username = username))
    if user:
        message = Message(content = message, user_id = user.id)
        res = repo.insert_message(message= message.to_dict())
    else:
        raise Exception(f"{username} user not found")
        
    return res

def read(repo, username: str):
    res = None
    logging.debug(f"[+] Reading {username}'s timeline")
    
    user = User.from_dict(repo.get_user(username = username))
    if user:
        res = repo.get_messages(user_ids = [user.id])
        username = {
            user.id: user.username
        }
        
        Message.print_messages(messages = res, usernames = username)
    else:
        raise Exception(f"{username} user not found")
    
    return res

def follow(repo, username: str, follow_username: str):
    res = False
    logging.debug(f"[+] User {username} wants to follow user {follow_username}.")
    
    user = User.from_dict(repo.get_user(username = username))
    follow_user = User.from_dict(repo.get_user(username = follow_username))
    if user:
        if follow_user:
            user.add_follow(follow_user.id)
            res = repo.update_user(user = user.to_dict())
        else:
            raise Exception(f"{follow_username} user to follow not found")
    else:
        raise Exception(f"{username} user not found")
            
    return res

def wall(repo, username: str):
    res = None
    logging.debug(f"[+] Reading user {username} wall.")
    
    user = User.from_dict(repo.get_user(username = username))
    if user:
        ids = [user.id]
        # Username is a dict key-value (id-username)
        usernames = {
            user.id: user.username
        }
        
        if user.follows and isinstance(user.follows, list):
            ids.extend(user.follows)
            for f in user.follows:
                usernames.update({
                    f: repo.get_user_by_id(f).get('username')
                })
        
        res = repo.get_messages(user_ids = ids)
        Message.print_messages(messages = res, usernames = usernames)
    else:
        raise Exception(f"{username} user not found")
        
    return res