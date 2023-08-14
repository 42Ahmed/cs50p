items = {}
while True:
    try:
        item = input().upper()
    except EOFError:
        break
    items[item]= items.get(item,0) + 1

items = sorted(items.items())

for item,count in items:
    print(f"{count} {item}")