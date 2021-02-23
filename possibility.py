import datetime
import random
import os
from progress.bar import IncrementalBar 

d1 = datetime.date(2020, 1, 1)
d2 = datetime.date(2020, 12, 31)
days = [d1 + datetime.timedelta(days=x) for x in range((d2-d1).days + 1)]
bdays = []
bar = IncrementalBar('Идет эксперимент', max = len(days))
for day in days:
    bar.next()
    bday = {}
    bday['d'] = day.strftime('%d')
    bday['m'] = day.strftime('%m')
    bdays.append(bday)

bar.finish()

atlantics = range(1, 889)

def isBD(num, bday):

    dWithoutFirst0 = str(int(bday['d']))
    mWithoutFirst0 = str(int(bday['m']))
    if (str(num)==bday['d']+mWithoutFirst0):
        return True 
    if (str(num)==dWithoutFirst0+bday['m']):
        return True        
    if (str(num)==dWithoutFirst0+mWithoutFirst0):
        return True    
    if (str(num)==mWithoutFirst0+bday['d']):
        return True 
    if (str(num)==bday['m']+dWithoutFirst0):
        return True        
    if (str(num)==mWithoutFirst0+dWithoutFirst0):
        return True    

    return False

bdaysAtlantic = {}
indir = os.path.dirname(os.path.abspath(__file__))
fout = open(indir + '/result.txt', 'w')


for num in atlantics:
    fout.write(str(num) + '\n')
    bdaysAtlantic[num] = 0
    for bday in bdays:
        if (isBD(num, bday)):
            fout.write('m: ' + bday['m'] + ' d: '+ bday['d']+ '\n')
            bdaysAtlantic[num]+=1

fout.close()

i0 = 0
i1 = 0
i2 = 0
i3 = 0
i4 = 0
for i in bdaysAtlantic:
    if (bdaysAtlantic[i]==0):
        i0+=1
    if (bdaysAtlantic[i]==1):
        i1+=1
    if (bdaysAtlantic[i]==2):
        i2+=1
    if (bdaysAtlantic[i]==3):   
        i3+=1
    if (bdaysAtlantic[i]==4):
        i4+=1

print('----------')
print(bdaysAtlantic[229])
print(bdaysAtlantic[292])
print('----------')
print(i0)
print('----------')
print(i1)
print(i2)
print(i3)
print(i4)
print('----------')
print(i1+i2+i3+i4)
print('----------')