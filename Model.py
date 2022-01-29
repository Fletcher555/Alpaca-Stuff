# First attempt to make black-scholes formula

import numpy as numpy
from scipy.stats import norm
import Alpaca

#r = float(input("Risk free interest rates: "))
s = float(input("Stock price: "))
k = float(input("Market strike price: "))
t = float(input("Time of option expiration in years days: "))
sigma = float(input("Sigma of stock: "))
t=t/365
sigma=sigma/100
primeInterest = 2.5
r=primeInterest/100

def blackScholes(r, s, k, t, sigma, type="c"):
    d1 = (numpy.log(s/k) + (r + sigma**2/2)*t)/(sigma*numpy.sqrt(t))
    d2 = d1 - sigma*numpy.sqrt(t)
    try:
        if type == "c":
            price = s*norm.cdf(d1, 0, 1) - k*numpy.exp(-r*t)*norm.cdf(d2, 0, 1)
        elif type == "p":
            price = k*numpy.exp(-r*t)*norm.cdf(-d2, 0, 1) - s*norm.cdf(-d1, 0, 1)
        return price
    except:
        print("Error - Make sure all option parameters are correct ")

print("Theoretical Option price is: ", round(blackScholes(r, s, k, t, sigma, type="c"),3))
