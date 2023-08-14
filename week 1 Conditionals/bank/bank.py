Greeting = input("Greeting: ").strip().lower()

if "hello" in Greeting:
    print("$0")
elif Greeting[0]=="h":
    print("$20")
else:
    print("$100")