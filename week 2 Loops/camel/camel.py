camel = input("camelCase: ")
snake = ""

snake += camel[0].lower()

for i in range(1,len(camel)):
    if camel[i].isupper():
        snake += "_"

    snake += camel[i].lower()

print("snake_case:",snake)