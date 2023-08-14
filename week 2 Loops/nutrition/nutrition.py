fruits = [
    {"Name": "Apple","Calories": 130},
    {"Name":"Avocado","Calories": 50},
    {"Name":"Sweet Cherries","Calories": 100},
    {"Name":"Kiwifruit","Calories": 90},
    {"Name":"Pear","Calories": 100},
]
wanted = input("Item: ").title()
for fruit in fruits:
    if wanted == fruit["Name"]:
        print("Calories:",fruit["Calories"])
