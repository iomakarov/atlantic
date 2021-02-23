import math
from termcolor import colored
simple = []
simple.append(1)
i = 1
l = 1
lmax = math.pow(14,2)
while (l != lmax):
    i+=1
    isSimple = True
    for j in range(2,i):
        if (i%j == 0):
            isSimple = False
    if (isSimple):
        simple.append(i)
    l = len(simple)



#for i in range(0,l):
#    print(simple[i])

n = math.ceil(math.sqrt(l))

for i in range(0,n):
    print('')
    for j in range(0,n):
        #if ()
        #print(colored('Файл успешно прочтен','green')
        if (i*n+j < l):
            color = 'white'
            if (simple[i*n+j]==463):
                color = 'red'
            if ((i == j) & (i == (n//2))):
                color = 'green' 
            print(colored(str(simple[i*n+j])+' ',color), end='')
print()
print(l)
print(n)