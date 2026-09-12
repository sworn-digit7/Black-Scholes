import math
from src.black_scholes import normal_cdf, calculate_d1, calculate_d2, call_price, put_price

def test_normal_cdf():
    assert math.isclose(normal_cdf(0), 0.5, rel_tol=1e-6)
    assert math.isclose(normal_cdf(0.35), 0.636831, rel_tol=1e-4)
    assert math.isclose(normal_cdf(0.15), 0.559618, rel_tol=1e-4)

def test_d1():
    d1 = calculate_d1(100, 100, 1, 0.05, 0.20)
    assert math.isclose(d1, 0.35, rel_tol=1e-4)

def test_d2():
    d1 = calculate_d1(100, 100, 1, 0.05, 0.20)
    d2 = calculate_d2(d1, 1, 0.20)
    assert math.isclose(d2, 0.15, rel_tol=1e-4)

def test_call_price():
    c = call_price(100, 100, 1, 0.05, 0.20)
    assert math.isclose(c, 10.4506, rel_tol=1e-3)

def test_put_price():
    p = put_price(100, 100, 1, 0.05, 0.20)
    assert math.isclose(p, 5.5735, rel_tol=1e-3)

def test_put_call_parity():
    S, K, T, r, sigma = 100, 100, 1, 0.05, 0.20
    c = call_price(S, K, T, r, sigma)
    p = put_price(S, K, T, r, sigma)
    rhs = S - K * math.exp(-r * T)
    assert math.isclose(c - p, rhs, rel_tol=1e-3)