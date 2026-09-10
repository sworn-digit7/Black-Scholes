from src.black_scholes import normal_cdf
from src.black_scholes import calculate_d1

def call_delta(S, K, T, r, sigma):

    delta_c = normal_cdf(calculate_d1(S, K, T, r, sigma))

    return delta_c

def put_delta(S, K, T, r, sigma):

    delta_p = normal_cdf(calculate_d1(S, K, T, r, sigma)) - 1

    return delta_p


