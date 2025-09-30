import numpy as np
import matplotlib.pyplot as plt

#Parameters you can change
portfolio_size = 100_000   # total dollars in portfolio
num_positions = 1000          # number of stocks in portfolio
avg_return = 0.07          # expected annual return per stock
volatility = 0.20
correlation = 0.1          # standard deviation of stock returns (20%)
max_positions = 50
simulations = 10_000       # number of random portfolios to simulate

def simulate_portfolio(num_positions):
    weights = np.ones(num_positions) / num_positions
    
    # covariance matrix
    cov_matrix = (volatility**2) * (
        correlation * np.ones((num_positions, num_positions)) +
        (1 - correlation) * np.eye(num_positions)
    )
    
    # portfolio variance
    port_variance = weights @ cov_matrix @ weights.T
    port_std_dev = np.sqrt(port_variance)
    
    return port_std_dev

#simulations
positions_range = range(1, max_positions+1)
risks = [simulate_portfolio(n) for n in positions_range]

# plot it
plt.figure(figsize=(8,5))
plt.plot(positions_range, risks, marker="o")
plt.title("Portfolio Risk vs. Number of Positions")
plt.xlabel("Number of Positions")
plt.ylabel("Portfolio Risk (Std Dev)")
plt.grid(True)
plt.show()