class calc:
    tax=0.0
    def cal(self,n):
          self.n=n
          if(n<=10000):
           tax=0.04*n
          elif (n>10000 and n<=50000):				
           tax=(0.04*10000)+(0.045*(n-10000))
          elif(n>50000 and n<=100000):
           tax=(0.04*10000)+(0.045*40000)+(0.06*(n-50000))
          elif(n>100000 and n<=250000):
           tax=(0.04*10000)+(0.045*40000)+(0.06*50000)+(0.075*(n-100000))
          elif(n>250000 and n<=300000):
           tax=(0.04*10000)+(0.045*40000)+(0.06*50000)+(0.075*150000)+(0.0825*(n-250000))
          elif(n>300000 and n<=400000):  
           tax=(0.04*10000)+(0.045*40000)+(0.06*50000)+(0.075*150000)+(0.0825*50000)+(0.09*(n-300000))
          elif(n>400000 and n<=500000):
           tax=(0.04*10000)+(0.045*40000)+(0.06*50000)+(0.075*150000)+(0.0825*50000)+(0.09*100000)+(0.0975*(n-400000))
          else:
           tax=(0.04*10000)+(0.045*40000)+(0.06*50000)+(0.075*150000)+(0.0825*50000)+(0.09*100000)+(0.0975*100000)+(0.105*(n-500000))
          return tax
if __name__ == "__main__":
    Calculation=calc()
    print(Calculation.cal(10000))
# if __name__ == "__main__":
#  print(cal(60000))