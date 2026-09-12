import numpy as np
from src.plotting import plot_sensitivity


def main():


    # Base case — your standard reference values
    S, K, T, r, sigma = 100, 100, 1, 0.05, 0.20

    plot_sensitivity("S", np.linspace(50, 150, 100), S, K, T, r, sigma, "graphs/stock_price_sensitivity.png")
    plot_sensitivity("K", np.linspace(50, 150, 100), S, K, T, r, sigma, "graphs/strike_price_sensitivity.png")
    plot_sensitivity("T", np.linspace(0.01, 2, 100), S, K, T, r, sigma, "graphs/time_sensitivity.png")
    plot_sensitivity("sigma", np.linspace(0.05, 0.6, 100), S, K, T, r, sigma, "graphs/volatility_sensitivity.png")
    plot_sensitivity("r", np.linspace(0.0, 0.15, 100), S, K, T, r, sigma, "graphs/interest_rate_sensitivity.png")



if __name__ == "__main__":
    main()