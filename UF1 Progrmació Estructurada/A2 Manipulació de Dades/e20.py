euros2=0
euros1=0
cts50=0
cts20=0
cts10=0

monedes=float()
cuenta=monedes.split()
TotalEu= euros1+euros2
Totalcts= cts10+cts20+cts50
for i in cuenta:
    if i == 2:
        euros2=euros2+1
    elif i == 1:
        euros1=euros1+1
    elif i == 0.5:
        cts50=cts50+1
    elif i == 0.2:
        cts20 = cts20 +1
    else:
        cts10 = cts10 +1
