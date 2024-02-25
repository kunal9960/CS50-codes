prompt = input("Expression: ")

x, y, z = prompt.split(" ")

x1 = float(x)
z1 = float(z)

if y == "+":
    result = x1 + z1
if y == "-":
    result = x1 - z1
if y == "*":
    result = x1 * z1
if y == "/":
    result = x1 / z1
print(round(result, 1))
