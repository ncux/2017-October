
try:
    forMe = open('CarModel.txt')
except IOError:
    print('No such file')

openned = forMe.read()
print(openned)


