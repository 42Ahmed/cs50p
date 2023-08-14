Expression = input("Expression: ")
x,y,z = Expression.split()

x = int(x)
z = int(z)

match y:
    case "+":
        result = x + z
    case "-":
        result = x - z
    case"*":
        result = x * z
    case"/":
        result = x / z

print(f"{result:.1f}")