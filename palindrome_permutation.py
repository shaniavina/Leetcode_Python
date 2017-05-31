from collections import Counter
def palindrome_permu1(str):
    str = str.lower()
    check = {}
    count = 0
    
    for s in str:
        if s == ' ':
            check[s] = 1
            continue
        if s not in check:
            check[s] = 1
            count += 1
        else:
            check[s] += 1
            if not check[s] % 2:
                count -= 1
            else:
                count += 1 
    return count <= 1

def palindrome_permu2(str):
    str = str.lower()
    #####whitespace significant
    return sum(v % 2 for v in Counter(str).values()) <= 1

def palindrome_permu3(str):
####bitvector
#####whitespace significant
    str = str.lower()
    bit_vec = 0
    for s in str:
        index = ord(s) - ord('a')
        print(index)
        mask = 1 << index
        print(mask)
        if (bit_vec & mask) == 0:
            bit_vec |= mask
        else:
            bit_vec &= ~mask
        print(bit_vec)
    return (bit_vec - 1) & bit_vec == 0

def main():
    str = 'tact coA'
    a = palindrome_permu3(str)
    print(a)

if __name__ == '__main__':
    main()
