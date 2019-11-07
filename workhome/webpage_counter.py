# with open("moj_plik.txt", "r+") as plik:

    # plik.write("Kolejna linia - z programu")
    # print( plik.readline())
    # plik.seek(0, 0)
    # plik.truncate(0)
    # line = plik.readline()

# with open("counter.txt", "r") as f:
#     count = f.read()
#     n = int(count)
#     print (f"Jesteś już {count} dzisiaj")
#
# with open("counter.txt", "w") as f:
#     f.write(str(n + 1))
#     f.close()

with open("counter.txt", "r+") as f:
    count = f.read()
    n = int(count)
    print (f"Jesteś już {count} dzisiaj")
    f.seek(0)
    # f.truncate(0)
    f.write(str(n + 1))
