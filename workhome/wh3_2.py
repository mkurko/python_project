print("program, który poda pierwsza i ostatnia cyfre podanej liczby")

in_number = input("Liczba: ")
#in_number=str(-252552)
flg_if_valid = in_number.lstrip('-+').isnumeric()
if flg_if_valid:
      print ("Ok liczymy....")
else:
        print("... kończe bo to zła liczba była")
        exit(1)

ln_length = len(in_number);
print ("dlugosc liczby: " + str(ln_length))

if int(in_number) > 0:
    print ("Początek:"+in_number[0])
else:
    print("Początek:" + in_number[1])

print ("Koniec:"+in_number[-1:])

# print("Podano poprawnie liczbę: " + in_number)
# if int(in_number) > 9 or int(in_number) < -9:
#     print("Podano: " + in_number)
#     print(
#         "Pierwsza cyfra to: " + in_number.lstrip('-')[0] + ", druga cyfra to: " + in_number.lstrip('-')[
#             -1])
# else:
#     print("Podano tylko jedną cyfrę. Pierwsza i ostatnia cyfra to zatem: " + in_number.lstrip("-"))
#
