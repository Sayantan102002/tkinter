l1=[]
l2=[]
class plaint:
    def calculation(self,t):
        def createList1(r1, r2,k): 
            return [item for item in range(r1, r2+100,k)] 
        def createList2(r1, r2,k): 
            return [item for item in range(r1, r2+1,k)]  
        def courtfees(n):
            n=t
            global l1
            global l2
            l1=createList1(1,1000,100)
            l1+=createList1(1101,7500,100)
            l1+=createList1(7751,10000,250)
            l1+=createList1(10501,20000,500)
            l1+=createList1(21001,50000,1000)
            l1+=createList1(55001,100000,5000)
            l1+=createList1(105001,200000,5000)
            l1+=createList1(205001,300001,5000)

            l2+=createList2(10,100,10)
            l2+=createList2(108,620,8)
            l2+=createList2(636,780,16)
            l2+=createList2(810,1380,30)
            l2+=createList2(1430,2880,50)
            l2+=createList2(3230,6380,350)
            l2+=createList2(6750,13780,370)
            l2+=createList2(13990,17980,210)
            # l2+=createList2(13990,17980,210)
            # print(l1)
            # print(l2)
            i=0
            for i in range(len(l1)):
                if n>=l1[i] and n<l1[i+1] and n<=300000:
                    return(l2[i])
                elif n>300000:
                    if (n-300000)%100000==0:
                        return((17980+((n-300000)/10000)*100))
                    else:
                        return(17980+((n-300000)//10000)*100+100)
        return courtfees(1000000)
if __name__ == "__main__":
    ob=plaint()
    print(ob.calculation(300000))#17980