class CaesarCipher:
    def __init__(self, cip):
        # verify the cipher is non-punctuated and all uppercase
        self.cip = re.sub('[^A-Z]', '', cip.upper())
        self.alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    def inputValidation(self) -> str:
        shift = input('enter an alpha character to shift by: ').upper()
        while shift:
            if ord(shift) > 90 or ord(shift) < 65:
                shift = input('Please enter an alpha character, between a and z, to shift by: ').upper()
                if shift.isalpha():
                    break
        return shift
        # cipher = input('enter an alpha based encrypted message for decryption')

    def ccipher(self) -> str:
        strs: str = ''

        shift: str = self.inputValidation()

        for char in self.cip:
            q = ord(char) - (ord(self.cip[0]) - ord(shift))
            if q < 65:
                strs += self.alpha[q - 65]
            else:
                strs += chr(q)
        return strs

cip = list('MEMYQZFADUZAIGZPQDEFMZPFTMFAZQOMZEGOOQQPUZAGDBDARQEEUAZUZYMZKIMKEEAYQEFGPQZFEMDQITUBEYMDFBDANXQYEAXHQDEFTUZWBGFZMYRQXXAIEMZPUYAYQPMXUEFEEAYQEFGPQZFETMHQMFTUDEFRADWZAIXQPSQXQMDZUZSQHQDKFTUZSFTQKOMZEAYQEFGPQZFETMHQFTQSURFARODQMFUHUFKEAYQEFGPQZFETMHQMWZMOWRADFDMZEBADFUZSUYBADFMZFUPQMERDAYAZQEGNVQOFFAMZAFTQDEAYQEFGPQZFETMHQFTQMNUXUFKFAMEWFTQDUSTFCGQEFUAZMFFTQDUSTFFUYQAROAGDEQEAYQEFGPQZFEEUYBXKIADWHQDKHQDKTMDP')

cc: CaesarCipher = CaesarCipher(cip)
print(cc.ccipher())
