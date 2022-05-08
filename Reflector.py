import string

class Reflector:
    def __init__(self,dic=[]):
        i=0
        self.dic={}
        if dic==[]:
            return
        for ch in list(string.ascii_uppercase):
            self.dic[ch]=dic[i]
            i+=1
def encode(self,ch):
    return self.dic[ch]