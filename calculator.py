#!/usr/bin/env python3

import sys

print(sys.argv)


if __name__ == '__main__':
    #print(sys.argv)
    #print("以上两行为测试")
    try:
        salary = float(sys.argv[1])
    except:
        print("Parameter Error")
    	
    start = 3500
    print("shouru",salary)
    if salary > start: 
        a= salary - start
    else:
        a = 0
  
    tax = 0
    tax1=0
    if a > 80000:
        tax = 0.45
        tax1 = 13505
    elif a > 55000:
        tax = 0.35
        tax1 = 5505
    elif a >35000:
        tax = 0.30
        tax1 = 2755
    elif a > 9000:
        tax = 0.25
        tax1 = 1005
    elif a > 4500:
        tax = 0.2
        tax1 = 555
    elif a > 1500:
        tax =0.1
        tax1 = 105
    else:
        tax = 0.03
        tax1 = 0
a = format(a * tax - tax1,'.2f')
print('shui-jin',a)
#print('shui-lv',tax)
#print('kouchushu',tax1)



        
