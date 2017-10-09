def divide(a, b):
    if b == 0:
        return 'Denomintor {} cannot be zero'.format(b)
    else:
        return round(a / float(b), 2)

def get_input():
    val = {'numerator': 0, 'denomintor': 0}
    for i in val.keys():
        while True:
            try:
                val[i] = int(raw_input('Please enter {}:'.format(i)))
            except ValueError:
                print('{} must be integer.'.format(i))
            else:
                break
    print(divide(val['numerator'], val['denomintor']))


get_input();
