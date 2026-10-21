meaning = 8
print("")

if meaning > 10:
    print("Ride on!")
else:
    print("not today")


# TERNARY OPERATOR
print("not today") if meaning <= 5 else print("Ride on!")

# ANOTHER EXAMPLE OF TERNARY OPERATOR
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)