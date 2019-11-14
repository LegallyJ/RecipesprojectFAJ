from flask import Flask, render_template, request

# app = Flask("MyApp")

# @app.route("/Jenny")
# def hello_someone(name):
#     return render_template("hello.html", name=name.title())


# @app.route("/signup", methods=["POST"])
# def sign_up():
#     form_data = request.form
#     print form_data["email"]
#     return "All OK"

# app.run(debug=True)


#These modules are all from flask
from flask import Flask, render_template, request
#This module is from dotenv
from dotenv import load_dotenv
#These are python provided modules
import requests, os

app = Flask("MyExampleApp")

@app.route("/")
def home_page():
	return render_template("home.html")

# @app.route("/otherpage")
# def other_page():
# 	return render_template("other_page.html")
#search: embed twitter feed into flask website

@app.route("/apiexample", methods=["POST"])
def api_example():
	#We use the request module to easily collect all the data input into the form
	form_data = request.form
	input_ingredient_name = form_data["ingredient"]

	results = get_recipes(input_ingredient_name)

# 	#The second argument of the render_template method lets us send data into our html form
# 	#You can pass multiple things in - just separate them with commas
# 	#You can also pass in data in lists, and then pull out items from the list within the.html file itself!
	return render_template("recipes.html", reciperesults=results, user_data=form_data)

def get_recipes(input_ingredient_name):
	load_dotenv();
	api_key = os.getenv("RECIPES_API_KEY")

	endpoint = 'https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/'
	payload = {"apikey": api_key, "s":input_ingredient_name}
	response = requests.get(endpoint, params=payload)

	json_data = response.json()

	#You'll see any printed data in your terminal - helpful to understand what's happening, and to debug
	print "JSON response from the API call:"
	print json_data

	return json_data["Search"]

app.run(debug=True)
