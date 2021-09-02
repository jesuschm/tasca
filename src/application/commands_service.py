from src.domain.messages.message import Message

def post(repo, user: str, message: str):
    res = True
    print(f"[+] {user} user is posting: {message}.")
    
    # TODO: Get user
    message = Message(content = message, user_id = 1)
    res = repo.insert_message(message= message.to_dict())
    return res

def read(repo, user: str):
    res = None
    print(f"[+] Reading {user}'s timeline")
    
    # TODO: Get user from db or insert it
    res = repo.get_messages(user_id = user.id)
    return res

def follow(user: str, follow: str):
    rc = False
    print(f"[+] User {user} is following user {follow}.")
    
    # TODO: 
    # 1. Get the user
    # 2. Get the follow user
    # 3. Update the user follow list with the follow user id
    # 4. Upsert the user
    
    return rc

def wall(user: str):
    rc = True
    print(f"[+] Reading user {user} wall.")
    
    # TODO: 
    # 1. Get the user
    # 2. Get all the follow users
    # 4. Get all messages posted by all the users id
    return rc