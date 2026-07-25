def total_calc (bill_amount,tip_perc):
    total = bill_amount + tip_perc* 0.01
    print(f"Please pay BDT {total} ")

total_calc(575,10)