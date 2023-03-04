n1 = float(input(''))
n2 = float(input(''))
M = (n1 + n2) / 2
if M < 5:
    print('\033[31mDisapproved\033[m')
elif (M == 5) or (M > 5) and (M < 7):
    print('\033[93mRecovery\033[m')
else:
    print('\033[92mApproved\033[m')
