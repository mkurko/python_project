print ("Program do rysowania piramidy")


ln_pyr_val = int(input("Podaj wielkość piramidy: "))

ln_pyr_val = int(ln_pyr_val)
i = 1
lv_pyr_len = range(1, 2 * ln_pyr_val, 2)
print (lv_pyr_len)
while i <= ln_pyr_val:
    print(" " * (ln_pyr_val - i) + "#" * lv_pyr_len[(i - 1)])
    i += 1
