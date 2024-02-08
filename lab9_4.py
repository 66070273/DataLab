'''Calculator V2'''
def main(cal, total):
    '''print result'''
    if cal == 1:
        total = 1
    else:
        for i in range(len(str(cal))):
            if i == len(str(cal)) - 1:
                total += (cal - (10**i)) * ((len(str(cal))) + 1)
            else:
                total += (9 * (10**i)) * (len(str(10**i))+1)
        total += len(str(cal)) + 1
    return total
print(main(int(input()), 0))