def validate_inputs(S, K, T, sigma):
    
    if S <= 0:
        raise ValueError("Invalid value for stock price")
    if K <= 0:
        raise ValueError("Invalid value for strike price")
    if T <= 0:
        raise ValueError("Invalid value for time to expiry")
    if sigma <= 0:
        raise ValueError("Invalid value for volatility")