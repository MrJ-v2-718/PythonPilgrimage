from hashlib import md5, sha1, sha224, sha256

text = input("Enter text to hash ('q' to quit): ")

algorithm = input('\nEnter algorithm (md5/sha1/sha224/sha256): ').lower()
if algorithm == 'md5':
    output = md5(text.encode('utf-8'))
elif algorithm == 'sha1':
    output = sha1(text.encode('utf-8'))
elif algorithm == 'sha224':
    output = sha224(text.encode('utf-8'))
elif algorithm == 'sha256':
    output = sha256(text.encode('utf-8'))
else:
    output = 'Invalid algorithm selection'

print(f'\nHash value: {output.hexdigest()}')

