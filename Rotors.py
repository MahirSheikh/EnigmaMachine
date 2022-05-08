import string

class Rotor:
    def __init__(self,dic=[],noche=""):
        i=0
        self.dic={}
        self.noche=noche
        if dic==[]:
            return
        for ch in list(string.ascii_uppercase):
            self.dic[ch]=dic[i]
            i+=1
        
    def encode_left_to_right(self,ch):
        for k,v in self.dic.items():
            if v==ch:
                return k
    def encode_right_to_left(self,ch):
        return self.dic[ch]
    def turn(self):
        letters=list(string.ascii_uppercase)
        tmp=self.dic["A"]
        for i in range(25):
            self.dic[letters[i]]=self.dic[letters[i+1]]
        self.dic["Z"]=tmp
    def PutPosition(self,ch):
        while self.dic["A"]!=ch:
            self.turn()
            



