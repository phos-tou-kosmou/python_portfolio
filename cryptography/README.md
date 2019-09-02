# Caesar Cipher
###### Python object to find key for encrypted cipher

The class is instantiated like so:

```
newCC: CaesarCipher = CaesarCipher('FDSJKAFDJS')
```

which yields a new CaesarCipher object with type of
CaesarCipher

There are two methods that come with it currently.

First is the inputValidation method, 
which ensures the input is solely upper case 
alpha elements.

```i.e. ascii values of 90-65```

Second the ccipher method, which returns the result 
of mapping each element to a shifted alphabet 
according to the user's input.

At first the shifting was done manually but
was not too difficult, because the letter 'A' is
the shift key for the included cipher.