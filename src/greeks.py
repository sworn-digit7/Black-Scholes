from src.black_scholes import normal_cdf
from src.black_scholes import calculate_d1

def call_delta(S, K, T, r, sigma):

    delta = normal_cdf(calculate_d1(S, K, T, r, sigma))

    return delta


