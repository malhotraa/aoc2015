import hashlib

def find(inp, prefix):
    i = 0
    while True:
        hsh = hashlib.md5("{}{}".format(inp, i).encode('utf-8')).hexdigest()
        if hsh.startswith(prefix):
            return i
        i+=1

print('part1:', find("bgvyzdsv", "00000"))
print('part1:', find("bgvyzdsv", "000000"))