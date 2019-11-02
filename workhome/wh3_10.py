print ("Program 24h temperatur")

dane = "215021482120211921002076207620502065202020152010200520002001199319901950183417501744186019462010"

for time in list(range(0, 24)):
    lv_res = ""
    lv_res = lv_res + str(time) + ":00:\t"
    temp_string = dane[(time * 4):((time * 4) + 4)]
    temp_float = float(temp_string[:2] + "." + temp_string[2:])
    lv_res = lv_res + temp_string[:2] + "." + temp_string[2:] + "\u00b0" + "C"
    if temp_float <= 20.00:
        lv_res = lv_res + "\t!"
    else:
        pass

    if temp_float <= 18.5:
        lv_res = lv_res + "!"
    print(lv_res)
