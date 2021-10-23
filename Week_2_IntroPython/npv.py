def npv (cashflows,r,initial_investment):
    sum_of_cf=0
    for i in range(0,len(cashflows)):
        current_cf = round(cashflows[i]/(1+r)**(i+1),2)
        sum_of_cf=sum_of_cf+current_cf
    npv = sum_of_cf-initial_investment
    if npv > 0:
        print("profitable by {}".format(npv))
    elif npv < 0:
        print("not profitable by {}".format(npv))
    else:
        print("breakeven")