
from tgtg import TgtgClient
#from get_tokens import get_tokens 
from time import gmtime, strftime

from butikker import Butikk


butikker = {}
#client = get_tokens(email)
def get_items(email: str, client: TgtgClient):
    
    #items = client.get_items()
    items = [
    {'item': {'item_id': '15441', 'sales_taxes': [{'tax_description': 'VAT', 'tax_percentage': 15.0}], 'tax_amount': {'code': 'NOK', 'minor_units': 1030, 'decimals': 2}, 'price_excluding_taxes': {'code': 'NOK', 'minor_units': 7900, 'decimals': 2}, 'price_including_taxes': {'code': 'NOK', 'minor_units': 7900, 'decimals': 2}, 'value_excluding_taxes': {'code': 'NOK', 'minor_units': 0, 'decimals': 2}, 'value_including_taxes': 
    {'code': 'NOK', 'minor_units': 0, 'decimals': 2}, 'taxation_policy': 'PRICE_INCLUDES_TAXES', 
    'show_sales_taxes': False, 'item_price': {'code': 'NOK', 'minor_units': 7900, 'decimals': 2}, 
    'item_value': {'code': 'NOK', 'minor_units': 0, 'decimals': 2}, 'cover_picture': {'picture_id': '29837', 
    'current_url': 'https://images.tgtg.ninja/store/1489165215_7Cb3jSuXOl_scale.jpg', 
    'is_automatically_created': False}, 'logo_picture': {'picture_id': '29836', 
    'current_url': 'https://images.tgtg.ninja/store/1489165215_HHCAWi70Rd_scale.jpg', 
    'is_automatically_created': False}, 'name': 'Middag', 
    'description': 'Redd en forundringsporsjon med deilig overskuddsmat fra Jaipur, og bli med i kampen mot matsvinn! \n\nInnholdet vil variere, og kan for eksempel være retter med kylling, lam, biff, scampi, fisk og/eller grønnsaker/vegetar - eller en miks av disse. Ris følger alltid med. Alle rettene er glutenfrie, og inneholder melkeprodukter og cashewnøtter (ingen peanøtter eller egg).\n\nOBS: Vi tilbyr ikke bestikk og pose - dette må tas med hjemmefra :-)\n\nBestill og betal via appen, hent til angitt hentetidspunkt og nyt med god samvittighet. Husk å si takk for maten når du henter - det er god stil at Jaipur ønsker å redusere matsvinnet sitt!', 
    'food_handling_instructions': '', 
    'can_user_supply_packaging': False, 
    'packaging_option': 'MUST_BRING_BAG', 
    'collection_info': 'OBS: Vi tilbyr ikke bestikk og pose - dette må tas med hjemmefra :-)', 
    'diet_categories': [], 'item_category': 'MEAL', 'buffet': True, 
    'badges': [{'badge_type': 'SERVICE_RATING_SCORE', 'rating_group': 'LIKED', 'percentage': 88, 'user_count': 2347, 'month_count': 6}, {'badge_type': 'OVERALL_RATING_TRUST_SCORE', 'rating_group': 'LIKED', 'percentage': 85, 'user_count': 2347, 'month_count': 6}], 
    'positive_rating_reasons': ['POSITIVE_FEEDBACK_DELICIOUS_FOOD', 'POSITIVE_FEEDBACK_GREAT_QUANTITY', 'POSITIVE_FEEDBACK_GREAT_VALUE', 'POSITIVE_FEEDBACK_QUICK_COLLECTION', 'POSITIVE_FEEDBACK_FRIENDLY_STAFF', 'POSITIVE_FEEDBACK_GREAT_VARIETY'], 
    'average_overall_rating': {'average_overall_rating': 3.9123921924648206, 'rating_count': 2203, 'month_count': 6}, 
    'favorite_count': 0}, 'store': {'store_id': '15345', 
    'store_name': 'Jaipur Indisk Restaurant', 'branch': '', 
    'description': '', 'tax_identifier': '920249000MVA', 
    'website': 'www.jaipur.no', 'store_location': 
    {'address': {'country': {'iso_code': 'NO', 'name': 'Norway'}, 
    'address_line': 'Karl Johans gate 18C, 0159 Oslo, Norway', 'city': '', 
    'postal_code': ''}, 'location': {'longitude': 10.7417245, 'latitude': 59.9126921}}, 
    'logo_picture': {'picture_id': '29836', 'current_url': 'https://images.tgtg.ninja/store/1489165215_HHCAWi70Rd_scale.jpg', 
    'is_automatically_created': False}, 'store_time_zone': 'Europe/Oslo', 'hidden': False, 'favorite_count': 0, 
    'we_care': False, 'distance': 6726.489279214551, 'cover_picture': {'picture_id': '29837', 
    'current_url': 'https://images.tgtg.ninja/store/1489165215_7Cb3jSuXOl_scale.jpg', 
    'is_automatically_created': False}, 'is_manufacturer': False}, 
    'display_name': 'Jaipur Indisk Restaurant (Middag)', 
    'pickup_interval': {'start': '2023-12-22T15:00:00Z', 
    'end': '2023-12-22T19:00:00Z'}, 
    'pickup_location': {'address': {'country': {'iso_code': 'NO', 'name': 'Norway'}, 'address_line': 'Karl Johans gate 18C, 0159 Oslo, Norway', 'city': '', 'postal_code': ''}, 'location': {'longitude': 10.7417245, 'latitude': 59.9126921}}, 'purchase_end': '2023-12-22T19:00:00Z', 'items_available': 49, 'distance': 6726.489279214551, 'favorite': True, 'in_sales_window': True, 'new_item': False, 'item_type': 'MAGIC_BAG', 
    'matches_filters': True, 'item_tags': [{'id': 'X_ITEMS_LEFT', 'short_text': '5+ left', 'long_text': '5+ left'}]},  




    {'item':
    {'item_id': '41009', 
    'sales_taxes': [{'tax_description': 'VAT', 'tax_percentage': 15.0}], 
    'tax_amount': {'code': 'NOK', 'minor_units': 639, 'decimals': 2}, 'price_excluding_taxes': {'code': 'NOK', 'minor_units': 4900, 'decimals': 2}, 'price_including_taxes': {'code': 'NOK', 'minor_units': 4900, 'decimals': 2}, 'value_excluding_taxes': {'code': 'NOK', 'minor_units': 14700, 'decimals': 2}, 'value_including_taxes': {'code': 'NOK', 'minor_units': 14700, 'decimals': 2}, 'taxation_policy': 'PRICE_INCLUDES_TAXES', 'show_sales_taxes': False, 'item_price': {'code': 'NOK', 'minor_units': 4900, 'decimals': 2}, 'item_value': {'code': 'NOK', 'minor_units': 14700, 'decimals': 2}, 
    'cover_picture': {'picture_id': '69932', 'current_url': 'https://images.tgtg.ninja/item/cover/70ff066f-1f5a-4e9d-b365-5bf3ccb12520.jpg', 'is_automatically_created': False}, 
    'logo_picture': {'picture_id': '69930', 'current_url': 'https://images.tgtg.ninja/store/9891807a-5d1a-415c-9d1a-f6ef17032c0c.jpg', 'is_automatically_created': False}, 
    'name': '', 'description': 'Redd en forundringspose med overskuddsmat hos BIT Byporten, og bli med i kampen mot matsvinn! Posen kan for eksempel inneholde forskjellig bakst eller annet godt.   Bestill og betal via appen, hent til angitt hentetidspunkt og nyt med god samvittighet. Husk å si takk for maten når du henter - det er god stil at BIT Byporten ønsker å redusere matsvinnet sitt :-)', 
    'food_handling_instructions': '', 'can_user_supply_packaging': False, 'packaging_option': 'CANT_BRING_ANYTHING', 
    'collection_info': '', 'diet_categories': [], 'item_category': 'BAKED_GOODS', 'buffet': False, 
    'badges': [{'badge_type': 'OVERALL_RATING_TRUST_SCORE', 'rating_group': 'LOVED', 'percentage': 90, 'user_count': 866, 'month_count': 6}, {'badge_type': 'SERVICE_RATING_SCORE', 'rating_group': 'LOVED', 'percentage': 92, 'user_count': 866, 'month_count': 6}], 
    'positive_rating_reasons': ['POSITIVE_FEEDBACK_GREAT_VALUE', 'POSITIVE_FEEDBACK_GREAT_QUANTITY', 'POSITIVE_FEEDBACK_DELICIOUS_FOOD', 'POSITIVE_FEEDBACK_FRIENDLY_STAFF', 'POSITIVE_FEEDBACK_QUICK_COLLECTION', 'POSITIVE_FEEDBACK_GREAT_VARIETY'], 
    'average_overall_rating': {'average_overall_rating': 4.590966122961104, 'rating_count': 797, 'month_count': 6}, 'favorite_count': 0}, 'store': {'store_id': '40527', 'store_name': 'BIT Byporten', 'branch': '', 'description': 'Redd en forundringspose med overskuddsmat hos BIT Byporten, og bli med i kampen mot matsvinn! Posen kan for eksempel inneholde forskjellig bakst eller annet godt. \n\nBestill og betal via appen, hent til angitt hentetidspunkt og nyt med god samvittighet. Husk å si takk for maten når du henter - det er god stil at BIT Byporten ønsker å redusere matsvinnet sitt :-)\n\nSpørsmål? Kontakt info@toogoodtogo.no\n\nFinn oss på Facebook (www.facebook.com/toogoodtogoNorge/) & Instagram (@toogoodtogo.no) - og del gjerne opplevelsen din med oss!', 'tax_identifier': '896228552MVA', 'website': '', 
    'store_location': {'address': {'country': {'iso_code': 'NO', 'name': 'Norway'}, 'address_line': 'Jernbanetorget 6, 0154 Oslo, Norge', 'city': '', 'postal_code': ''}, 
    'location': {'longitude': 10.7522842, 'latitude': 59.9118018}}, 'logo_picture': {'picture_id': '69930', 'current_url': 
    'https://images.tgtg.ninja/store/9891807a-5d1a-415c-9d1a-f6ef17032c0c.jpg', 'is_automatically_created': False}, 
    'store_time_zone': 'Europe/Oslo', 'hidden': False, 'favorite_count': 0, 'we_care': False, 
    'distance': 6726.518707882006, 
    'cover_picture': {'picture_id': '69932', 'current_url': 'https://images.tgtg.ninja/item/cover/70ff066f-1f5a-4e9d-b365-5bf3ccb12520.jpg', 'is_automatically_created': False}, 'is_manufacturer': False}, 
    'display_name': 'BIT Byporten', 
    'pickup_location': {'address': {'country': {'iso_code': 'NO', 'name': 'Norway'}, 'address_line': 'Jernbanetorget 6, 0154 Oslo, Norge', 'city': '', 'postal_code': ''}, 'location': {'longitude': 10.7522842, 'latitude': 59.9118018}}, 
    'items_available': 0, 'distance': 6726.518707882006, 'favorite': True, 'in_sales_window': False, 'new_item': False, 'item_type': 'MAGIC_BAG', 'matches_filters': True, 
    'item_tags': [{'id': 'NOTHING_TO_SAVE_TODAY', 'short_text': 'Nothing today', 'long_text': 'Nothing today'}]},



    {'item': 
    {'item_id': '44616', 'sales_taxes': [{'tax_description': 'VAT', 'tax_percentage': 15.0}], 
    'tax_amount': {'code': 'NOK', 'minor_units': 639, 'decimals': 2}, 
    'price_excluding_taxes': {'code': 'NOK', 'minor_units': 4900, 'decimals': 2}, 
    'price_including_taxes': {'code': 'NOK', 'minor_units': 4900, 'decimals': 2}, 
    'value_excluding_taxes': {'code': 'NOK', 'minor_units': 14700, 'decimals': 2}, 
    'value_including_taxes': {'code': 'NOK', 'minor_units': 14700, 'decimals': 2}, 
    'taxation_policy': 'PRICE_INCLUDES_TAXES', 'show_sales_taxes': False, 
    'item_price': {'code': 'NOK', 'minor_units': 4900, 'decimals': 2}, 
    'item_value': {'code': 'NOK', 'minor_units': 14700, 'decimals': 2}, 
    'cover_picture': {'picture_id': '69932', 'current_url': 'https://images.tgtg.ninja/item/cover/70ff066f-1f5a-4e9d-b365-5bf3ccb12520.jpg', 'is_automatically_created': False}, 
    'logo_picture': {'picture_id': '69930', 'current_url': 'https://images.tgtg.ninja/store/9891807a-5d1a-415c-9d1a-f6ef17032c0c.jpg', 'is_automatically_created': False}, 
    'name': '', 'description': 'Redd en forundringspose med overskuddsmat hos BIT Bussterminal, og bli med i kampen mot matsvinn! Posen kan for eksempel inneholde forskjellig bakst eller annet godt.   Bestill og betal via appen, hent til angitt hentetidspunkt og nyt med god samvittighet. Husk å si takk for maten når du henter - det er god stil at BIT ønsker å redusere matsvinnet sitt :-)', 
    'food_handling_instructions': '', 'can_user_supply_packaging': False, 'packaging_option': 'CANT_BRING_ANYTHING', 
    'collection_info': '', 'diet_categories': [], 'item_category': 'BAKED_GOODS', 'buffet': False, 
    'badges': [{'badge_type': 'SERVICE_RATING_SCORE', 'rating_group': 'LOVED', 'percentage': 94, 'user_count': 1421, 'month_count': 6}, {'badge_type': 'OVERALL_RATING_TRUST_SCORE', 'rating_group': 'LOVED', 'percentage': 91, 'user_count': 1421, 'month_count': 6}], 
    'positive_rating_reasons': ['POSITIVE_FEEDBACK_GREAT_VALUE', 'POSITIVE_FEEDBACK_GREAT_QUANTITY', 'POSITIVE_FEEDBACK_DELICIOUS_FOOD', 'POSITIVE_FEEDBACK_FRIENDLY_STAFF', 'POSITIVE_FEEDBACK_QUICK_COLLECTION', 'POSITIVE_FEEDBACK_GREAT_VARIETY'], 
    'average_overall_rating': {'average_overall_rating': 4.630699088145897, 'rating_count': 1316, 'month_count': 6}, 
    'favorite_count': 0}, 'store': {'store_id': '43384', 'store_name': 'BIT Bussterminalen', 'branch': '', 'description': '', 'tax_identifier': '896228552MVA', 'website': '', 
    'store_location': {'address': {'country': {'iso_code': 'NO', 'name': 'Norway'}, 
    'address_line': 'Schweigaards gate 10, 0185 Oslo, Norge', 'city': '', 'postal_code': ''}, 
    'location': {'longitude': 10.7581479, 'latitude': 59.9116799}}, 
    'logo_picture': {'picture_id': '69930', 'current_url': 'https://images.tgtg.ninja/store/9891807a-5d1a-415c-9d1a-f6ef17032c0c.jpg',
    'is_automatically_created': False}, 
    'store_time_zone': 'Europe/Oslo', 'hidden': False, 'favorite_count': 0, 
    'we_care': False, 'distance': 6726.575559007227, 
    'cover_picture': {'picture_id': '69932', 'current_url': 'https://images.tgtg.ninja/item/cover/70ff066f-1f5a-4e9d-b365-5bf3ccb12520.jpg', 
    'is_automatically_created': False}, 'is_manufacturer': False}, 
    'display_name': 'BIT Bussterminalen', 
    'pickup_location': {'address': {'country': {'iso_code': 'NO', 'name': 'Norway'}, 
    'address_line': 'Schweigaards gate 10, 0185 Oslo, Norge', 'city': '', 'postal_code': ''}, 
    'location': {'longitude': 10.7581479, 'latitude': 59.9116799}}, 'items_available': 0, 
    'distance': 6726.575559007227, 'favorite': True, 'in_sales_window': False, 'new_item': False, 
    'item_type': 'MAGIC_BAG', 'matches_filters': True, 
    'item_tags': [{'id': 'NOTHING_TO_SAVE_TODAY', 'short_text': 'Nothing today', 'long_text': 'Nothing today'}]}

    ]
    for i in items: 
        butikk = Butikk(i['store']['store_name'])
        butikker[i['store']['store_name']] = butikk
        butikk.legg_til_butikk()

def get_available_items(email: str, client: TgtgClient):
    tid = strftime("%H:%M", gmtime())
    #items = client.get_items()
    items = [
    {'item': {'item_id': '15441', 'sales_taxes': [{'tax_description': 'VAT', 'tax_percentage': 15.0}], 'tax_amount': {'code': 'NOK', 'minor_units': 1030, 'decimals': 2}, 'price_excluding_taxes': {'code': 'NOK', 'minor_units': 7900, 'decimals': 2}, 'price_including_taxes': {'code': 'NOK', 'minor_units': 7900, 'decimals': 2}, 'value_excluding_taxes': {'code': 'NOK', 'minor_units': 0, 'decimals': 2}, 'value_including_taxes': 
    {'code': 'NOK', 'minor_units': 0, 'decimals': 2}, 'taxation_policy': 'PRICE_INCLUDES_TAXES', 
    'show_sales_taxes': False, 'item_price': {'code': 'NOK', 'minor_units': 7900, 'decimals': 2}, 
    'item_value': {'code': 'NOK', 'minor_units': 0, 'decimals': 2}, 'cover_picture': {'picture_id': '29837', 
    'current_url': 'https://images.tgtg.ninja/store/1489165215_7Cb3jSuXOl_scale.jpg', 
    'is_automatically_created': False}, 'logo_picture': {'picture_id': '29836', 
    'current_url': 'https://images.tgtg.ninja/store/1489165215_HHCAWi70Rd_scale.jpg', 
    'is_automatically_created': False}, 'name': 'Middag', 
    'description': 'Redd en forundringsporsjon med deilig overskuddsmat fra Jaipur, og bli med i kampen mot matsvinn! \n\nInnholdet vil variere, og kan for eksempel være retter med kylling, lam, biff, scampi, fisk og/eller grønnsaker/vegetar - eller en miks av disse. Ris følger alltid med. Alle rettene er glutenfrie, og inneholder melkeprodukter og cashewnøtter (ingen peanøtter eller egg).\n\nOBS: Vi tilbyr ikke bestikk og pose - dette må tas med hjemmefra :-)\n\nBestill og betal via appen, hent til angitt hentetidspunkt og nyt med god samvittighet. Husk å si takk for maten når du henter - det er god stil at Jaipur ønsker å redusere matsvinnet sitt!', 
    'food_handling_instructions': '', 
    'can_user_supply_packaging': False, 
    'packaging_option': 'MUST_BRING_BAG', 
    'collection_info': 'OBS: Vi tilbyr ikke bestikk og pose - dette må tas med hjemmefra :-)', 
    'diet_categories': [], 'item_category': 'MEAL', 'buffet': True, 
    'badges': [{'badge_type': 'SERVICE_RATING_SCORE', 'rating_group': 'LIKED', 'percentage': 88, 'user_count': 2347, 'month_count': 6}, {'badge_type': 'OVERALL_RATING_TRUST_SCORE', 'rating_group': 'LIKED', 'percentage': 85, 'user_count': 2347, 'month_count': 6}], 
    'positive_rating_reasons': ['POSITIVE_FEEDBACK_DELICIOUS_FOOD', 'POSITIVE_FEEDBACK_GREAT_QUANTITY', 'POSITIVE_FEEDBACK_GREAT_VALUE', 'POSITIVE_FEEDBACK_QUICK_COLLECTION', 'POSITIVE_FEEDBACK_FRIENDLY_STAFF', 'POSITIVE_FEEDBACK_GREAT_VARIETY'], 
    'average_overall_rating': {'average_overall_rating': 3.9123921924648206, 'rating_count': 2203, 'month_count': 6}, 
    'favorite_count': 0}, 'store': {'store_id': '15345', 
    'store_name': 'Jaipur Indisk Restaurant', 'branch': '', 
    'description': '', 'tax_identifier': '920249000MVA', 
    'website': 'www.jaipur.no', 'store_location': 
    {'address': {'country': {'iso_code': 'NO', 'name': 'Norway'}, 
    'address_line': 'Karl Johans gate 18C, 0159 Oslo, Norway', 'city': '', 
    'postal_code': ''}, 'location': {'longitude': 10.7417245, 'latitude': 59.9126921}}, 
    'logo_picture': {'picture_id': '29836', 'current_url': 'https://images.tgtg.ninja/store/1489165215_HHCAWi70Rd_scale.jpg', 
    'is_automatically_created': False}, 'store_time_zone': 'Europe/Oslo', 'hidden': False, 'favorite_count': 0, 
    'we_care': False, 'distance': 6726.489279214551, 'cover_picture': {'picture_id': '29837', 
    'current_url': 'https://images.tgtg.ninja/store/1489165215_7Cb3jSuXOl_scale.jpg', 
    'is_automatically_created': False}, 'is_manufacturer': False}, 
    'display_name': 'Jaipur Indisk Restaurant (Middag)', 
    'pickup_interval': {'start': '2023-12-22T15:00:00Z', 
    'end': '2023-12-22T19:00:00Z'}, 
    'pickup_location': {'address': {'country': {'iso_code': 'NO', 'name': 'Norway'}, 'address_line': 'Karl Johans gate 18C, 0159 Oslo, Norway', 'city': '', 'postal_code': ''}, 'location': {'longitude': 10.7417245, 'latitude': 59.9126921}}, 'purchase_end': '2023-12-22T19:00:00Z', 'items_available': 49, 'distance': 6726.489279214551, 'favorite': True, 'in_sales_window': True, 'new_item': False, 'item_type': 'MAGIC_BAG', 
    'matches_filters': True, 'item_tags': [{'id': 'X_ITEMS_LEFT', 'short_text': '5+ left', 'long_text': '5+ left'}]},  




    {'item':
    {'item_id': '41009', 
    'sales_taxes': [{'tax_description': 'VAT', 'tax_percentage': 15.0}], 
    'tax_amount': {'code': 'NOK', 'minor_units': 639, 'decimals': 2}, 'price_excluding_taxes': {'code': 'NOK', 'minor_units': 4900, 'decimals': 2}, 'price_including_taxes': {'code': 'NOK', 'minor_units': 4900, 'decimals': 2}, 'value_excluding_taxes': {'code': 'NOK', 'minor_units': 14700, 'decimals': 2}, 'value_including_taxes': {'code': 'NOK', 'minor_units': 14700, 'decimals': 2}, 'taxation_policy': 'PRICE_INCLUDES_TAXES', 'show_sales_taxes': False, 'item_price': {'code': 'NOK', 'minor_units': 4900, 'decimals': 2}, 'item_value': {'code': 'NOK', 'minor_units': 14700, 'decimals': 2}, 
    'cover_picture': {'picture_id': '69932', 'current_url': 'https://images.tgtg.ninja/item/cover/70ff066f-1f5a-4e9d-b365-5bf3ccb12520.jpg', 'is_automatically_created': False}, 
    'logo_picture': {'picture_id': '69930', 'current_url': 'https://images.tgtg.ninja/store/9891807a-5d1a-415c-9d1a-f6ef17032c0c.jpg', 'is_automatically_created': False}, 
    'name': '', 'description': 'Redd en forundringspose med overskuddsmat hos BIT Byporten, og bli med i kampen mot matsvinn! Posen kan for eksempel inneholde forskjellig bakst eller annet godt.   Bestill og betal via appen, hent til angitt hentetidspunkt og nyt med god samvittighet. Husk å si takk for maten når du henter - det er god stil at BIT Byporten ønsker å redusere matsvinnet sitt :-)', 
    'food_handling_instructions': '', 'can_user_supply_packaging': False, 'packaging_option': 'CANT_BRING_ANYTHING', 
    'collection_info': '', 'diet_categories': [], 'item_category': 'BAKED_GOODS', 'buffet': False, 
    'badges': [{'badge_type': 'OVERALL_RATING_TRUST_SCORE', 'rating_group': 'LOVED', 'percentage': 90, 'user_count': 866, 'month_count': 6}, {'badge_type': 'SERVICE_RATING_SCORE', 'rating_group': 'LOVED', 'percentage': 92, 'user_count': 866, 'month_count': 6}], 
    'positive_rating_reasons': ['POSITIVE_FEEDBACK_GREAT_VALUE', 'POSITIVE_FEEDBACK_GREAT_QUANTITY', 'POSITIVE_FEEDBACK_DELICIOUS_FOOD', 'POSITIVE_FEEDBACK_FRIENDLY_STAFF', 'POSITIVE_FEEDBACK_QUICK_COLLECTION', 'POSITIVE_FEEDBACK_GREAT_VARIETY'], 
    'average_overall_rating': {'average_overall_rating': 4.590966122961104, 'rating_count': 797, 'month_count': 6}, 'favorite_count': 0}, 'store': {'store_id': '40527', 'store_name': 'BIT Byporten', 'branch': '', 'description': 'Redd en forundringspose med overskuddsmat hos BIT Byporten, og bli med i kampen mot matsvinn! Posen kan for eksempel inneholde forskjellig bakst eller annet godt. \n\nBestill og betal via appen, hent til angitt hentetidspunkt og nyt med god samvittighet. Husk å si takk for maten når du henter - det er god stil at BIT Byporten ønsker å redusere matsvinnet sitt :-)\n\nSpørsmål? Kontakt info@toogoodtogo.no\n\nFinn oss på Facebook (www.facebook.com/toogoodtogoNorge/) & Instagram (@toogoodtogo.no) - og del gjerne opplevelsen din med oss!', 'tax_identifier': '896228552MVA', 'website': '', 
    'store_location': {'address': {'country': {'iso_code': 'NO', 'name': 'Norway'}, 'address_line': 'Jernbanetorget 6, 0154 Oslo, Norge', 'city': '', 'postal_code': ''}, 
    'location': {'longitude': 10.7522842, 'latitude': 59.9118018}}, 'logo_picture': {'picture_id': '69930', 'current_url': 
    'https://images.tgtg.ninja/store/9891807a-5d1a-415c-9d1a-f6ef17032c0c.jpg', 'is_automatically_created': False}, 
    'store_time_zone': 'Europe/Oslo', 'hidden': False, 'favorite_count': 0, 'we_care': False, 
    'distance': 6726.518707882006, 
    'cover_picture': {'picture_id': '69932', 'current_url': 'https://images.tgtg.ninja/item/cover/70ff066f-1f5a-4e9d-b365-5bf3ccb12520.jpg', 'is_automatically_created': False}, 'is_manufacturer': False}, 
    'display_name': 'BIT Byporten', 
    'pickup_location': {'address': {'country': {'iso_code': 'NO', 'name': 'Norway'}, 'address_line': 'Jernbanetorget 6, 0154 Oslo, Norge', 'city': '', 'postal_code': ''}, 'location': {'longitude': 10.7522842, 'latitude': 59.9118018}}, 
    'items_available': 0, 'distance': 6726.518707882006, 'favorite': True, 'in_sales_window': False, 'new_item': False, 'item_type': 'MAGIC_BAG', 'matches_filters': True, 
    'item_tags': [{'id': 'NOTHING_TO_SAVE_TODAY', 'short_text': 'Nothing today', 'long_text': 'Nothing today'}]},



    {'item': 
    {'item_id': '44616', 'sales_taxes': [{'tax_description': 'VAT', 'tax_percentage': 15.0}], 
    'tax_amount': {'code': 'NOK', 'minor_units': 639, 'decimals': 2}, 
    'price_excluding_taxes': {'code': 'NOK', 'minor_units': 4900, 'decimals': 2}, 
    'price_including_taxes': {'code': 'NOK', 'minor_units': 4900, 'decimals': 2}, 
    'value_excluding_taxes': {'code': 'NOK', 'minor_units': 14700, 'decimals': 2}, 
    'value_including_taxes': {'code': 'NOK', 'minor_units': 14700, 'decimals': 2}, 
    'taxation_policy': 'PRICE_INCLUDES_TAXES', 'show_sales_taxes': False, 
    'item_price': {'code': 'NOK', 'minor_units': 4900, 'decimals': 2}, 
    'item_value': {'code': 'NOK', 'minor_units': 14700, 'decimals': 2}, 
    'cover_picture': {'picture_id': '69932', 'current_url': 'https://images.tgtg.ninja/item/cover/70ff066f-1f5a-4e9d-b365-5bf3ccb12520.jpg', 'is_automatically_created': False}, 
    'logo_picture': {'picture_id': '69930', 'current_url': 'https://images.tgtg.ninja/store/9891807a-5d1a-415c-9d1a-f6ef17032c0c.jpg', 'is_automatically_created': False}, 
    'name': '', 'description': 'Redd en forundringspose med overskuddsmat hos BIT Bussterminal, og bli med i kampen mot matsvinn! Posen kan for eksempel inneholde forskjellig bakst eller annet godt.   Bestill og betal via appen, hent til angitt hentetidspunkt og nyt med god samvittighet. Husk å si takk for maten når du henter - det er god stil at BIT ønsker å redusere matsvinnet sitt :-)', 
    'food_handling_instructions': '', 'can_user_supply_packaging': False, 'packaging_option': 'CANT_BRING_ANYTHING', 
    'collection_info': '', 'diet_categories': [], 'item_category': 'BAKED_GOODS', 'buffet': False, 
    'badges': [{'badge_type': 'SERVICE_RATING_SCORE', 'rating_group': 'LOVED', 'percentage': 94, 'user_count': 1421, 'month_count': 6}, {'badge_type': 'OVERALL_RATING_TRUST_SCORE', 'rating_group': 'LOVED', 'percentage': 91, 'user_count': 1421, 'month_count': 6}], 
    'positive_rating_reasons': ['POSITIVE_FEEDBACK_GREAT_VALUE', 'POSITIVE_FEEDBACK_GREAT_QUANTITY', 'POSITIVE_FEEDBACK_DELICIOUS_FOOD', 'POSITIVE_FEEDBACK_FRIENDLY_STAFF', 'POSITIVE_FEEDBACK_QUICK_COLLECTION', 'POSITIVE_FEEDBACK_GREAT_VARIETY'], 
    'average_overall_rating': {'average_overall_rating': 4.630699088145897, 'rating_count': 1316, 'month_count': 6}, 
    'favorite_count': 0}, 'store': {'store_id': '43384', 'store_name': 'BIT Bussterminalen', 'branch': '', 'description': '', 'tax_identifier': '896228552MVA', 'website': '', 
    'store_location': {'address': {'country': {'iso_code': 'NO', 'name': 'Norway'}, 
    'address_line': 'Schweigaards gate 10, 0185 Oslo, Norge', 'city': '', 'postal_code': ''}, 
    'location': {'longitude': 10.7581479, 'latitude': 59.9116799}}, 
    'logo_picture': {'picture_id': '69930', 'current_url': 'https://images.tgtg.ninja/store/9891807a-5d1a-415c-9d1a-f6ef17032c0c.jpg',
    'is_automatically_created': False}, 
    'store_time_zone': 'Europe/Oslo', 'hidden': False, 'favorite_count': 0, 
    'we_care': False, 'distance': 6726.575559007227, 
    'cover_picture': {'picture_id': '69932', 'current_url': 'https://images.tgtg.ninja/item/cover/70ff066f-1f5a-4e9d-b365-5bf3ccb12520.jpg', 
    'is_automatically_created': False}, 'is_manufacturer': False}, 
    'display_name': 'BIT Bussterminalen', 
    'pickup_location': {'address': {'country': {'iso_code': 'NO', 'name': 'Norway'}, 
    'address_line': 'Schweigaards gate 10, 0185 Oslo, Norge', 'city': '', 'postal_code': ''}, 
    'location': {'longitude': 10.7581479, 'latitude': 59.9116799}}, 'items_available': 0, 
    'distance': 6726.575559007227, 'favorite': True, 'in_sales_window': False, 'new_item': False, 
    'item_type': 'MAGIC_BAG', 'matches_filters': True, 
    'item_tags': [{'id': 'NOTHING_TO_SAVE_TODAY', 'short_text': 'Nothing today', 'long_text': 'Nothing today'}]}

    ]
    ute = []
    for i in items: 
        if len(i) > 12: 
            ute.append(i)

    for i in ute: 
        if i['in_sales_window'] and i['items_available'] > 0: 
            navn = i['store']['store_name']
            dag = strftime("%A")
            tid = strftime("%H:%M", gmtime())
            print(navn, i['items_available'])
            print(tid)
            butikker[navn].legg_til_tid(dag, tid)

get_items('email', TgtgClient(1, 1, 1, 1))
get_available_items('email', TgtgClient(1, 1, 1, 1))




    