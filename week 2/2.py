'''
i = 0
while i < 50:
    coin = int(input('insert the coin: '))
    if coin % 5 != 0 or coin < 0:
        continue
    else:
        i += coin
    
    if i > 50:
        print('yr change is:', i - 50)
        
 '''       

def main():
    coke_machine()

def ur_change(i):
    return ('change:', i - 50)
    

def coke_machine():
    i = 0
    while i < 50:
        coin = int(input('insert thr coin: '))
        if coin % 5 != 0 or coin < 0:
            continue
        else:
            i += coin
        
        if i > 50:
            ur_change()

main()