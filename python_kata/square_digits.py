def square_digits(num):
    snum = str(num)
    final = ''
    for i in snum :
        val = pow(ord(i) - 48, 2)
        final += str(val)
    return int(final)

print(square_digits(9119))