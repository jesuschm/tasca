def create_user(repo, username):
    print(f"[+] Creating the user {username}")
    res = repo.create_user(username)
    return res