group = input("How many people are in your party? ")
group = int(group)

if group >= 8:
    print("\nThere is a 30 minute wait.")
else:
    print("\nWe should have a table in about 5 minutes.")