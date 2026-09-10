import math

def normal_pdf(x):
    
    pdf = 1 / ( math.sqrt(2 * math.pi) * (math.e)**((-x**2) / 2) )

    return pdf

def normal_cdf(x):

    cdf = 0.5 * (1 + math.erf(x / math.sqrt(2)))

    return cdf
