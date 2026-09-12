import math
from src.greeks import call_delta, gamma, vega, call_theta, call_rho

def test_call_delta():
    assert math.isclose(call_delta(100, 100, 1, 0.05, 0.20), 0.6368, rel_tol= 1e-3)

def test_gamma():
    assert math.isclose(gamma(100, 100, 1, 0.05, 0.20), 0.018762, rel_tol= 1e-3)

def test_vega():
    assert math.isclose(vega(100, 100, 1, 0.05, 0.20), 37.52, rel_tol= 1e-3)

def test_call_theta():
    assert math.isclose(call_theta(100, 100, 1, 0.05, 0.20), -6.41, rel_tol= 1e-3)

def test_call_rho():
    assert math.isclose(call_rho(100, 100, 1, 0.05, 0.20), 53.23, rel_tol= 1e-3)
