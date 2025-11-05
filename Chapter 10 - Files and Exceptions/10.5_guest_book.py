from pathlib import Path

path = Path("guest_book.txt")

print("Enter 'q' to quit.")
names = []

while True:
    name = input("Enter your name: ").strip()
    if name.lower() == "q":
        break
    if not name:           # skip empty submissions
        continue
    names.append(name)

# Write all collected names to the file, one per line
if names:
    path.write_text("\n".join(names) + "\n", encoding="utf-8")
    print(f"Wrote {len(names)} name(s) to {path.name}.")
else:
    print("No names entered; nothing written.")


