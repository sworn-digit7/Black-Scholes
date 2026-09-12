# Black-Scholes Option Pricing Model

A from-scratch Python implementation of the Black-Scholes option pricing model, including full Greeks calculation, input validation, automated testing, and sensitivity analysis via generated graphs.

## Overview

This project implements the Black-Scholes formula for pricing European call and put options, without relying on any pre-built financial libraries — every formula (probability functions, `d1`/`d2`, pricing, and all five Greeks) is derived and coded manually using only `math` and `numpy`.

The program takes five market inputs from the user (stock price, strike price, time to expiry, volatility, and risk-free rate), validates them, calculates the fair option price and its sensitivities, and generates graphs showing how the option's price responds to changes in each input.

## Features

- **Option pricing** — European call and put prices via the closed-form Black-Scholes formula
- **The Greeks** — Delta, Gamma, Vega, Theta, and Rho, calculated from first principles
- **Input validation** — rejects invalid inputs (e.g. negative prices, zero time-to-expiry) with a re-prompt loop rather than crashing
- **Automated tests** — `pytest` suite verifying every pricing and Greek function against known correct values, plus a put-call parity check
- **Sensitivity graphs** — five auto-generated plots showing how call/put price responds to each input variable, dynamically scaled around the user's actual inputs

## Project Structure

```
Black-Scholes/
│
├── main.py                  # Entry point — collects input, runs calculations, generates graphs
│
├── src/
│   ├── __init__.py
│   ├── black_scholes.py     # Core pricing formulas (d1, d2, call/put price, normal pdf/cdf)
│   ├── greeks.py             # Delta, Gamma, Vega, Theta, Rho
│   ├── validation.py         # Input validation
│   └── plotting.py           # Sensitivity graph generation
│
├── tests/
│   ├── test_pricing.py       # Tests for pricing formulas + put-call parity
│   └── test_greeks.py        # Tests for all five Greeks
│
├── graphs/                   # Auto-generated sensitivity graphs (created on run)
│
├── requirements.txt
└── README.md
```

## The Maths

For a European call option:

```
C = S·N(d1) − K·e^(−rT)·N(d2)
```

For a European put option:

```
P = K·e^(−rT)·N(−d2) − S·N(−d1)
```

Where:

```
d1 = [ln(S/K) + (r + σ²/2)T] / (σ√T)
d2 = d1 − σ√T
```

| Symbol | Meaning |
|---|---|
| S | Current stock price |
| K | Strike price |
| T | Time to expiry (years) |
| r | Risk-free interest rate |
| σ | Volatility (annualised standard deviation) |
| N(x) | Cumulative distribution function of the standard normal distribution |

## Installation

Clone the repository and install dependencies:

```bash
git clone <your-repo-url>
cd Black-Scholes
pip install -r requirements.txt
```

## Usage

Run the program from the project root:

```bash
python main.py
```

You'll be prompted for:
- Stock price
- Strike price
- Time to expiry (in years)
- Volatility (as a decimal, e.g. 0.2 for 20%)
- Risk-free rate (as a decimal, e.g. 0.05 for 5%)

The program then prints the call price, put price, and all five Greeks, and saves five sensitivity graphs to the `graphs/` folder.

### Example

```
Stock price: 100
Strike price: 100
Time to expiry: 1
Volatility: 0.20
Risk-free rate: 0.05

Call Price: £10.4506
Put Price: £5.5735
Delta: 0.6368
Gamma: 0.0188
Vega: 37.5240
Theta: -6.4140
Rho: 53.2325

✅ Graphs generated in the 'graphs/' folder.
```

## Testing

Run the full test suite with:

```bash
python -m pytest
```

Tests verify each pricing and Greek function against known correct values (calculated by hand and cross-checked), and confirm put-call parity holds:

```
C − P = S − K·e^(−rT)
```

## Assumptions & Limitations

This implementation follows the standard Black-Scholes assumptions:
- The underlying follows geometric Brownian motion with constant volatility
- No arbitrage opportunities exist
- No transaction costs or taxes
- The risk-free rate is constant
- The stock pays no dividends
- Options are European-style (exercisable only at expiry)

These assumptions mean the model won't perfectly match real-world option prices (which reflect volatility smiles, jump risk, and discrete dividends), but it remains the foundational model for options pricing and a core building block in quantitative finance.

## Skills Demonstrated

- Translating mathematical formulas into tested, modular Python code
- Input validation and defensive programming
- Unit testing with `pytest`
- Data visualisation with `matplotlib`
- Clean project structure and separation of concerns (pricing, Greeks, validation, and plotting kept independent)

## Possible Extensions

- Support for American options (early exercise)
- Implied volatility calculation (solving for σ given a market price)
- A simple web interface (e.g. Streamlit) for interactive input and live-updating graphs
- Support for continuous dividend yield
