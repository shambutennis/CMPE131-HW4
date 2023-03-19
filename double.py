def double(func):
    def wrapper():
        print(func())
        print("Let’s try that again!")
        print(func())
    return wrapper

