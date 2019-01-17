import numpy as np

#   This program calculates the Prices of your Dimsum
#   based on the total price of the bill and 
#   how many dishes you have had!
#
#   At the moment, it only takes 2 sizes.
#   The next version will take 3 sizes.

def increment(price):
    price = price + 1
    return price

def dec(price):
    price = price - 1
    return price

def price_divide(price, number):
    ans = price / number
    return ans    
    
#def check_valid(s_price, m_price, l_price):
#   if (s_price <= m_price) and (m_price <= l_price):
#        return 1
#    else:
#        return 0


sm_price = 0.0
me_price = 0.0
run = 1

s_num = float(input('how many small did u get?'))
print(s_num)
m_num = float(input('how many medium'))
print(m_num)
#l_num = int(input('how many large'))
#print(l_num)
total = float(input('how much was it?'))

    #increment small price, until total price
    #increment med price, decrement small. med=total-small
    #keep going until small is lesser med

while (sm_price < total):
    sm_price = total
    print('$',sm_price)

while (run == 1):
    sm_price = dec(sm_price) #decrement small price.
    sm_1 = price_divide(sm_price,s_num) #find individual price
    me_price = total - sm_price #make sure these are floats!!
    med_1 = price_divide(me_price,m_num)
    
    if(np.floor(sm_1) >= np.floor(med_1)):
        run = 1
        continue
    elif(np.floor(sm_1) < np.floor(med_1)):
        run = 0
        break

print(sm_1,med_1)
        
        
        
        
    

