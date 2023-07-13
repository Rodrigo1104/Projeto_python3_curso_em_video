test = list()
test.append('Rodrigo')
test.append(30)
galera = list()
galera.append(test[:])
test[0] = 'Emily'
test[1] = 20
galera.append(test[:])
print(galera)
