myage = 23
year = 2019
print("My name is", __name__)


def main():
    print("First module main's method")


if __name__ == "__main__":
    print("This won't run if I'm  imported.")
    main()
