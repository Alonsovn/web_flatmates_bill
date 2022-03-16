from flask import Flask, render_template, request
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField

from web_flatmates_bill.model.bill import Bill
from web_flatmates_bill.model.flatmate import Flatmate

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html',
                               result=False,
                               billform=bill_form)

    def post(self):
        bill_form = BillForm(request.form)
        amount = float(bill_form.amount.data)
        period = bill_form.period.data
        bill = Bill(amount, period)

        name1 = bill_form.name1.data
        days1 = float(bill_form.days_in_house1.data)
        flatmate1 = Flatmate(name1, days1)

        name2 = bill_form.name2.data
        days2 = float(bill_form.days_in_house2.data)
        flatmate2 = Flatmate(name2, days2)

        return render_template('bill_form_page.html',
                               result=True,
                               billform=bill_form,
                               name1=flatmate1.name,
                               amount1=flatmate1.pays(bill, flatmate2),
                               name2=flatmate2.name,
                               amount2=flatmate2.pays(bill, flatmate1))


class ResultsPage(MethodView):

    def post(self):
        bill_form = BillForm(request.form)
        amount = float(bill_form.amount.data)
        period = bill_form.period.data
        bill = Bill(amount, period)

        name1 = bill_form.name1.data
        days1 = float(bill_form.days_in_house1.data)
        flatmate1 = Flatmate(name1, days1)

        name2 = bill_form.name2.data
        days2 = float(bill_form.days_in_house2.data)
        flatmate2 = Flatmate(name2, days2)

        return render_template('results.html',
                               name1=flatmate1.name,
                               amount1=flatmate1.pays(bill, flatmate2),
                               name2=flatmate2.name,
                               amount2=flatmate2.pays(bill, flatmate1))


class BillForm(Form):
    amount = StringField("Bill Amount: ", default=100)
    period = StringField("Bill Period: ", default="March 1")

    name1 = StringField("Name: ", default="John")
    days_in_house1 = StringField("Days in the house: ", default=20)

    name2 = StringField("Name: ", default="Mary")
    days_in_house2 = StringField("Days in the house: ", default=12)

    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill_form_page', view_func=BillFormPage.as_view('bill_form_page'))
# app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))

app.run()
# app.run(debug=True)
