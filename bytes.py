
def shifr(s):
    encoding_string=s.encode(encoding='utf-8')
    print('Bytes string: ', encoding_string)
    for bytes in encoding_string:
        print(bytes, end=',')
def deshifr(d):
    string=[]
    for i in range(len(d)):
        try:
            a=chr(int(d[i]))
        except ValueError:
            print(d[i], 'Invalid data type, it will not be processed')
        else:
            string.append(a)
    print('\nOriginal string: ', string)
shifr(input('Enter what you want to encrypt: '))
deshifr(input('\nEnter what you want to decrypt: ').split())
