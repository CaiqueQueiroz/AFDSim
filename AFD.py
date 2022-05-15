# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

E = [str(x) for x in input("\n Digite os estados\n").split() ]
Sigma = [str(x) for x in input("\n Digite o alfabeto \n").split()]
n = int(input("Digite o numero de transições"))
Delta = {'e': 'e'}
while ( n != 0):
    o, c, d = [str(x) for x in input("\n Digite as transições \n").split(',')]
    Delta[o, c] = d
    n = n - 1
i = input("Digite o estado inicial")
F = [str(x) for x in input("\n Digite os estados finais \n").split()]
Cadeia = [str(x) for x in input("\n Digite as palavras teste \n").split()]
EA = i
ca = 0
while (ca < len(Cadeia)):
    if Cadeia[ca] in Sigma:
        EA = Delta[EA, Cadeia[ca]]
    else:
        EA = Delta['e']
        break
    ca = ca + 1
if EA in F:
    print("S")
else: 
    print("N")
# E = ['i','q1','q2']
#Sigma = ['0','1']
#Delta = {('i','0'): 'i', ('i', '1'): 'q1', ('q1','0'): 'q2', ('q1','1'): 'q1', ('q2','0'): 'q1', ('q2','1'): 'q1',
#         ('e','0'): 'e', ('e','1'): 'e'}
#F = ['q1']




