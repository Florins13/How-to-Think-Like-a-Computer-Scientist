import mymodule1
import mymodule2

print((mymodule2.myage - mymodule1.myage) ==
      (mymodule2.year - mymodule1.year))
print("My name is", __name__)
mymodule1.main()
# Ex 5
# So, this print __name__ actually prints the name of the module. If you are
# printing the current module (the one you are in) you will get an __main__
# because you are in main, make sense.
# If you print another module you will just simply get the name of that module.
#
# Whats interesting here is that this condition if __name__ == "__main__": let's
# us set functions that will run only if you are in main, or if you call them directly.
# example mymodule1.main()
