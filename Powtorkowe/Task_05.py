alfabet = 'aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż'
ALFABET = 'AĄBCĆDEĘFGHIJKLMNŃOÓPQRSŚTUVWXYZŹŻ'


# create an encryption function
def encrypt(txt, key):
    encrypted = ""
    for character in txt:
        if character.isupper():
            indx = ALFABET.find(character)
            encrypted += ALFABET[(indx + key) % len(ALFABET)]
        else:
            indx = alfabet.find(character)
            encrypted += alfabet[(indx + key) % len(alfabet)]
    return encrypted


# create a decryption function
def decrypt(txt, key):
    decrypted = ""
    for character in txt:
        if character.isupper():
            indx = ALFABET.find(character)
            decrypted += ALFABET[(indx - key) % len(ALFABET)]
        else:
            indx = alfabet.find(character)
            decrypted += alfabet[(indx - key) % len(alfabet)]
    return decrypted


# create of the Caesar Cipher function
def cezar(text, key, function=encrypt):
    replacement = text.split()
    new_list_ = []
    for word in replacement:
        new_list_.append(function(word, key))
    return ' '.join(new_list_)


def main():
    print("Encrypted text:", cezar('ZuZa Będąwska', 3, encrypt))
    print("Decrypted text:", cezar('AxAc Dhfćzumc', 3, decrypt))


if __name__ == '__main__':
    main()
