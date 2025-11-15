import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the walk is active.
while True:
    # Make a random walk
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use('classic')
    #fig, ax = plt.subplots()
    fig, ax = plt.subplots(figsize=(15, 9), dpi=100) # Altered the size of the fill screen

    # Coloring the Points
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Oranges,
               edgecolors='none', s=20)
    ax.set_aspect('equal')

    # Emphasize the starting and ending points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running= input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
