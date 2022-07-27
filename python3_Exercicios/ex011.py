import math
l1 = float(input('side? :'))
l2 = float(input('height? :'))
a = l1 * l2
ink = math.ceil(a/2)
print('this wall is {:.1f} square meters, and you will need {} paint cans.'.format(a, ink))
