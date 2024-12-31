def high(x):
    list = x.split()
    high = 0
    final = ''

    print(list)

    for word in list :
        curr = 0
        for lett in word :
            curr += ord(lett) - 96
        print(curr)
        if curr > high : 
            high = curr
            final = word
    return final


print(ord('d') - 96)

print(high('man i need a taxi up to ubud'))