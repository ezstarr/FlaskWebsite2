from flask import Flask, redirect, url_for, request, flash, escape, render_template, jsonify
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


@app.route('/result', methods=['GET', 'POST'])
def creates_read_result_html_page():
    name = request.args.get('name', 'N/A', type=str)
    numofcards = request.args.get('numofcards', 1, type=int)

    if numofcards < 1:
        numofcards = 1
    if numofcards > 6:
        numofcards = 6

    print(f"{numofcards}")

    tarot_deck = F_D.TarotDeck()
    sample = random.sample(tarot_deck.list_of_cards, numofcards)

    # Show the descriptions for {numofcards} cards.

    # return render_template('submit-tarot.html')

    # r_variable = f"Hey {name}, you selected {numofcards}. \n"

    # f"Your random cards are: \n\n {'<br>'.join(repr(samp) for samp in sample)}."

    return render_template('reading_result.html', name=name, sample=sample)




if __name__ == "__main__":
    app.run(debug=False)
