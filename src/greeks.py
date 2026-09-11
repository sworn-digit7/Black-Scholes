from src.black_scholes import normal_cdf
from src.black_scholes import calculate_d1
from src.black_scholes import normal_pdf
import math

def call_delta(S, K, T, r, sigma):

    delta_c = normal_cdf(calculate_d1(S, K, T, r, sigma))

    return delta_c

def put_delta(S, K, T, r, sigma):

    delta_p = normal_cdf(calculate_d1(S, K, T, r, sigma)) - 1

    return delta_p

def gamma(S, K, T, r, sigma):

    r = normal_pdf(calculate_d1(S, K, T, r, sigma)) / ( S * sigma * math.sqrt(T))

    return r

