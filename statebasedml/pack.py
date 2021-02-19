from copy import copy

def strpacker(string):
    i = 0
    packer = {}
    for x in string:
        if x not in packer:
            packer[x] = copy(i)
            i += 1
    return packer

def strpack(string,packer):
    pack_int = 0
    mult = len(packer)
    for i in range(len(string)):
        assert string[i] in packer, "All chars in the string must be in the packer"
        pack_int = pack_int*mult + packer[string[i]]
    pack_str = ""
    print(pack_int)
    while pack_int > 0:
        pack_str += chr(pack_int%256)
        pack_int = pack_int // 256
    return pack_str

def strunpack(string,packer):
    inv_packer = {}
    for x in packer:
        inv_packer[packer[x]] = x
    assert len(packer) == len(inv_packer), "Something is wrong with this packer"
    pack_int = 0
    rev_string = string[::-1]
    for i in range(len(string)):
        pack_int = pack_int*256+ord(rev_string[i])
    print(pack_int)
    unpack_str = ""
    mult = len(packer)
    while pack_int > 0:
        unpack_key = pack_int%mult
        unpack_str += inv_packer[unpack_key]
        pack_int = pack_int // mult
    return unpack_str[::-1]