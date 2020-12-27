def is_valid(passwd):
    for i in range(len(passwd)):
        if passwd[i] in ['i', 'o', 'l']:
            return False
    
    cnt = 0
    for i in range(ord('a'), ord('z') + 1):
        if chr(i)+chr(i) in passwd:
            cnt += 1
    
    if cnt < 2:
        return False

    valid = False
    for i in range(len(passwd)-2):
        ord_i = ord(passwd[i])
        ord_i_plus_1 = ord(passwd[i+1])
        ord_i_plus_2 = ord(passwd[i+2])
        valid = valid or ((ord_i_plus_1 == ord_i + 1) and (ord_i_plus_2 == ord_i + 2))

    return valid

def next_passwd(passwd):
    idx = len(passwd) - 1
    new_passwd = ''
    carry = True
    while idx >= 0 and carry:
        char = passwd[idx]
        if ord(char) + 1 > ord('z'):
            new_char = 'a'
            carry = True
        else:
            new_char = chr(ord(char) + 1)
            carry = False
        new_passwd = new_char + new_passwd
        idx -= 1

    new_passwd = passwd[:idx+1] + new_passwd
    return new_passwd

def part1(passwd):
    while not is_valid(passwd):
        passwd = next_passwd(passwd)
    return passwd

print('part1:', part1('hepxcrrq'))
print('part2:', part1(next_passwd('hepxxyzz')))