import numpy as np
from src.plotting import plot_sensitivity
from src.validation import validate_inputs
from src.black_scholes import normal_cdf, calculate_d1, calculate_d2, call_price, put_price
from src.greeks import call_delta, gamma, vega, call_theta, call_rho


def main():

    while True:
        try:
            S = float(input("Stock price: "))
            K = float(input("Strike price: "))
            T = float(input("Time to expiry: "))
            sigma = float(input("Volatility: "))
            r = float(input("Risk-free rate: "))

            validate_inputs(S, K, T, sigma)  # add r validation once you decide the rule
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.\n")


    print(f"Call Price: £{call_price(S, K, T, r, sigma):.4f}")
    print(f"Put Price: £{put_price(S, K, T, r, sigma):.4f}")
    print(f"Delta: {call_delta(S, K, T, r, sigma):.4f}")
    print(f"Gamma: {gamma(S, K, T, r, sigma):.4f}")
    print(f"Vega: {vega(S, K, T, r, sigma):.4f}")
    print(f"theta: {call_theta(S, K, T, r, sigma):.4f}")
    print(f"Rho: {call_rho(S, K, T, r, sigma):.4f}")

    plot_sensitivity("S", np.linspace(S * 0.5, S * 1.5, 100), S, K, T, r, sigma, "graphs/stock_price_sensitivity.png")
    plot_sensitivity("K", np.linspace(K * 0.5, K * 1.5, 100), S, K, T, r, sigma, "graphs/strike_price_sensitivity.png")
    plot_sensitivity("T", np.linspace(0.01, T * 2, 100), S, K, T, r, sigma, "graphs/time_sensitivity.png")
    plot_sensitivity("sigma", np.linspace(sigma * 0.25, sigma * 2, 100), S, K, T, r, sigma, "graphs/volatility_sensitivity.png")
    plot_sensitivity("r", np.linspace(0.0, r * 3, 100), S, K, T, r, sigma, "graphs/interest_rate_sensitivity.png")


if __name__ == "__main__":
    main()



# S, K, T, r, sigma = 100, 100, 1, 0.05, 0.20