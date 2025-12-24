def divide(x, y):
    a = y
    b = x
    result = a / b
    return result

def main():
    breakpoint()
    x = 1
    y = 2
    z = 0
    result = -1
    if x > 5:
        result = divide(y, x)
    else:
        result = divide(z, y)
    print(result)

if __name__ == "__main__":
    main()

