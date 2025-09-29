import numpy as np
import matplotlib.pyplot as plt

# === Parameters you can change ===
portfolio_size = 100_000   # total dollars in portfolio
num_positions = 100000        # number of stocks in portfolio
avg_return = 0.07          # expected annual return per stock
volatility = 0.60          # standard deviation of stock returns (20%)
simulations = 10_000       # number of random portfolios to simulate

# === Simulation ===
weights = np.ones(num_positions) / num_positions  # equal weighting
returns = np.random.normal(avg_return, volatility, (simulations, num_positions))
portfolio_returns = (returns @ weights) * portfolio_size

# === Results ===
mean_return = np.mean(portfolio_returns) / portfolio_size
std_dev = np.std(portfolio_returns) / portfolio_size

print(f"Expected Portfolio Return: {mean_return:.2%}")
print(f"Portfolio Risk (Std Dev): {std_dev:.2%}")

# === Visualization ===
plt.hist(portfolio_returns / portfolio_size, bins=50, alpha=0.7, color="blue")
plt.axvline(mean_return, color="red", linestyle="dashed", linewidth=2, label="Mean")
plt.title(f"Distribution of Portfolio Returns ({num_positions} positions)")
plt.xlabel("Return")
plt.ylabel("Frequency")
plt.legend()
plt.show()