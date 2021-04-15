def spiralize(number):
    x = 1 # starting point and number we are at in spiral
    counter = 0 # variable to keep track how many corners we are at
    i = 2 # increments that get added to starting point
    total = 0 # sum of the corners 

    while x <= number ** 2: # while x is still less than square of number (size of spiral)
        total += x # number we are at gets added to total
        x += i # go to next corner
        counter += 1 # count of which corner we are at
        if counter == 4: # if we make a full rotation arount the corners, got to next one
            i += 2 # increment the space need to reach corners
            counter = 0 # reset the rotation

    return total