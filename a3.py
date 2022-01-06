from colorama import init 
from termcolor import colored 
init() 
co_dict={298:['The person whose religious feelings are intended to be wounded',
              'Uttering words, etc., with deliberate intent to wound the religious feelings of any person.'],
         323:['The person to whom the hurt is caused',
              'Voluntarily causing hurt.'],
         334:['The person to whom the hurt is caused','Voluntarily causing hurt on provocation.'],
         335:['The person to whom the hurt is caused','Voluntarily causing grievous hurt on grave and sudden provocation.'],
         341:['The person restrained or confined','Wrongfully restraining or confining any person.'],
         342:['The person restrained or confined','Wrongfully restraining or confining any person.'],
         343:['The person confined','Wrongfully confining a person for three days or more.'],
         344:['The person confined','Wrongfully confining a person for ten days or more.'],
         346:['The person confined','Wrongfully confining a person in secret.'],
         352:['The person assaulted or to whom criminal force is used','Assault or use of criminal force.'],
         355:['The person assaulted or to whom criminal force is used','Assault or use of criminal force.'],
         358:['The person assaulted or to whom criminal force is used','Assault or use of criminal force.'],
         379:['The owner of the property stolen','Theft.'],
         403:['The owner of the property misappropriated','Dishonest misappropriation of property.'],
         407:['The owner of the property misappropriated','Criminal breach of trust by a carrier, wharfinger, etc.'],
         411:['The owner of the property stolen','Dishonestly receiving stolen property knowing it to be stolen.'],
         414:['The owner of the property stolen','Assisting in the concealment or disposal of stolen property, knowing it to be stolen.'],
         417:['The person cheated','Cheating.'],
         419:['The person cheated','Cheating by personation.'],
         421:['The creditors who are affected thereby','Fraudulent removal or concealment of property, etc., to prevent distribution among creditors.'],
         422:['The creditors who are affected thereby','Fraudulently preventing from being made available for his creditors a debt or demand due to the offender.'],
         423:['The person affected thereby','Fraudulent execution of deed of transfer containing false statement of consideration.'],
         424:['The person affected thereby','Fraudulent removal or concealment of property.'],
         426:['The person to whom the loss or damage is caused','Mischief, when the only loss or damage caused is loss or damage to a private person.'],
         427:['The person to whom the loss or damage is caused','Mischief, when the only loss or damage caused is loss or damage to a private person.'],
         428:['The owner of the animal','Mischief by killing or maiming animal.'],
         429:['The owner of the cattle or animal','Mischief by killing or maiming cattle, etc.'],
         430:['The person to whom the loss or damage is caused',
              'Mischief by injury to works of irrigation by wrongfully diverting water when the only loss or damage caused is loss or damage to private person.'],
         447:['The person in possession of the property trespassed upon','Criminal trespass.'],
         448:['The person in possession of the property trespassed upon','House-trespass.'],
         451:['The person in possession of the house trespassed upon','House-trespass to commit an offence (other than theft) punishable with imprisonment.'],
         482:['The person to whom loss or injury is caused by such use','Using a false trade or property mark.'],
         483:['The person to whom loss or injury is caused by such use','Counterfeiting a trade or property mark used by another.'],
         486:['The person to whom loss or injury is caused by such use',
              'Knowingly selling, or exposing or possessing for sale or for manufacturing purpose, goods marked with a counterfeit property mark.'],
         491:['The person with whom the offender has contracted','Criminal breach of contract of service.'],
         497:['The husband of the woman','Adultery.'],
         498:['The husband of the woman and the woman','Enticing or taking away or detaining with criminal intent a married woman.'],
         500:['The person defamed',
              'Defamation, except such cases as are specified against section 500 of the Indian Penal Code (45 of 1860) in column 1 of the Table under sub-section (2).'],
         501:['The person defamed','Printing or engraving matter, knowing it to be defamatory.'],
         502:['The person defamed','Sale of printed or engraved substance containing defamatory matter, knowing it to contain such matter.'],
         504:['The person insulted','Insult intended to provoke a breach of the peace.'],
         506:['The person intimidated','Criminal intimidation.'],
         508:['The person induced','Inducing person to believe himself an object of divine displeasure.'],
             }    
co_dict2={312:['The woman to whom miscarriage is caused.','Causing miscarriage.'],
         325:['The person to whom hurt is caused.','Voluntarily causing grievous hurt.'],
         337:['The person to whom hurt is caused.','Causing hurt by doing an act so rashly and negligently as to safety of others.'],
         338:['The person to whom hurt is caused.','Causing grievous hurt by doing an act so rashly and negligently as to endanger human life or the personal safety of others.'],
         357:['The person assaulted or to whom the force was used.','Assault or criminal force in attempting wrongfully to confine a person.'],
         381:['The owner of the property stolen.','Theft, by clerk or servant of property in possession of master.'],
         406:['The owner of the property in respect of which the breach of trust has been committed.','Criminal breach of trust'],
         408:['The owner of the property in respect of which the breach of trust has been committed.','Criminal breach of trust by a clerk or servant.'],
         418:['The person cheated.','Cheating a person whose interest the offender was bound, either by law or by legal contract, to protect.'],
         420:['The person cheated.','Cheating and dishonestly inducing delivery of property or the making, alteration or destruction of a valuable security.'],
         494:['The husband or wife of the person so marrying.','Marrying again during the life-time of a husband or wife.'],
         500:['The person defamed.','Defamation against the President or the Vice-President or the Governor of a State or the Administrator of a Union territory or a Minister in respect of his public functions when instituted upon a complaint made by the Public Prosecutor.'],
         509:['The woman whom it was intended to insult or whose privacy was intruded upon.','Uttering words or sounds or making gestures or exhibiting any object intending to insult the modesty of a woman or intruding upon the privacy of a woman.'],
        }
# a=''
print('   ','\n')
a1=colored(' ----------------------------------------- ','red')
b1=colored(' | DEVELOPED BY --> Sayantan Chakraborty | ','red')
c1=colored(' |          Ph. No.- 7908 375 185        | ','red')
d1=colored(' ----------------------------------------- ','red')
print('         '+a1)
print('         '+b1)
print('         '+c1)
print('         '+d1,'\n')
c=0
print (colored("                  COMPOUNDING OF OFFENCES", "green"),'\n',colored("           (According to section 320 of Cr.P.C)", "green"), "\n",colored("           ------------------------------------", "green"),"\n")


def entry():
  global c
  c+=1
  if c==1:
    print(colored('   Enter the Section of I.P.C:','green'),end=' ')
  elif c>1:
    print(colored('   Enter any further Section of I.P.C:','green'),end=' ')
  t=0
  try:
    t=int(input())
    print()
  except ValueError:
      print('',end='')
  def search(n):
    # global a
    # global j
    k=1
    if t in co_dict.keys():
        for i,j in co_dict.items():
            if n==i:
             print(colored('   Offence:- ','white'))
             print(colored('   ----------','green'))
             print(colored('   '+j[1],'green'),'\n')
             print(colored('   Person by whom offence may be compounded:- ','white'))
             print(colored('   -------------------------------------------','green'))
             print(colored('   '+j[0]+', according to section 320(1) of Cr.P.C.','red'))
             print()
             k=2
    if t in co_dict2.keys():
        for x,y in co_dict2.items():
            if n==x:
             print(colored('   Offence:- ','white'))
             print(colored('   ----------','green'))
             print(colored('   '+y[1],'green'),'\n')
             print(colored('   Person by whom offence may be compounded:- ','white'))
             print(colored('   -------------------------------------------','green'))
             print(colored('   '+y[0]+' With the permission of the court as per section 320(2) of Cr.P.C.','red'),'\n')       
             k=2
    if k==1: 
      print()        
      print(colored('   This offence is not compoundable according to section 320 of Cr.P.C.','red'))
      print()
    print(colored('                ------------------- END -------------------','green'),'\n')
  search(t)  
while 1:     
    entry()