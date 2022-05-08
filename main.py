import PlugBoard
import Rotors
import string
import Reflector
import Enigma

# print(list(string.ascii_lowercase))
pb=PlugBoard.PlugBoard()
# print(pb.dic)
# print(str('A'+1))
Beta=Rotors.Rotor(["L","E","Y","J","V","C","N","I","X","W","P","B","Q","M","D","R","T","A","K","Z","G","F","U","H","O","S"],"Q")
Gamma=Rotors.Rotor(["F","S","O","K","A","N","U","E","R","H","M","B","T","I","Y","C","W","L","Q","P","Z","X","V","G","J","D"],"E")
I=Rotors.Rotor(["E","K","M","F","L","G","D","Q","V","Z","N","T","O","W","Y","H","X","U","S","P","A","I","B","R","C","J"],"Q")
II=Rotors.Rotor(["A","J","D","K","S","I","R","U","X","B","L","H","W","T","M","C","Q","G","Z","N","P","Y","F","V","O","E"],"E")
III=Rotors.Rotor(["B","D","F","H","J","L","C","P","R","T","X","V","Z","N","Y","E","I","W","G","A","K","M","U","S","Q","O"],"V")
IV=Rotors.Rotor(["E","S","O","V","P","Z","J","A","Y","Q","U","I","R","H","X","L","N","F","T","G","K","D","C","M","W","B"],"J")
V=Rotors.Rotor(["V","Z","B","R","G","I","T","Y","U","P","S","D","N","H","L","X","A","W","M","J","Q","O","F","E","C","K"],"Z")
A=Reflector.Reflector(["E","J","M","Z","A","L","Y","X","V","B","W","F","C","R","Q","U","O","N","T","S","P","I","K","H","G","D"])
B=Reflector.Reflector(["Y","R","U","H","Q","S","L","D","P","X","N","G","O","K","M","I","E","B","F","Z","C","W","V","J","A","T"])
C=Reflector.Reflector(["F","V","P","J","I","A","O","Y","E","D","R","Z","X","W","G","C","T","K","U","Q","S","B","N","M","H","L"])


pb.plugLead("AG")
enigma=Enigma.Enigma(A,I,II,III,pb)
print("pb is=",pb.dic)
print("the III values=",III.dic)
print("the II values=",II.dic)
print("the I values=",I.dic)
print("the ref values=",A.dic)


#WHILE TO DEBUG THE ROTORS HOW THEY ROUND
# while(True):
#     ch=input("enter input")
#     enigma.encode(ch)
#     print("the III values=",III.dic.values())
#     print("the II values=",II.dic.values())
#     print("the I values=",I.dic.values())

encruptedStr=enigma.encodeStr("MKYBYCGLJLRDGL")
print(encruptedStr)