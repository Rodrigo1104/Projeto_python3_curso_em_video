from random import choice
n1 = str(input('first student? :'))
n2 = str(input('second student? :'))
n3 = str(input('third student? :'))
n4 = str(input('fourth student? :'))
list = [n1, n2, n3, n4]
print("the chosen student was {}".format(choice(list)))
