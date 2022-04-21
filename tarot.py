import json
from pprint import pprint as pp


def get_tarot_names(file_name):
    # opening json file
    file = open(file_name)
    # return a JSON object as a dictionary
    card_dictionary = json.load(file)

    # list containing dictionaries
    all_cards_info = []
    card_names = []

    for all_card_info in card_dictionary['cards']:
        all_cards_info.append(all_card_info)

    for all_card_info in all_cards_info:
        card_names.append(all_card_info['name'])
    file.close()
    return card_names


get_tarot_names('tarot-images.json')

