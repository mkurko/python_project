print("Program do rysowania prostokątu")
in_size=input("długość prostokąta: ")
in_hight=input(" szerokość prostokąta: ")

length = int(in_size)
width = int(in_hight)
print("+" + "-" * (length - 2) + "+")
i = 1
while i < (width-1):
    print("|" + " " * (length - 2) + "|")
    i += 1
print("+" + "-" * (length - 2) + "+")