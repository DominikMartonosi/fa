import random

file=open('fa.txt','w')

fakitermelés=[]

dátum=20

for i in range(0,31):
    fakitermelés.append(random.randrange(50,101))

print('')

legnagyobb=0
legnagyobb=fakitermelés[0]
for nap in fakitermelés:
    if nap > legnagyobb:
        legnagyobb=nap
print(f'{legnagyobb}m3 volt a legnagyobb termelés!')
file.write(f'{legnagyobb}m3 volt a legnagyobb termelés!\n')

legkisebb=0
legkisebb=fakitermelés[0]
for nap in fakitermelés:
    if nap < legkisebb:
        legkisebb=nap
print(f'{legkisebb}m3 volt a legkevesebb termelés!')
file.write(f'{legkisebb}m3 volt a legkevesebb termelés!\n')

print('')
alkalom = 0
for i in range(0,len(fakitermelés)):
    if fakitermelés[i] > 82:
        alkalom+=1
print(f'{alkalom} alkalommal volt több a napi termelésmint 82m3!')

print(f"{dátum}. -án : {fakitermelés[dátum+1]}m3 fát termeltek!")
file.write(f'{dátum}. -án : {fakitermelés[dátum+1]}m3 fát termeltek!\n')

átlag = 0
for i in range(0,len(fakitermelés)):
    átlag = átlag+fakitermelés[i]
átlag = átlag/len(fakitermelés)

print(f'{átlag} volt az átlag fa termelés!')
file.write(f'{átlag} volt az átlag fa termelés!\n')