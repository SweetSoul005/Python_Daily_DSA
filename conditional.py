'''if, short hand if, elif, else, nested if else'''

age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")



# Conditional Expression (Ternary Operator)

age = 20
s = "Adult" if age >= 18 else "Minor"
print(s)

#Match-Case Statement : It is similar to the switch-case statement available in other programming languages.


number = 2

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")




