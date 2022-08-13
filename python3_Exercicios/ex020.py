from random import shuffle
n1 = str(input('first? :'))
n2 = str(input('second? :'))
n3 = str(input('third? :'))
n4 = str(input('fourth? :'))
List = [n1, n2, n3, n4]
shuffle(List)
print(List)
