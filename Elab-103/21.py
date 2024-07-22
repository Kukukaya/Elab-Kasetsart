def nb_year(p0, percent, aug, p):
    n_day = 1
    amount = int(p0+p0*percent/100+aug)
    while(p>amount):
        #print(amount)
        amount = int(amount+amount*percent/100+aug)
        n_day+=1
    return n_day

print( nb_year(1500000, 0.25, 1000, 2000000) )