from src.black_scholes import normal_cdf
from src.black_scholes import calculate_d1
from src.black_scholes import calculate_d2
from src.black_scholes import normal_pdf
import math

def call_delta(S, K, T, r, sigma):

    delta_c = normal_cdf(calculate_d1(S, K, T, r, sigma))

    return delta_c

def put_delta(S, K, T, r, sigma):

    delta_p = normal_cdf(calculate_d1(S, K, T, r, sigma)) - 1

    return delta_p

def gamma(S, K, T, r, sigma):

    gamma_value = normal_pdf(calculate_d1(S, K, T, r, sigma)) / ( S * sigma * math.sqrt(T))

    return gamma_value

def vega(S, K, T, r, sigma):

    v = S * normal_pdf(calculate_d1(S, K, T, r, sigma)) * (math.sqrt(T))

    return v

def call_theta(S, K, T, r, sigma):

    d1 = calculate_d1(S, K, T, r, sigma)
    d2 = calculate_d2(d1, T, sigma)

    c_theta = (

    (- (S * normal_pdf(d1) * sigma) / ( 2 * math.sqrt(T) ))

    - (r * K * (math.e ** (-r*T)) * normal_cdf(d2))

    )

    return c_theta

def put_theta(S, K, T, r, sigma):

    d1 = calculate_d1(S, K, T, r, sigma)
    d2 = calculate_d2(d1, T, sigma)

    p_theta = (

        - (S * normal_pdf(d1) * sigma) / (2 * math.sqrt(T))

        + (r * K * (math.e ** (-r*T)) * normal_cdf( - (d2)))
    )

    return p_theta


def call_rho(S, K, T, r, sigma):

    d1 = calculate_d1(S, K, T, r, sigma)
    d2 = calculate_d2(d1, T, sigma)

    c_rho = (K * T * (math.e ** (-r * T)) * normal_cdf(d2))

    return c_rho

def put_rho(S, K, T, r, sigma):

    d1 = calculate_d1(S, K, T, r, sigma)
    d2 = calculate_d2(d1, T, sigma)

    p_rho = (-K * T * (math.e ** (-r * T)) * normal_cdf(-d2))

    return p_rho