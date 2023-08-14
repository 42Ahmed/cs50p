price = 50
coins = 0
amountDue =  price - coins

while amountDue > 0:
    insertedCoins = int(input("insert: "))
    if insertedCoins == 25 or insertedCoins == 10 or insertedCoins == 5:
        coins += insertedCoins
        amountDue =  price - coins
    if amountDue <= 0:
        print("Change Owed:", (coins - price))
    else:
        print(f"Amount Due: {amountDue}")