def func(time,place,curr_loc,amount,type,merchant,any_invalid,any_recurr_debits):
    if time=="Morning"and place in['Mumbai','Delhi'] and curr_loc=='Delhi' and amount<100000 and type=='Debit' and merchant=='Safe' and any_invalid=='No' and any_recurr_debits=='No':
        return True
    elif time=="Eve"and place in['Delhi'] and curr_loc=='Delhi' and amount<100000 and type=='Debit' and merchant=='Safe' and any_invalid=='No' and any_recurr_debits=='No':
        return True
    elif time=="Night"and place in['Delhi','Mumbai'] and curr_loc==['Delhi','Mumbai'] and amount<100000 and type=='Debit' and merchant==['Safe','Doubt'] and any_invalid==['No','Yes'] and any_recurr_debits==['No','Yes']:
            return False
    else:
        return False
    
