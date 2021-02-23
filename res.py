years = 2020
vyears = years/400*97
xdays = vyears*366 + (years-vyears)*365
vWd = vyears/xdays
vnWd = (years)/xdays
print(years)
print(vyears)
print(str(vWd))
print(str(vnWd))
res = 9/888*vnWd*4 + 35/888*vnWd*3 + (155-1)/888*vnWd*2 + (251-1+1)/888*vnWd + 2/888*vWd
print(res)
print(1/res)
