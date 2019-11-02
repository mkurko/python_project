print( "Program do sprawdzania roku przestępnego")


in_year = int(input("Podaj rok: "))
# if in_year in list(range(0,in_year+1,4)):
if in_year % 4 == 0 and (in_year % 100 != 0 or in_year % 400 == 0):
    print("Rok " + str(in_year) + " rok przestępny.")
else:
    print("Rok " + str(in_year) + " nie jest rokiem przestępnym.")
