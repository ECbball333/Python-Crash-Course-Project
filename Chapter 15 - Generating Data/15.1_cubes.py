import matplotlib.pyplot as mpl

x_values = list(range(1, 6))
y_values = [x**3 for x in x_values]

fig, ax = mpl.subplots()
ax.scatter(x_values, y_values, s=100, color=(0, .9, 0))
#ax.scatter(x_values, y_values, c=y_values, cmap=mpl.cm.Purples, s=30)

ax.set_title("First 5 cube numbers")
ax.set_xlabel('n')
ax.set_ylabel("n³")

mpl.show()