from model.bill import Bill
from model.flatmate import Flatmate
from report.pdfreport import PdfReport


print("Hi user!. Please enter the next details: ")
amount = float(input("Bill amount: "))
period = input("What is the bill period? E.g January 2022 ")
bill = Bill(amount, period)


name1 = input("What is your Name? ")
days_in_house1 = int(input
                     (f"How many days {name1} stay in the house during {period}? "))
flatmate1 = Flatmate(name1, days_in_house1)

name2 = input("What is the name of the other flatmate? ")
days_in_house2 = int(input
                     (f"How many days {name2} stay in the house during {period}? "))

flatmate2 = Flatmate(name2, days_in_house2)

print(f"{flatmate1.name} pays",  flatmate1.pays(bill, flatmate2))
print(f"{flatmate2.name} pays",  flatmate2.pays(bill, flatmate1))

pdf_report = PdfReport(f"{bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, bill)
