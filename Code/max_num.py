def max_num(x, y):
    if x > y:
        return x
    else:
        return y

while True:
    try:
        print("Enter your INTEGER value of X and press Enter")
        x = int(input('X: '))

        print("Enter your INTEGER value of Y and press Enter")
        y = int(input('Y: '))

        # print max number
        print('max number: ', max_num(x, y))

        print("========== End ==========")

    except ValueError:
        print('Please input a NUMBER...')
