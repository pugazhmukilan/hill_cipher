import numpy as np

#function for converting the number matrix to their respective alphabet matrix 
def matrix_to_letter(n):
    
    global  encry_string
    encry_string=''
    for i in n:
        for j in i:
            encry_string+=chr(j+97)
    return encry_string #final value 

    
    
# function for the encryption and decryption
def encryption(a,b):
    encry_l=[]
    for i in range(0,len(b),2):
        l=[]
        try:
            l += [ord(b[i])-97,ord(b[i+1])-97]
        except:
            l += [ord(b[i])-97,0]
        
        
        c=np.matmul(a,l)#multiplying the matrix to have the resultant encryptd matrix
        encry_l.append(c%26)#taking the mode of the the each array that has to be inserted into the matrix
    


    return matrix_to_letter(encry_l)# returns the another function in this function 




      

##main program starts here

msg=input("Enter the message for encryption : ")


#making the length of the msg even \
word_list=msg.split(" ")#spliting the sentence for ec=ncrypting and decrypting each word in the sentence

encrypted_message=''
decrypted_message=''

for i in word_list:
    length=len(i)
    if len(i)%2!=0:
        i=i+'a'
    else:
        pass
    randmat=np.array([[1,2],[1,3]])
    inv=np.linalg.inv(randmat)
    int_inv=inv.astype(int)
    
    encrypted_message+=" "+encryption(randmat,i)  #concatinating the encrypted string as one string
    decrypted_message+=" "+encryption(int_inv ,encry_string)[0:length]  # concatinating the decrypted string as one string 

print("encrypted message is :",encrypted_message)
print("decrypted message is  : ",decrypted_message)
