from flask import Flask, redirect, url_for, request, flash, escape, render_template
import random
import Fortune_deck as F_D
import json
import tarot


app = Flask(__name__)

# Introduces what I'm doin on the home page:
title = "Hello! <br>This is the main page:" 
title += "Goal of today's stream: <br><h1>Basic Tarot Reader</h1>"
title += "<a href=\"http://127.0.0.1:5000/submit\">tarot page</a>"


# The home page
@app.route("/", methods=['GET', 'POST'])
def home():
	return render_template('index.html')

@app.route("/admin")
def admin():
	return redirect(url_for("home"))

numofcards = 0

# @app.route("/tarot.py", methods=['GET','POST'])
# def tarot_reading():
# 	tarot_card_names = tarot.get_tarot_names('tarot-images.json')


	# print(tarot_deck)

	# return render_template('tarot.py')

# print(tarot_reading())


@app.route('/submit', methods=['GET', 'POST'])
def creates_index_html_page():
	name = request.args.get('name', "N/A")
	numofcards = request.args.get('numofcards', 1, type=int)

	if numofcards > 6:
		numofcards = 6

	print(f"{numofcards}")


	tarot_deck = F_D.TarotDeck()
	sample = random.sample(tarot_deck.list_of_cards, numofcards)



	# Show the descriptions for {numofcards} cards.

	return f"Hey {name}, you selected {numofcards}. Your random cards are: <br><br> {'<br>'.join(repr(samp) for samp in sample)}."



if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, debug=False)







