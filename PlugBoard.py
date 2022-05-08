import string
class PlugBoard():
    def __init__(self):
        self.plugCount=0
        
        self.dic={}
        for ch in list(string.ascii_uppercase):
            self.dic[ch]=ch
            
        
    def encode(self,c):
        return self.dic[c]
    
        
    def plugLead(self,str1):
        if str1[0]==str1[1]:
            return
        if self.plugCount==10:
            print("the plug is fully, no place any more")
            return
        if self.dic[str1[0]]!=str1[0]:
            print (f"error plug, -{str1[0]}- is conected already")
            return
        if self.dic[str1[1]]!=str1[1]:
            print (f"error plug, -{str1[1]}- is conected already")
            return
        self.dic[str1[0]]=str1[1]
        self.dic[str1[1]]=str1[0]
        self.plugCount+=1
    def unPlugLead(self,str1):
        if str1[0]==str1[1]:
            return
        if self.dic[str1[0]]==str1[1] and self.dic[str1[1]]==str1[0]:
            self.dic[str1[0]]=str1[0]
            self.dic[str1[1]]=str1[1]
            self.plugCount-=1
        else:
            print("there is no plug like this")


