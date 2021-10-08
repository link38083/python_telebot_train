import binascii

def decode_pass(pass_list, bits):
    print(f"{int(bin(int.from_bytes(pass_list[0][0].encode(), 'big'))[2:]):08d}")
    b = (" ".join([f"{int(bin(int.from_bytes(n.encode(), 'big'))[2:]):08d}" for n in pass_list[0]]))
    if b == bits:
        return pass_list[0]
    else:
        return False

print(decode_pass(['password123', 'admin', 'admin1'], '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 00110010 00110011'))