
''' A simple checksum utility for windows developed using Python3 and hashlib by M.Anish only.
   This program uses certutil in windows so no use of third party software inorder to  reduce security risks.'''
   
import os                                                                
import hashlib
import platform

def sha3(file,txt):
      if platform.python_version().lower()<'3.6.0':
        print('\nSorry, This function will not work for this platform!\n')
        x=input()
        exit(1)
      limit=1024
      if txt=='256':
        v=hashlib.sha3_256()
      else:
        v=hashlib.sha3_512()
      with open(file,'rb+') as f:
          buff=f.read(limit)
          v.update(buff)
          while len(buff)>0:
              buff=f.read(limit)
              v.update(buff)
      d=str(v.hexdigest())
      print(d)
      if txt=='256':
        with open(file+'_sha3_256.txt','w') as k:
            k.write(d)
    
      else:
        with open(file+'_sha3_512.txt','w') as k:
            k.write(d)
      
print("\n\t-----PywinHash: A Simple checksum utility------")
print("\nEnter Filename:")
y=input()
if os.path.exists(y)==False:
    print('ERROR: FILE NOT FOUND!')
    y=input()
    exit(1)
os.system("cls")

print("\n\t-----Supported Hash Algorithms---")
print('\n>Insecure Hash Algorithms supported:-')                    
print('MD5')
print('SHA1')
print('\n>Secure Hash Algoritms supported:-')
print('SHA256')
print('SHA384')
print('SHA512')
print('SHA3_256')
print('SHA3_512')
print('\n\nEnter Hash Algorithm:')
x=input()
x=x.lower()
if(x=='sha256'):
   os.system("certutil -hashfile "+y+" sha256>>sha256.txt")
elif(x=='sha512'):
   os.system("certutil -hashfile "+y+" sha512>>sha512.txt")
elif(x=='sha1'):
   os.system("certutil -hashfile "+y+" sha1>>sha1.txt")
elif(x=='md5'):
   os.system("certutil -hashfile "+y+" md5>>md5.txt")
elif(x=='sha384'):
   os.system("certutil -hashfile "+y+" sha384>>sha384.txt")
elif(x=='sha3_256'):
   sha3(y,'256')
elif(x=='sha3_512'):
   sha3(y,'512')
else:
   print("\tHash Algorithm not supported!")
x=input()
       
       
     




