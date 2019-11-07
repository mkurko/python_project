import pickle
# #
# entries = [ #lista!
#     {"title": "fasfafs", "body": "fdfsf","imie": "fadam"} #słownik!
# ]
# with open('filename.pickle','wb') as book_file:
#     pickle.dump(entries, book_file)
# #

# with open('book.pkl','rb+') as book_file:
#     pickle.dump(entries, book_file)
#     book_file.seek(0)
#     data = pickle.load(book_file)
#     print(len(data))





# with open('book2.pkl','rb+') as book_file:
# #     pickle.dump(entries, book_file)
# 
#     data = pickle.load(book_file)
#     print("ILOŚC LINI w knidze:" + str(len(data)))
#     book_file.seek(len(data))
#     pickle.dump( {"title": "fasfafs", "body": "fdfsf","imie": "fadam"},book_file)
#     pickle.dump( {"title": "fasfafs", "body": "fdfsf","imie": "fadam"},book_file)


def wprowadz_dane():
    ln_tyt = "afa"  # input("podaj tytuł: " )
    ln_tre = "tresdfsdfsdfsd"  # input("podaj tresc: " )
    ln_imie = "mario"  # input("podaj imie: " )
    new_dict = {"title": ln_tyt, "body": ln_tre, "imie": ln_imie}
    return new_dict


def policz_liczbe_wierszy(x):
    return len(x)

new_dict = wprowadz_dane()

with open('filename.pickle', 'rb+') as pfile:
    data = pickle.load(pfile)
    # print ("na początku: " + str(len(data)))
    # print(data)
    data.append(new_dict)
    # print(data)
    # print(new_dict)
    pfile.seek(0)
    pickle.dump(data, pfile)

counter = policz_liczbe_wierszy(data)

print("ILOŚC LINI w knidze na końcu:" + str(counter))