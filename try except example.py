
try:
    forMe = open('CarModels.txt', 'r')
except IOError:
    print('No such file')
else:                               # else statement is optional; see "try example 2.py"
    openned = forMe.readlines()
    print(openned)

