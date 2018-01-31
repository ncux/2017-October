"""NOTE: This program requires a function be defined, created and called. The call will send values based on user input. The function call must capture a return value that is used in print output.
The function will have parameters and return a string.
Program: fishstore()

create and test fishstore()

    fishstore() takes 2 string arguments: fish & price
    fishstore returns a string in sentence form
    gather input for fish_entry and price_entry to use in calling fishstore()
    print the return value of fishstore()

    example of output: Fish Type: Guppy costs $1

# [ ] create, call and test fishstore() function """

def fishstore(fish, price):
    return fish + ': ' + ' cost = ' + str(price)

fish2 = fishstore('tuna', 12.00)
print(fish2)




