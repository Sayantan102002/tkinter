from colorama import init 
from termcolor import colored 
init() 
l1=[]
l2=[]
d=0
t=0
y=0
print()
a1=colored(' ----------------------------------------- ','red')
b1=colored(' | DEVELOPED BY --> Sayantan Chakraborty | ','red')
c1=colored(' |          Ph. No.- 7908 375 185        | ','red')
d1=colored(' ----------------------------------------- ','red')
print('                   '+a1)
print('                   '+b1)
print('                   '+c1)
print('                   '+d1)
print()
print(colored('                              AD VALOREM COURT FEES','green'))
print(colored('                              ---------------------','yellow'))
print(colored('  [Fees for West Bengal are taken from W.B.C.F. (Amendment) Act. 2002 dt. 31.12.2002]','green'))
def createList1(r1, r2,k): 
    return [item for item in range(r1, r2+100,k)] 
def createList2(r1, r2,k): 
    return [item for item in range(r1, r2+1,k)]  
def courtfees():
    global l1
    global l2
    l1=createList1(1,7500,100)
    l1+=createList1(7751,10000,250)
    l1+=createList1(10501,20000,500)
    l1+=createList1(21001,50000,1000)
    l1+=createList1(55001,300001,5000)
    l2+=createList2(10,100,10)
    l2+=createList2(108,620,8)
    l2+=createList2(636,780,16)
    l2+=createList2(810,1380,30)
    l2+=createList2(1430,2880,50)
    l2+=createList2(3230,6380,350)
    l2+=createList2(6750,13780,370)
    l2+=createList2(13990,17980,210)
    # print(l1,'\
    l2+=createList2(13990,17980,210)
    # print(l2)
# courtfees()
def calculation(a):
    courtfees()
    global d
    global t
    i=0
    for i in range(len(l1)):
        if a>=l1[i] and a<l1[i+1] and a<=300000:
            return (l2[i])
        elif a>300000:
             t=a-300000
             d=t//10000
            #  print(d)
             if d!=0 and (t%10000)==0:
              return(17980+(d*100))
             elif d!=0 and (t%10000)!=0:
              return(17980+(d*100)+100)
             elif t>=1 and t<=10000:
              return(17980+100)
             else:
              return(17980+(d*100))
def min():
    n=0
    o=0
    while 1:
        global y
        print()
        print(colored('  Enter suit value for assessment of Court Fees:- ','green'),'\n')
        print('  Rs. ',end='')
        try:
            n=float(input())
            o=calculation(n)
        except ValueError:
            print()
            y=1
        if y==1:
            print(colored('  Only numbers are accepted.','red'),'\n')
            y=0    
        elif o>50000: 
            print()
            print(colored('  Maximum amount of Court Fees to be paid Rs. '+str(50000),'red'),'\n')
            y=0        
        else:    
            y=0
            z=calculation(n)
            print()
            print(colored('  Court Fees to be paid: Rs.'+str(z),'red'))
            print()
        print(colored('               ----------------------------- END -----------------------------','green'))
        print()
min()