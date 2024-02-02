print(f"is 5 less 2? {5 < 2}")
print(f"is 5 equal 7? {5 == 7}")
print(f"is 10 greater 2? {10 > 2}")
print(f"is 17 less 19? {17 < 19}")
print(f"is 65 greater 19? {65 > 19}")


print ("one is equal to 4:",int(1==2))
print ("one is equal to 1:",int(1==1))

myname = "Arjun"
myage = 20
print(f"a: {24}") # numeric literal
print(f"b: {'Greetings'}")  # String variable
print(f"c: {False}")  # Constant Literal
print(f"d: {myname}") # String variable
print(f"e: {myage}") # numeric variable

print((1 -2 +3),(3 - 2 + 1))
print((24 - 2 * 6),(1 + 3 * 6))

print(f"is 'matt'=='matthew'? {'matt'=='matthew'}")

my_name = "arjun"
print("assignment: ",my_name)
print("equality: ",my_name == "arjun")



print("comparison:", "aa" < "b")
print("comparison:",5 < 6)


a = 7
b = 9
print(f"comparison: {a} is greater than {b}" if a > b else "")
print(f"comparison: {a} is less than {b}" if a < b else "")
print(f"comparison: {a} is greater than or equal to {b}" if a >= b else "")
print(f"comparison: {a} is less than or equal to {b}" if a <= b else "")


a = 1
b = 0  # 1 is true while 0 is false
print(f"Logical: AND test {a and b}")
print(f"Logical: OR test {a or b}") # either can be true for result to be true or both can be true
print(f"Logical: XOR test {a ^ b}") # if both are true it will be false; only one can be true
print(f"Logical: NOT test {not a}")


bank_balance = 100
if bank_balance < 200:
    money = 3000
    bank_balance += money
else:
    print("balance is less than or equal to 200.")



bank_balance = 700
savings = 100
if bank_balance < 100:
    money = 1000
    bank_balance += money
elif bank_balance > 200:
    savings += 100
    bank_balance -= 100
else:
    savings += 300
    bank_balance -= 300
    
    
print(bank_balance)
print(savings)


fuel = 3
print("There is enough fuel" if fuel >= 3 else "Fill tank now")