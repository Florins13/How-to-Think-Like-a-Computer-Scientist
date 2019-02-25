# Ex 1
def readposint():
    try:
        check = int(input("Type a positive integer:"))
        if check > 0:
            print("The number inserted is:{0} and is a positive integer!".format(check))
        if check < 0:
            print("The number inserted {0} is not a positive integer!".format(check))
    except ValueError:
        print("Ups, the number inserted is not a number")
    except KeyboardInterrupt:
        print("Ups, nothing was inserted")


readposint()
