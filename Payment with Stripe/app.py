from flask import Flask, render_template, request, redirect, url_for
import stripe

app = Flask(__name__)

# chaves fakes usadas para teste na api stripe
public_key = "pk_test_g6do5S237ekq10r65BnxO6S0"
stripe.api_key = "sk_test_BQokikJOvBiI2HlWgH4olfQ2"

@app.route('/')
def index():
	
	return render_template("index.html", public_key = public_key)

@app.route('/thankyou')
def thankyou():
	
	return render_template("thankyou.html")

@app.route('/payment', methods = ['POST'])
def payment():

	#info do cliente
	customer = stripe.Customer.create(email = request.form['stripeEmail'],
									  source = request.form['stripeToken'])

	#info do pgto
	charge = stripe.Charge.create(customer = customer.id,
								  amount = 100,
								  currency = 'usd',
								  description = 'Teste')
	
	return redirect(url_for("thankyou.html"))

if __name__ == '__main__':
	app.run(debug = True)