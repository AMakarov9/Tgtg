from tgtg import TgtgClient

def get_tokens(emaila: str): 

    # Create the client based on the tgtg API. 
    # Tokens are always new for each session. 

    client = TgtgClient(email = emaila)
    credentials = client.get_credentials()
    tokens = []
    for i in credentials: 
        if i in ["access_token", "refresh_token", "user_id", "cookie"]: 
            tokens.append(credentials[i])

    client = TgtgClient(access_token=tokens[0], refresh_token=tokens[1], user_id=tokens[2], cookie=tokens[3])
    return client