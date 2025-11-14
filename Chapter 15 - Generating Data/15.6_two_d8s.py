from collections import Counter
import plotly.express as px
from die import Die

die_1 = Die(8)
die_2 = Die(8)

results = [die_1.roll() + die_2.roll() for _ in range(200_000)]
counts = Counter(results)

poss_results = list(range(2, die_1.num_sides + die_2.num_sides + 1))
frequencies = [counts[v] for v in poss_results]

fig = px.bar(x=poss_results, y=frequencies,
             title="Results of rolling two D8 dice 200,000 times",
             labels={"x": "Result", "y": "Frequency"})
fig.update_layout(xaxis_dtick=1)
fig.show()
fig.write_html("dice_result.html")