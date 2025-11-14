import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(200)
    rw.fill_walk()

    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(15, 9), dpi=100)
    ax.set_aspect("equal", adjustable="datalim")

    # (Optional) light base path for context
    ax.plot(rw.x_values, rw.y_values, linewidth=1.5, color="gray", alpha=0.35, zorder=1)

    # Fade via colormap: early -> late
    ax.scatter(
        rw.x_values, rw.y_values,
        c=range(rw.num_points),         # color by step index
        cmap="viridis",                 # pick any: 'viridis', 'plasma', 'cividis'
        s=10,                           # a bit larger so the gradient shows
        edgecolors="none",
        zorder=2
    )

    # Start/end markers on top
    ax.plot(0, 0, marker="o", markersize=8, color="green", linestyle="None", zorder=3)
    ax.plot(rw.x_values[-1], rw.y_values[-1], marker="o", markersize=8,
            color="red", linestyle="None", zorder=3)

    ax.axis("off")
    plt.tight_layout()
    plt.show()

    if input("Make another walk? (y/n): ").lower().startswith("n"):
        break
