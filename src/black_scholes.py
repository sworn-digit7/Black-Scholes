import math

def normal_pdf(x):
    
    pdf = 1 / ( math.sqrt(2 * math.pi) * (math.e)**((-x**2) / 2) )

    return pdf

def normal_cdf(x):

    cdf = 0.5 * (1 + math.erf(x / math.sqrt(2)))

    return cdf

def calculate_d1(S, K, T, r, sigma):

    d1 =  (math.log(S / K) + ((r + (sigma ** 2)) / 2) * T) / (sigma * math.sqrt(T))

    return d1

def calculate_d2(d1, T, sigma):

    d2 = d1 - (sigma * math.sqrt(T))

    return d2

