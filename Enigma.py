import PlugBoard
import Rotors
import Reflector


class Enigma:
    def __init__(self,reflector=Reflector.Reflector([]),r1=Rotors.Rotor([],""),r2=Rotors.Rotor([],""),r3=Rotors.Rotor([],""),pb=PlugBoard.PlugBoard()):
        self.pb=pb
        self.r1=r1
        self.r2=r2
        self.r3=r3
        self.reflector=reflector
    def encode(self,ch):

        ch=self.pb.encode(ch)
        
        ch=self.r3.encode_right_to_left(ch)
        
        ch=self.r2.encode_right_to_left(ch)
        
        ch=self.r1.encode_right_to_left(ch)
        
        ch=self.reflector.dic[ch]
        
        ch=self.r1.encode_left_to_right(ch)
        
        ch=self.r2.encode_left_to_right(ch)
        
        ch=self.r3.encode_left_to_right(ch)

        ch=self.pb.encode(ch)
        if  self.r3.dic["A"]==self.r3.noche:
            self.r3.turn()
            self.r2.turn()
            return ch
        if  self.r2.dic["A"]==self.r2.noche:
            self.r3.turn()
            self.r2.turn()
            self.r1.turn()
            return ch
        self.r3.turn()
        return ch
    def encodeStr(self,str0):
        str1=""
        for c in str0:
            str1+=self.encode(c)
        return str1