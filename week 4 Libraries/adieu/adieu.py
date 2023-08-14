import inflect

p = inflect.engine()
names = []

while True:
    try:
        name = input("Name: ")
    except:
        break
    names.append(name)

print("Adieu, adieu, to", p.join(names))
