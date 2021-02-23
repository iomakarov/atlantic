import datetime
import random
from progress.bar import IncrementalBar 
from collections import Counter
from threading import Thread
from multiprocessing import Process

d1 = datetime.date(1, 1, 1)
d2 = datetime.date(2020, 12, 31)
days = [d1 + datetime.timedelta(days=x) for x in range((d2-d1).days + 1)]
bdays = []
bar = IncrementalBar('Идет эксперимент', max = len(days))
xdays = []
for day in days:
    bar.next()
    bday = {}
    bday['d'] = day.strftime('%d')
    bday['m'] = day.strftime('%m')
    bdays.append(bday)
    xdays.append(day.strftime('%m%d'))
bar.finish()

c = Counter(xdays)
print(c['0229'])

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


cBdays = len(bdays)
cAtlantics = len(atlantics)

print(cBdays)
print(cAtlantics)


xCon = 0
countExperiment = 1000000000
print('-------------------------------')
print('-------------------------------')
print('-------------------------------')
#bar = IncrementalBar('Идет эксперимент', max = countExperiment)
for i in range(1,countExperiment+1):
    bday = bdays[random.randint(0,cBdays-1)]
    atlantic = random.randint(1,cAtlantics)
    if (isBD(atlantic, bday)):
        xCon+=1
    #bar.next()
    if (i%1000000==0 & i!=1):
        print('-------------------------------')
        print(xCon)
        print(i)
        res = xCon/i
        print(res)
        if (res != 0):
            print(1/res)
#bar.finish()

print('-----------FINAL--------------------')
print(xCon)
print(countExperiment)
res = xCon/countExperiment
print(res)
print(1/res)


