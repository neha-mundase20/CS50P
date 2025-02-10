def main():
    hello("Word")
    goodbye("World")

def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"GoodBye, {name}")

if __name__=="__main__":
    main()
    # Whenever this file will be called from command line, __name__ will be set to "__main__", so then only
    # main() will be called. If this file is called from somewhere else, main() won't be called, but still we
    # will be able to access rest of the functions
