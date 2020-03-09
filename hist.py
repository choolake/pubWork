#!/usr/bin/env python3
'''
Print Data in a histogram format
'''
def main():
    outcomes = { 'Progress': 1, 'Trailing': 3, 'Retriver': 2,'Excluded': 1 }#Outcomes in a Dictionary
    print_dict(outcomes)

def print_dict(o):
    print(max(o.items())[1])
    #Prinitng Header
    for i in o.keys():
        print(i, end=' ',flush=True)
    print('')
    ##
    values=o.values()#get outcome count
    items=o.items() 
    for rownum in range(max(items)[1]):
        for value in values:
            #print(f'{rownum}<{value}', end='        ',flush=True)#for Verification
            if rownum < value : #if row number is less than the ooutcome count printing
                print('   *   ', end=' ',flush=True)
            else:
                print('       ', end=' ',flush=True)
        print('')
    #for key,value in o.items(): ##for verification
    #    print(f'{key}: {value}')

if __name__ == '__main__': main()