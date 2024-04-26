def yoda():
    print("Smart, you are!")


print("The __name__ variable is:", __name__)

if __name__ == "__main__":
    print("my_functions is being run directly")
else:
    print("my_functions is being imported")
