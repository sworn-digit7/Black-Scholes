import math

def normal_pdf(x):
    
    pdf = 1 / ( math.sqrt(2 * math.pi) * (math.e)**((-x**2) / 2) )

    return pdf

