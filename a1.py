import tsc2
from datetime import date
from colorama import init 
from termcolor import colored 
init() 
tax=0
w=0
m=0
x=0
a=0
global n
c=0
print()
# def date___time():
d=date(2020,5,30)
t=date.today()
z=(d-t).days
# print(z)
# def expire():
#       while 1:
#         notification.notify(
#         title='Your license is going to expire on 14.05.2020',
#         message='For renewal contact the developer',
#         app_icon="C:/Users/Sayantan/Desktop/python projects/favicon.ico",
#         timeout=10
#     )    
#         time.sleep(5)
def license():
#t=True
# def f():
#    global w
#    while w!='YES' and w!='NO':
#      print(colored('  Do you want to add amount:(yes or no)')
#      print('--> ',end='')
#      k=input()
#      k=k.upper()
#      print()
#      if k=='YES':
#           print(colored('  Enter the amount:')
#           print(colored('  Rs. ',end='')
#           a=float(input())
#           m=tsc2.cal(a)
#           print(colored('  Rs.',m)
#           break 
#      elif k=='NO':
#           break
#      else:
#           print(colored('  Only yes or no is accepted')
#           print(colored('  Try Again')
#           print()
   a1=colored(' ----------------------------------------- ','red')
   b1=colored(' | -:DEVELOPED BY:- Sayantan Chakraborty | ','red')
   c1=colored(' |          Ph. No.- 7908 375 185        | ','red')
   d1=colored(' ----------------------------------------- ','red')
   print('         '+a1)
   print('         '+b1)
   print('         '+c1)
   print('         '+d1,'\n')
   print(colored("The Indian Succession Act. 1925"),"\n",colored("Under Section 372"))
   def f2():
          global m
          global a
          f=0
          print()
          print(colored('  Enter the additional amount:','green'))
          # print(colored('  ',end='')
          print()
          print('  Rs. ',end='')
          try:
               a=float(input())
          except ValueError:
               print(colored('  Only numbers are accepted.','red'))
               f=1
          if f==1:
              print()
          else:
               m=tsc2.cal(a)
               r1=str(round(m,2))
               print()
               q1=colored('Non-Judicial stamp to be paid on the Additional amount of Rs. '+r1,'red')
               print('  '+q1)
               print()
          print(colored('             --------------------- END ---------------------','green'))
          print()
          
   def sc():
     def calculation():#Calculation of the succession calculator
          if(n<=10000):
           tax=0.03*n
          elif (n>10000 and n<=50000):				
           tax=(0.03*10000)+(0.04*(n-10000))
          elif(n>50000 and n<=100000):
           tax=(0.03*10000)+(0.04*40000)+(0.05*(n-50000))
          elif(n>100000 and n<=250000):
           tax=(0.03*10000)+(0.04*40000)+(0.05*50000)+(0.06*(n-100000))
          elif(n>250000 and n<=300000):
           tax=(0.03*10000)+(0.04*40000)+(0.05*50000)+(0.06*150000)+(0.065*(n-250000))
          elif(n>300000 and n<=400000):  
           tax=(0.03*10000)+(0.04*40000)+(0.05*50000)+(0.06*150000)+(0.065*50000)+(0.07*(n-300000))
          elif(n>400000 and n<=500000):
           tax=(0.03*10000)+(0.04*40000)+(0.05*50000)+(0.06*150000)+(0.065*50000)+(0.07*100000)+(0.075*(n-400000))
          else:
           tax=(0.03*10000)+(0.04*40000)+(0.05*50000)+(0.06*150000)+(0.065*50000)+(0.07*100000)+(0.075*100000)+(0.08*(n-500000))
          print()
          r=str(round(tax,2))
          q=colored('Non-Judicial stamp to be paid of'+' Rs.'+r,'red')
          print('  '+q)
          #print()
          #print('Exact amount to be paid:'+' Rs.'+str(math.ceil(tax))+'/-')
     print(colored('  Enter required amount for obtaining Succession Certificate [New Filing]: ','green'))
     print()
     try:
      print('  Rs.',end='')
      n=float(input())
      calculation()
     except ValueError: 
      print()        
      print(colored('  Only numbers are accepted.','red'))
     print()
     #f()
     # print()
     print(colored('  ----------------- END ------------------','green'))
     print()
     print()
     # n=''
     # while n!=0:
     #  if n==0:
     #         break
     #  else:  
     #      print(colored('  Enter any further required amount, if any: [Enter zero(0) to close the window]','\n')
     #  try:
     #     print(colored('  Rs.',end='')
     #     n=float(input())
     #     calculation()
     #     print()
     #  except ValueError:
     #     print()         
     #     print(colored('  Only numbers are accepted.')
     # #  f()
     # #  print()
     #  print()
     #  print(colored('  ----------------- END ------------------')
     #  print()
   while True :
     while True:
          global c
          c=c+1
          if c==1:
           print(colored('  Enter required amount for the assessment of value of Non-Judicial Stamp,','green'))
          elif c>1:
           print(colored('  Enter any further amount require for the assessment of value of Non-Judicial Stamp,','green'))
          print(colored('  for obtaining Succession Certificate:-','green'),'\n')
          print(colored('  --------------------------------------','green'))
          print(colored('  1. For New Filing.','green'))
          print(colored('  2. For Additional Amount.','green'))
          print(colored('  --------------------------------------','green'))
          print()
          print('  Option: ',end='')   
          try:
               x=int(input())
               print()
          except ValueError:
               f=1
               def ef():
                    print()
                    print(colored('  Put Only 1 or 2. Try Again!','red'))
                    print()
                    print(colored('  ----------------- END ------------------','green'))
                    print()
               ef()
               break
          if x==1:
           sc()
          elif x==2:
           f2()
          elif x>2 or f==1:
           print()
           print(colored('  Put Only 1 or 2. Try Again!','red'))
           print()
          #     ef()
           print(colored('         ----------------- END ------------------','green'))
           print()
if z==0 or z<0:
     print(colored('Your license has been expired.','red'),'\n')
     print(colored('To continue this service please contact with:-','green'))
     a1=colored(' ----------------------------------------- ','red')
     b1=colored(' | DEVELOPED BY --> Sayantan Chakraborty | ','red')
     c1=colored(' |          Ph. No.- 7908 375 185        | ','red')
     d1=colored(' ----------------------------------------- ','red')
     print(' '+a1)
     print(' '+b1)
     print(' '+c1)
     print(' '+d1,'\n')
     p=input()
else:
     license()