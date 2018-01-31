"""Write a function that accepts a filename as input argument and reads the file and saves each line of the file as
an element in a list (without the new line ("\n")character) and returns the list.
Each line of the file has comma separated values: eg:
 2017,Mazda,Mazda6
2018,Honda,Accord
2018,Toyota,Camry
2017,Ford,Fusion"""

def listCars():
    cars = open("CarModels.txt", 'r')
    carList = cars.readlines()
    print(carList)


listCars()