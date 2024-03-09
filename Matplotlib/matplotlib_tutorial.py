# Some Basic matplotlib
import matplotlib.pyplot as plt

# Making a Line Graph
x_values = [0, 1, 2, 3, 4, 5]
squares = [0, 1, 4, 9, 16, 25]
plt.plot(x_values, squares)
# Renders Graph
plt.show()

# Making a Scatter Plot
x_values2 = list(range(1000))
squares2 = [x**2 for x in x_values2]
plt.scatter(x_values2, squares2, s=10)

# Customization Options
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize=18)
plt.ylabel("Square of Value", fontsize = 18)
plt.tick_params(axis="both", which="major", labelsize=14)
plt.axis([0, 1100, 0, 1100000])

# 2nd plot does not show until user closes the 1st plot
plt.show()

