import matplotlib.pyplot as plt

# Correcting the Plot
input_values = [1,2,3,4,5]
squares = [1, 4, 9, 16, 25]

# Using Built-in Styles
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)  # added to customize the chart

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

plt.show()



