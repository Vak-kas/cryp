ENC = 0;
DEC = 1;

def makeDisk(k1, k2):
    
    enc_disk = {}
    dec_disk = {}
    for i in range(26):
        enc_i = (i*k1+k2)%26
        enc_ascii = enc_i + 65
        enc_disk[chr(i+65)] = chr(enc_ascii);
        dec_disk[chr(enc_ascii)] = chr(i+65)


    return enc_disk, dec_disk


def affine(msg, key1, key2, mode):
    ret=''

    msg = msg.upper()
    enc_disk, dec_disk = makeDisk(key1, key2)

    if enc_disk is None:
        return ret
    
    if mode is ENC:
        disk = enc_disk

    if mode is DEC:
        disk = dec_disk

    for c in msg:
        if c in disk:
            ret+=disk[c]
        else:
            ret+=c;

    return ret;


def main():
    plaintext = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key1, key2 = 3, 5

    print("Original : \t%s" %plaintext.upper());
    ciphertext = affine(plaintext, key1, key2, ENC);
    print("Affine Cipher :\t%s" %ciphertext);
    deciphertext = affine(ciphertext, key1, key2, DEC);
    print("Deciphered:\t%s" %deciphertext);

if __name__ == "__main__":
    main();






