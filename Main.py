import numpy as np
import matplotlib.pyplot as plt

# Data for Bitcoin supply and demand
price = np.linspace(0, 20000, 100) # Prices from 0 to 20000
quantity_supplied = 10000 + 0.2 * price # Supply function
quantity_demanded = 20000 - 0.5 * price # Demand function

# Find the equilibrium point (where supply and demand intersect)
equilibrium_point = np.argmin(np.abs(quantity_supplied - quantity_demanded))

# Plot Bitcoin supply and demand
plt.figure(figsize=(10, 6))
plt.plot(price, quantity_supplied, label='Bitcoin Supply', color='blue')
plt.plot(price, quantity_demanded, label='Bitcoin Demand', color='red')
plt.scatter(price[equilibrium_point], quantity_supplied[equailibrium_point],
            color='black', label='Equilibrium Point')

# Labels and title
plt.title('Bitcoin Supply and Demand')
plt.xlabel('Price')
plt.ylabel('Quantity')
plt.legend()

# Equilibrium line
plt.axvline(x=price[equilibrium_point], color='black', linestyle='--')
plt.axhline(y=quantity_supplied[equilibrium_point], color='black', linestyle='--')

# Show the plot
plt.grid(True)
plt.show()