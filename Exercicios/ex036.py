s = float(input("What is your salary? :"))  # salary
i = float(input('What is the value of the house? :'))  # valor house
p = int(input('In how many years? :'))    # years old
print('=-=-'*8)
if i / (p * 12) <= (s * 30) / 100:
    print('Approved')
else:
    print('Declined')
