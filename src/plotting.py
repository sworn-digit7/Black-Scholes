import numpy as np
import matplotlib.pyplot as plt
from src.black_scholes import call_price, put_price

def plot_sensitivity(param_name, param_range, S, K, T, r, sigma, save_path):
    
    call_prices = []
    put_prices = []

    for value in param_range:
        # Build a fresh copy of inputs each loop, overriding just the one being swept
        params = {"S": S, "K": K, "T": T, "r": r, "sigma": sigma}
        params[param_name] = value

        call_prices.append(call_price(**params))
        put_prices.append(put_price(**params))

    plt.figure(figsize=(8, 5))
    plt.plot(param_range, call_prices, label="Call Price")
    plt.plot(param_range, put_prices, label="Put Price")
    plt.xlabel(param_name)
    plt.ylabel("Option Price (£)")
    plt.title(f"Option Price Sensitivity to {param_name}")
    plt.legend()
    plt.grid(True)
    plt.savefig(save_path)
    plt.close()