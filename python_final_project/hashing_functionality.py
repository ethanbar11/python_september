import hashlib
def signup(username,password):
    password_hash=str(hashlib.sha1(password.encode()).hexdigest())

    print(password_hash)
    ## Enter hash + username to DB
    insert_user_plus_hash_to_db(username,password_hash)

signup('hello','bla')

def signin(username,password):
    password_hash=hashlib.sha1(password)
    # Select username and hash from DB
    hash_to_check=get_hash_from_db(username)
    # if password_hash==hash_to_check:
    #     User can login
    # else:
    #     User can't login