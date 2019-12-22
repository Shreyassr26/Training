def get_input():
    try:
        a = int(input("Enter the a value"))
        b = int(input("Enter the b value"))
        return a,b
    except ValueError as e:
        print(e)
        return get_input()
    finally:
        print("finally of get_input")

def div(a,b):
    try:
        c = a/b
        return c
    except ZeroDivisionError as e:
        print(e)
    finally:
        print("finally of division")

def main():
    try:
        a,b = get_input()
        c = div(a,b)
        print(c)
    except ZeroDivisionError as e:
        print(e)
        main()
    except:
        print("Exception is arrised")
        main()
    finally:
        print("Process completed")