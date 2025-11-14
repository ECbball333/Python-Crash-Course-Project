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
    ax.plot(rw.x_values, rw.y_values, linewidth=2)
    ax.set_aspect('equal')

    # Emphasize the starting and ending points
    ax.plot(0, 0, c='green')
    ax.plot(rw.x_values[-1], rw.y_values[0], c='red')

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running= input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
