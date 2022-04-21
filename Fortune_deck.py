import random
import json

# This creates a list of dictionaries, called a Deck:
# A list containing dictionaries (aka cards)
# A card is stored as a dictionary
# A Deck is a list of dictionaries.


class TarotDeck:
	def __init__(self):
		self.list_of_cards = []
		self.load_deck()

	def load_deck(self):
		"""This adds card objects from tarot-images.json to a list"""
		self.list_of_cards = []   # make sure list is empty each time fill_deck() is called
		with open("tarot-images.json") as json_file:  # opens .json to create a json file(a file-like object)
			json_data = json.load(json_file)  # .load() loads json file into a dict

		for json_card in json_data['cards']:
			self.list_of_cards.append(TarotCard(json_card))


	def __repr__(self):
		"""
		Makes output more readable when using print() on a TarotCard
		:return: string
		"""
		return f"{self.list_of_cards}"

# 	def show(self):
# 		for card in self.list_of_cards:
# 			print("card", card.card_number, card.card_description, card.card_img_image)
#
#
# 	def shuffle(self):
# 		random.shuffle(self.list_of_cards)
#
# 	def does_reading(self, numofcards):
# 		return random.sample(self.list_of_cards, numofcards, counts=None)

#
# # Takes in arguements to create cards:
class TarotCard:
	"""
	This Class creates a TarotCard object with multiple properties loaded from JSON file
	"""
	def __init__(self, json_card):
		"""
		Constructor to initialize/create properties/attributes with the appropriate values from the JSON file.
		:param json_card (a dictionary with all the info on a single card from tarot-cards.json file
		"""
		self.name = json_card.get('name')
		self.number = json_card.get('number')
		self.arcana = json_card.get('arcana')
		self.suit = json_card.get('suit')
		self.img = json_card.get('img')
		self.fortune_telling = json_card.get('fortune_telling')
		self.keywords = json_card.get('keywords')
		self.meanings = TarotMeanings(json_card.get('meanings'))
		self.archetype = json_card.get('Archetype')
		self.hebrew_alphabet = json_card.get('Hebrew Alphabet')
		self.numerology = json_card.get('Numerology')
		self.elemental = json_card.get('Elemental')
		self.mythical_spiritual = json_card.get('Mythical/Spiritual')
		self.questions_to_ask = json_card.get('Questions to Ask')


	def __repr__(self):
		"""
		Makes output more readable when using print() on a TarotCard
		:return: string
		"""
		return f"{self.name} - {self.keywords}"
#
class TarotMeanings:
	"""
	A Class to hold the sub-properties of meanings in the json_card dictionary.
	"""
	def __init__(self, json_meanings):
		"""
		This constructor stores the light and shadow values into its own property
		:param json_meanings: the dict where the light and shadow values are found
		"""
		self.light = json_meanings.get('light')
		self.shadow = json_meanings.get('shadow')


tarot_deck = TarotDeck()

reading = random.sample(tarot_deck.list_of_cards, 4)

for read in reading:
	print(read)