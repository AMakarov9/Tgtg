from tgtg import TgtgClient

def get_tokens(emaila: str): 

    # Create the client based on the tgtg API. 
    # Tokens are always new for each session. 

    client = TgtgClient(email = emaila)
    credentials = client.get_credentials()
    client = TgtgClient(access_token=credentials["access_token"], refresh_token=credentials["refresh_token"], user_id=credentials["user_id"], cookie=credentials["datadome_cookie"])
    return client