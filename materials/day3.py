#ln_lat=input("podaj liczbe lat: " )
#ln_ilosc=input("podaj liczbe zwierzat: " )

ln_lat=2
ln_ilosc=5

zdanie="ala ma " + str(ln_lat)

zdanie= f"ala ma  {ln_lat}"

zdanie="ala ma {}".format(ln_lat)

zdanie="ala ma {a}".format(a=ln_lat)
print(zdanie)



liczba=1.4242

print (str(liczba))
print ("liczba %s"% liczba)
print ("liczba %1.1f"% liczba)

zdanie='abcdefg'
print (zdanie[1:3])
print (zdanie[:2])
print (zdanie[::-1])
print (zdanie[-3:])

if 1 == 2:
    print("if")
elif 2 == 'w':
    print ("elif")
else:
    print("else")
#
#
# var=3
# if (var%2)==0:
#     print("odd")
# else:
#     print("not")
#
# print (4//4)

var=3
print ("podzielna przez ")
if var%3==0 and var%5==0:
    print("3i5")
elif var%3==0:
    print ("3")
else:
    print("ni")

liczby_parzyste=range(0,20,2)
print (list(range(0,20,2)))
print (tuple(range(0,20,2))) #krotka jest niemutowalna czyli nie mozna zmieniac tam wartosci


#IMPORTANT !!!

lista=list('abc', 'fafs')
lista=list('abc')
print (lista) # ['a', 'b', 'c']
lista=['abc']
print (lista) #['abc']


while True:
    print (123)
    break