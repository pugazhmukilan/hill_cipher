# hill_cipher

This Python code contains a program that encrypts and decrypts a message using a 2x2 matrix. The project aims to demonstrate the basic concept of matrix encryption and decryption.

The matrix_to_letter function takes a matrix of numbers as input and returns a string consisting of corresponding alphabet characters. The encryption function takes two inputs, a 2x2 matrix a and a string b to be encrypted. It splits the input string into pairs of two characters and converts them to a matrix of numbers. Then it multiplies the matrix with the given 2x2 matrix a to generate the encrypted matrix. Finally, it takes the modulus of each element in the encrypted matrix with 26 and appends the resulting numbers to a list. The matrix_to_letter function is called with this list to return the final encrypted string.

In the main program, the user is prompted to enter a message to be encrypted. The program splits the input message into words and encrypts and decrypts each word individually. If the length of a word is odd, an extra character 'a' is added to make it even. A random 2x2 matrix is generated to be used as the encryption key for each word. The encrypted and decrypted strings for each word are concatenated and displayed to the user.

The project can be improved by adding more encryption and decryption techniques and allowing the user to choose the encryption technique to be used. It can also be extended to encrypt and decrypt longer messages, handle punctuation, and support multiple encryption keys for a single message. The code can be documented better with appropriate comments and function descriptions for ease of understanding.
