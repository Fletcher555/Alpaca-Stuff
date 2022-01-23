import numpy
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv(r"C:\Users\danie\OneDrive\High School\Grade 12\Semester 1\Math 30\Unit 3\mathProjectdata.csv")
x = data.years
y = data.number

number = int(input("\nWhat Degree Polynomial? "))
formula = numpy.poly1d(numpy.polyfit(x, y, number))

myline = numpy.linspace(2017, 2021,)

def graph():
    plt.scatter(x, y)
    plt.plot(myline, formula(myline))
    plt.xlabel("Years")
    plt.ylabel("#of caribou")
    plt.Text(0, 0.5,)
    plt.title("Regression Graph")
    plt.show()

def year_prediction():
    year = float(input("\nWhat year are you predicting? "))
    calc = formula(year)
    print(calc)

def caribou_prediction():
    prediction = (formula - 100000)
    roots = prediction.roots
    rounded = numpy.round(roots.real, 3) + numpy.round(roots.imag, 3) * 1j
    print(rounded)


print(formula)
graph()
year_prediction()
caribou_prediction()



