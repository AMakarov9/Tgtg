from tgtg import TgtgClient
from get_client import get_tokens 
from time import gmtime, strftime
from time import sleep
import tgtg

def get_available_items(client: TgtgClient, utSkrevet: list):
    print("get_available items is running...")
    tid = strftime("%H:%M", gmtime())
    items = client.get_items()
    ute = []

    # Items is set to collection of Toogoodtogo stores in JSON-format.
    # Items with a length more than 12 are either avaliable, sold out or something else. 
    for i in items: 
        if len(i) > 12: 
            ute.append(i)
    if len(ute) == 0: 
        return False
    else: 
        # In items_available is over 0, the item is available. 
        # I also pass in a list as argument for the function to only return items that havent been returned yet. 
        # I add to this list in telegram.py. 
        for i in ute: 
            if i['in_sales_window'] and i['items_available'] > 0 and i['store']['store_name'] not in utSkrevet: 
                navn = i['store']['store_name']
                dag = strftime("%A")
                tid = strftime("%H:%M:%S", gmtime())

                # Return the name that will be used to check if a store has been printed. 
                return f"{navn}, {i['items_available']}, {tid}, {dag}"



def run(client, utSkrevet):
    try:
        return get_available_items(client, utSkrevet=utSkrevet)

    except tgtg.exceptions.TgtgLoginError as e:

        print("Feil ved innlogging: Kontroller at e-postadressen er korrekt.")
        return 
    
