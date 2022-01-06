import re
#'Ins. by Criminal Law (Am.) Act. 2013 (w.e.f 03.2.2013)'
def Explanatory_note():
    print()
    print('Explanatory note:- ','\n-----------------')
    print('1. In regard to offences under the Indian Penal Code, the entries in the second and third Columns against a section the number of which is given in the first column are not intended as the definition of, and the punishment prescribed for, the offence in the Indian Penal Code, but merely as indication of the substance of the section.','\n')
    print('2. In this Schedule, (i) the expression “Magistrate 1st Class” and “Any Magistrate” include Metropolitan Magistrates but not Executive Magistrate;(ii) the word “cognizable” stands for “a police officer may arrest without warrant”; and (iii) the word “non-cognizable” stands for “a police officer shall not arrest without warrant”.')
# Explanatory_note()

d2={'115':['If an act which causes harm to be done in consequence of the abetment.', 'Imprisonment for 14 Years and fine.', 'According as offence abetted is cognizable or non-cognizable', 'Non-bailable.', 'Court by which offence is triable.'],
    '116':['Abetment of an offence, punishable with Imprisonment, if the offence be not committed in consequence of the abetment.', 'Imprisonment extending to a quarter part of the longest term provided for the offence, or fine, or both.', 'According as offence abetted is cognizable or non-cognizable', 'According as offence abetted is bailable or non-bailable.', 'Court by which offence is triable.'],
    '118':['If the offence be not committed.', 'Imprisonment for 3 years and fine', 'According as offence abetted is cognizable or non-cognizable.', 'Bailable', 'Court by which offence abetted is triable.'],
    '119':['If the offence be punishable with death or imprisonment for life.', 'Imprisonment for 10 years', 'According as offence is Cognizable or Non-Cognizable', 'Non-bailable', 'Court by which offence abetted is triable'],
    '120':['If the offence be not committed.', 'Imprisonment extending to one-eighth part of the longest term provided for the offence, or fine, or both.', 'According as offence is cognizable or non-cognizable.', 'Bailable', 'Court by which offence abetted is triable.'],
    '120B':['Any other criminal conspiracy.', 'Imprisonment for 6 months, or fine, or both.', 'Non=cognizable', 'Bailable', 'Magistrate of the first class.'],
    '153':['If not committed.', 'Imprisonment for 6 months, or fine, or both.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '153A':['Promoting enmity between classes in place of worship, etc.', 'Imprisonment for 5 years, and fine.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '153B':['If committed in a place of public worship, etc.', 'Imprisonment for 5 years and fine', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '158':['Or to go armed.', 'Imprisonment for 2 years, or fine, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '171F':['Personation at an election.', 'Imprisonment for one year, or fine, or both.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '172':['If summons or notice require attendance in person, etc., in a Court of Justice.', 'Simple imprisonment for 6 months, or fine of 1,000 rupees, or both. ', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '173':['If summons, etc., require attendance in person, etc., in a Court of Justice.', 'Simple imprisonment for 6 months, or fine of 1,000 rupees, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '174':['If the order requires personal attendance, etc., in a Court of Justice.', 'Simple imprisonment for 6 months, or fine of 1,000 rupees, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '174A':['In a case where declaration has been made under sub-section (4) of section 82 of this Code pronouncing a person as proclaimed offender.',"Imprisonment for 7 years and fine.", 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '175':['If the document is required to be produced in or delivered to a Court of Justice.', 'Simple imprisonment for 6 months, or fine of 1,000 rupees, or both.', 'Non-Cognizable', 'Bailable', 'The Court in which the offence is committed, subject to the provisions of Chapter XXVI; or, if not committed, in a court, any Magistrate.'],
    '176':['If the notice or information required respects the commission of an offence, etc.', 'Simple imprisonment for 6 months, or fine of 1,000 rupees, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'], 
    '177':['If the information required respects the commission of an offence, etc.', 'Imprisonment for 2 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '187':['Wilfully neglecting to aid a public servant who demands aid in the execution of process, the prevention of offences, etc.', 'Simple imprisonment for 6 months, or fine of 500 rupees, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '188':['If such disobedience causes danger to human life, health or safety, etc.', 'Imprisonment for 6 months, or fine of 1,000 rupees, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '193':['Giving or fabricating false evidence in any other case.', 'Imprisonment for 3 years and fine', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '194':['If innocent person be thereby convicted and executed.', 'Death, or as above.', 'Non-Cognizable', 'Non-Bailable', 'Court of Session.'],
    '195A':['If innocent person is convicted and sentenced in consequence of false evidence with death, or imprisonment for more than seven years.', 'The same as for the offence.', 'Cognizable', 'Non-Bailable', 'Court by which offence of giving false evidence is triable.'],
    '201':['If punishable with imprisonment for life or imprisonment for 10 years.', 'Imprisonment for 3 years and fine.', 'Non-Cognizable', 'Bailable', 'Magistrate of the fiest class'],
    '211':['If offence charged be punishable with imprisonment for 7 years or upwards.', 'Imprisonment for 7 years and fine.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '212':['If punishable with imprisonment for life or with imprisonment for 10 years.', 'Imprisonment for 3 years and fine.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '213':['If punishable with imprisonment for life or with imprisonment for 10 years.', 'Imprisonment for 3 years and fine.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '214':['If punishable with imprisonment for life or with imprisonment for 10 years.', 'Imprisonment for 3 years and fine.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '216':['If punishable with imprisonment for life or with imprisonment for 10 years.', 'Imprisonment for 3 years, with or without fine.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '221':['If punishable with imprisonment for life or imprisonment for 10 years.', 'Imprisonment for 3 years, with or without fine.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '222':['If under sentence of imprisonment for life or imprisonment for 10 years, or upwards.', 'Imprisonment for 7 years, with or without fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '225':['If charged with an offence punishable with imprisonment for life or imprisonment for 10 years.', 'Imprisonment for 3 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.',],
    '225A':['(b) in case of negligent omission or sufferance.', 'Simple imprisonment for 2 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '228A':['Printing or publication of a proceeding without prior permission of court.', 'Imprisonment for two years and fine.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '235':['If Indian coin.', 'Imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Sessions.'],
    '294A':['Publishing proposals relating to lotteries.', 'Fine of 1,000 rupees', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '304':['If act is done with knowledge that it is likely to cause death, but without any intention to cause death, etc.', 'Imprisonment for 10 years, or fine, or both.', 'Cognizable', 'non-Bailable', 'Court of Session.'],
    '307':['If such act causes hurt to any person.', 'Imprisonment for life, or imprisonment for 10 years and fine.', 'Cognizable', 'non-Bailable', 'Court of Session.'],
    '308':['If such act causes hurt to any person', 'Imprisonment for 7 years, or fine, or both.', 'Cognizable', 'non-Bailable', 'Court of Session.'],
    '312':['If the woman be quick with child.', 'Imprisonment for 7 years and fine.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '314':['If act done without women’s consent.', 'Imprisonment for life, or as above.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '354A':['Sexual harassment of the nature of making sexually coloured remark.', 'Imprisonment which may extend to 1 year or with fine or with both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '354C':['Voyeurism.', 'Imprisonment of not less than 3 years but which may extend 7 years and with fine for second or subsequent conviction.', 'Cognizable', 'Non-Bailable', 'Any Magistrate.'],
    '354D':['Stalking.', 'Imprisonment up to 5 years and with fine for second or subsequent conviction.', 'Cognizable', 'Non-Bailable', 'Any Magistrate.'],
    '363A':['Maiming a minor in order that such minor may be employed or used for purposes of begging.', 'Imprisonment for life and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '370':['Trafficking of more than one person.', 'Imprisonment of not less than 10 years but which may extend to imprisonment for life and with fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '370A':['Exploitation of a trafficked person.', 'Imprisonment of not less than 3 years but which may extend to 5 years and with fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '376':['Rape by a police officer or a public servant or member of armed forces or a person being on the management or on the staff of a jail, remand home or other place of custody or women’s or children’s institution or by a person on the management or on the staff of a hospital, and rape committed by a person in a position of trust or authority towards the person raped or by a near relative of the person raped.', 'Rigorous imprisonment of not less than 10 years but which may extend to imprisonment for life which shall mean the remainder of that person’s natural life and with fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '388':['If the offence threatened be an unnatural offence.', 'Imprisonment for life.', 'Cognizable', 'Bailable', 'Magistarte of the first class.'],
    '389':['If the offence be an unnatural offence.', 'Imprisonment for life.', 'Cognizable', 'Bailable', 'Magistarte of the first class.'],
    '392':['If committed on the highway between sunset and sunrise.', 'Rigorous imprisonment for 14 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistarte of the first class.'],
    '404':['If by clerk or person employed by deceased', 'Imprisonment for 7 years and fine.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '451':['If the offence is theft', 'Imprisonment for 7 years and fine.', 'Cognizable', 'Non-Bailable', 'Any Magistrate.'],
    '454':['If the offence be theft.', 'Imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Any Magistrat.'],
    '457':['If the offence is theft', 'Imprisonment for 14 years and fine.', 'Imprisonment for 5 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '467':['When the valuable security is a promissory note of the Central Government.', 'Imprisonment for life, or imprisonment for 10 years and fine.', 'Non-Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '471':['When the forged document is a promissory note of the Central Government.', 'Punishment for forgery of such document.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '474':['If the document is one of the description mentioned in section 467 of the Indian Penal Code.', 'Imprisonment for life, or imprisonment for 7 years and fine.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '489E':['On refusal to disclose the name and address of the printer.', 'Fine of 200 rupees.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'], 
    '500':['Defamation in any other case', 'Simple imprisonment for 2 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '501':['(b) Printing or engraving matter knowing it to be defamatory, in any other case.', 'Simple imprisonment for 2 years, or fine, or both.' 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '502':['(b) Sale of printed or engraved substance containing defamatory matter, knowing it to contain such matter in any other case.', 'Simple imprisonment for 2 years, or fine, or both.' 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '505':['False statement, rumour, etc., with intent to create enmity, hatred or illwill between different classes.', 'Imprisonment for 3 years, or fine, or both.', 'Cognizable', 'Non-Bailable', 'Any Magistrate.'], 
    '506':['If threat be to cause death or grievous hurt, etc', 'Imprisonment for 7 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    }


d3={'119':['If the offence be not committed.', 'Imprisonment extending to a quarter part of the longest term provided for the of fence, or fine, or both.', 'According as offence is Cognizable or Non-Cognizable', 'Bailable.', 'Court by which offence abetted is triable.'],
    '176':['If the notice or information is required by an order passed under sub-section (1) of section 356 of this Code.', 'Imprisonment for 6 months, or fine of 1,000 rupees, or both. ' 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '201':['If punishable with less than 10 years’ imprisonment.', 'Imprisonment for a quarter of the longest term provided for the offence, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Court by which the offence is triable.'],
    '211':['If offence charged be capital or punishable with imprisonment for life.', 'Imprisonment for 7 years and fine.', 'Non-Cognizable', 'Bailable', 'Court of Session.'],
    '212':['If punishable with imprisonment for 1 year and not for 10 years.', 'Imprisonment for a quarter of the longest term, and of the descriptions, provided for the offence, or fine, or both.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '213':['If punishable with imprisonment for less than 10 years.', 'Imprisonment for a quarter of the longest term provided for the offence, or fine, or both.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '214':['If punishable with imprisonment for less than 10 years.', 'Imprisonment for a quarter of the longest term, provided for the offence, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '216':['If punishable with imprisonment for 1 year and not for 10 years.', 'Imprisonment for a quarter of the longest term provided for the offence, or fine, or both.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '221':['If punishable with imprisonment for less than 10 years.', 'Imprisonment for 2 years, with or without fine.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '222':['If under sentence of imprisonment for less than 10 years or lawfully committed to custody.', 'Imprisonment for 3 years, or fine, or both.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '225':['If charged with a capital offence.', 'Imprisonment for 7 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '370':['Trafficking of a minor.', 'Imprisonment of not less than 10 years but which may extend to imprisonment for life and with fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '376':['Persons committing offence of rape on a woman under sixteen years of age.', 'Rigorous imprisonment for a term which shall not be less than 20 years but which may extend to imprisonment for life, which shall mean imprisonment for the remainder of that person’s natural life and with fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '454':['If the offence be theft.', 'Imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '505':['False statement, rumour, etc., made in place of worship, etc., with intent to create enmity, hatred or ill-will.', 'Imprisonment for 5 years and fine.', 'Cognizable', 'Non-Bailable', 'Any Magistrate.'],
    }

d4={'225':['If the person is sentenced to imprisonment for life, or imprisonment for 10 years, or upwards.', 'Imprisonment for 7 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '370':['Trafficking of more than one minor.', 'Imprisonment of not less than 14 years but which may extend to imprisonment for life and with fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    }

d5={'225':['If under sentence of death', 'Imprisonment for life, or imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session'],
    '370':['Person convicted of offence of trafficking of minor on more than one occasion. ', 'Imprisonment for life which shall mean the remainder of that person’s natural life and with fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    }

d6={'370':['Public servant or a police officer involved in trafficking of minor.', 'Imprisonment for life which shall mean the remainder of that person’s natural life and with fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    }

d1={'109':['Abetment of any offence, if the act abetted is committed in consequence, and where no express provision is made for its punishment.', 'Same as for offence abetted.', 'According as offence abetted is cognizable or non cognizable.', 'According as offence abetted is bailable or non bailable.', 'Court by which offence abetted is triable.'],
    '110':['Abetment of any offence, if the person abetted does the act with a different intention from that of the abettor','Same as for offence abetted.', 'According as offence abetted is cognizable or non cognizable.', 'According as offence abetted is bailable or non bailable.', 'Court by which offence abetted is triable.'],
    '111':['Abetment of any offence, when one act is abetted and a different act is done; subject to the proviso.', 'Same as for offence intended to be abetted.', 'According as offence abetted is cognizable or non cognizable.', 'According as offence abetted is bailable or non bailable.', 'Court by which offence abetted is triable.'],
    '113':['Abetment of any offence, when an effect is caused by the act abetted different from  that intended by the abettor.', 'Same as for offene committed.', 'According as offence abetted is cognizable or non cognizable.', 'According as offence abetted is bailable or non bailable.', 'Court by which offence abetted is triable.'],
    '114':['Abetment of any offence, if abettor is present when offence is committed.', 'Same as for offence committed.', 'According as offence abetted is cognizable or non-cognizible', 'According as offence abetted is bailable or non bailable.', 'Court by which offence is triable.'],
    '115':['Abetment of an offence, punishable with  death or imprisonment for life, if the offence be not committed in Consequence of the abetment', 'Imprisonment for 7 Years and fine.', 'According as offence abetted is cognizable or non-connizable', 'Non-bailable.', 'Court by which offence is triable.'],      
    '116':['If the abettor or the person abetted be a public servant whose duty is is to prevent the offence.', 'Imprisonment extending to half of the longest term provided for the offence, or fine or both.', 'According as offence abetted is cognizable or non-cognizable', 'According as offence abetted is bailable or non-bailable.', 'Court by which offence abetted is triable.'],
    '117':['Abetting the commission of an offence by the public or by more than ten persons.', 'Imprisonment for 3 Years, or fine, or both.', 'According as offence abetted is cognizable or non-cognizable', 'According as offence abetted is bailable or non-bailable.', 'Court by which offence abetted is triable.'],
    '118':['Concealing a design to commit an offence punishable with death or imprisonment for life, if the offence be committed.', 'Imprisonment for 7 Years and fine.', 'According as offence abetted is cognizable or non-cognizable', 'Non-Bailable.', 'Court by which offence abetted is triable.'],
    '119':['A public servant concealing a design to commit an offence which it is his duty to prevent, if the offence be committed', 'Imprisonment extending to half of the longest term provided for the offence, or fine, or both.', 'According as offence abetted is Cognizable or Non-Cognizable', 'According as Court offence abetted is bailable or non-bailable', 'Court by which offence abetted is triable'],
    '120':['Concealing a design to commit an offence punishable with imprisonment, if offence be committed.', 'Imprisonment extending to a quarter part of the longest term provided for the offence, or fine, or both.', 'According as offence is Cognizable or Non-Cognizable.', 'According as offence abetted is bailable or Non-bailable.', 'Court by which offence abetted is triable.'],
    '120B':['Criminal conspiracy to commit an offence punishable with death, imprisonment for life or rigorous imprisonment for a term of 2 years or upwards.', 'Same as for abetment of the offence which is the object of the conspiracy.', 'According as the offence which is the object of conspiracy is cognizable or non-cognizable.', 'According as offence which is object of conspiracy is bailable or non-bailable.', 'Court by which abetment of the offence which is the object of conspiracy is triable.'],
    
    '121':['Waging or attempting to wage war, or abetting the waging of war, against the Government of India.', 'Death, or imprisonment for life and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '121A':['Conspiring to commit certain offences against the State.', 'Imprisonment for life, or imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '122':['Collecting arms, etc., with the intention of waging war against the Government of India.', 'Imprisonment for life, or imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '123':['Concealing with intent to facilitate a design to wage war', 'Imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '124':['Assaulting President, Governor, etc., with intent to compel or restrain the exercise of any lawful power.', 'Imprisonment for 7 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '124A':['Sedition.', 'Imprisonment for life and fine, or imprisonment for 3 years and fine, or fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '125':['Waging war against any Asiatic power in alliance or at peace with the Government of India, or abetting the waging of such war.', 'Imprisonment for life and fine, or imprisonment for 7 years and fine, or fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '126':['Committing depredation on the territories of any power in alliance or at peace with the Government of India.', 'Imprisonment for 7 years and fine, and forfeiture of certain property.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '127':['Receiving property taken by war or depredation mentioned in sections 125 and 126.', 'Imprisonment for 7 years and fine, and forfeiture of certain property.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '128':['Public servant voluntarily allowing prisoner of State or war in his custody to escape.', 'Imprisonment for life, or imprisonment for 10 years and fine', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '129':['Public servant negligently suffering prisoner of State of war in his custody to escape.', 'Simple imprisonment for 3 years and fine.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '130':['Aiding escape of, rescuing or harbouring, such prisoner, or offering any resistance to the recapture of such prisoner.', 'Imprisonment for life, or imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],

    '131':['Abetting mutiny, or attempting to seduce an officer, soldier, sailor or airman from his allegiance or duty', 'Imprisonment for life, or imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '132':['Abetment of mutiny, if mutiny is committed in consequence thereof.', 'Death, or imprisonment for life, or imprisonment for 10 years and fine', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '133':['Abetment of an assault by an officer, soldier, sailor or airman on his superior officer, when in the execution of his office.', 'Imprisonment for 3 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '134':['Abetment of such assault, if the assault is committed.', 'Imprisonment for 7 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '135':['Abetment of the desertion of an officer, soldier, sailor or airman.', 'Imprisonment for 2 years, or fine, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '136':['Harbouring such an officer,. soldier, sailor or airman who has deserted.', 'Imprisonment for 2 years, or fine, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '137':['Deserter concealed on board merchant vessel, through negligence of master or person in charge thereof.', 'Fine of 500 rupees.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '138':['Abetment of act of insubordination by an officer, soldier, sailor or airman, if the offence be committed in consequence.', 'Imprisonment for 6 months, or fine, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '140':['Wearing the dress or carrying any token used by a soldier, sailor or airman with intent that it may be believed that he is such a soldier, sailor or airman.', 'Imprisonment for 3 months, or fine of 500 rupees, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],

    '143':['Being member of an unlawful assembly.', 'Imprisonment for 6 months, or fine, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '144':['Joining an unlawful assembly armed with any deadly weapon.', 'Imprisonment for 2 years, or fine, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '145':['Joining or continuing in an unlawful assembly, knowing that it has been commanded to disperse.', 'Imprisonment for 2 years, or fine, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '147':['Rioting.', 'Imprisonment for 2 years, or fine, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '148':['Rioting, armed with a deadly weapon.', 'Imprisonment for 3 years, or fine, or both.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '149':['If an offence be committed by any member of an unlawful assembly, every other member of such assembly shall be guilty of the offence.', 'The same as for the offence.', 'According as offence is cognizable or noncognizable', 'According as offence is bailable or non-bailable.', 'The Court by which the offence is triable.'],
    '150':['Hiring, engaging or employing persons to take part in an unlawful assembly.', 'The same as for a member of such assembly, and for any offence committed by any member of such assembly.', 'Cognizable', 'According as offence is bailable or non-bailable.', 'The Court by which the offence is triable.'],
    '151':['Knowingly joining or continuing in any assembly of five or more persons after it has been commanded to disperse.', 'Imprisonment for 6 months, or fine or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '152':['Assaulting or obstructing public servant when suppressing riot, etc.', 'Imprisonment for 3 years, or fine, or both.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '153':['Wantonly giving provocation with intent to cause riot, if rioting be committed.', 'Imprisonment for 1 year, or fine, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    
    '153A':['Promoting enmity between classes.', 'Imprisonment for 3 years, or fine, or both.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    
    '153AA':['Knowingly carrying arms in any procession or organising or holding or taking part in any mass drill or mass traning with arms.', 'Imprisonment for 6 months and kfine of 2,000 rupees.', 'Cognizable', 'Non-Bailable', 'Any Magistrate.', 'Ins. by Cr.P.C (Amendment) Act 2005 (25 of 2005)'],
    '153B':['Imputations, assertions prejudicial to national integration', 'Imprisonment for 3 years, or fine, or both.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '154':['Owner or occupier of land not giving information of riot, etc.', 'Fine of 1,000 rupees.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '155':['Person for whose benefit or on whose behalf a riot takes place not using all lawful means to prevent it.', 'Fine.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '156':['Agent of owner or occupier for whose benefit a riot is committed not using all lawful means to prevent it.', 'Fine.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '157':['Harbouring persons hired for an unlawful assembly.', 'Imprisonment for 6 months, or fine, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '158':['Being hired to take part in an unlawful assembly or riot.', 'Imprisonment for 6 months, or fine, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '160':['Committing affray.', 'Imprisonment for one month, or fine of 100 rupees or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    
    '161':['Sections 161 to 165A of the I.P.C 1860 (45 of 1860) repealed by the Prevention of Coruption Act. 1988 (49 of 1988), S.31.','','','',''],
    '162':['Sections 161 to 165A of the I.P.C 1860 (45 of 1860) repealed by the Prevention of Coruption Act. 1988 (49 of 1988), S.31.','','','',''],
    '163':['Sections 161 to 165A of the I.P.C 1860 (45 of 1860) repealed by the Prevention of Coruption Act. 1988 (49 of 1988), S.31.','','','',''],
    '164':['Sections 161 to 165A of the I.P.C 1860 (45 of 1860) repealed by the Prevention of Coruption Act. 1988 (49 of 1988), S.31.','','','',''],
    '165':['Sections 161 to 165A of the I.P.C 1860 (45 of 1860) repealed by the Prevention of Coruption Act. 1988 (49 of 1988), S.31.','','','',''],
    '165A':['Sections 161 to 165A of the I.P.C 1860 (45 of 1860) repealed by the Prevention of Coruption Act. 1988 (49 of 1988), S.31.'],
    '166':['Public servant disobeying a direction of the law with intent to cause injury to any person.', 'Simple imprisonment for 1 year, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '166A':['Public servant disobeying direction under law.', 'Imprisonment for minimum 6 months which may extend to 2 years and fine.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'], 
    '166B':['Non-treatment of victim by hospital.', 'Imprisonment for 1 year or fine or both.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '167':['Public servant framing an incorrect document with intent to cause injury.', 'Imprisonment for 3 years, or fine, or both.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '168':['Public servant unlawfully engaging in trade.', 'Simple imprisonment for 1 year, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '169':['Public servant unlawfully buying or bidding for property.', 'Simple imprisonment for 2 years, or fine, or both and confiscation of property, if purchased.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '170':['Personating a public servant.', 'Imprisonment for 2 years or fine, or both .', 'Cognizable', 'Non-Bailable', 'Any Magistrate.'],
    '171':['Wearing garb or carrying token used by public servant with fraudulent intent.', 'Imprisonment for 3 months, or fine of 200 rupees, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],

    '171E':['bribery.', 'Imprisonment for 1 year or fine, or both, or if treating only, fine only.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '171F':['Undue influence at an election.', 'Imprisonment for one year, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '171G':['False statement in connection with an election.', 'Fine', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '171H':['Illegal payments in connection with elections.', 'Fine of 500 rupees.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '171I':['Failure to keep election accounts.', 'Fine of 500 rupees.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],

    '172':['Absconding to avoid service of summons or other proceeding from a public servant.', 'Simple imprisonment for 1 month, or fine of 500 rupees, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '173':['Preventing the service or the affixing of any summons of notice, or the removal of it when it has been affixed, or preventing a proclamation.', 'Simple imprisonment for 1 month, or fine of 500 rupees, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '174':['Not obeying a legal order to attend at a certain place in person or by agent, or departing there from without authority.', 'Simple imprisonment for 1 month, or fine of 500 rupees, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '174A':['Failure to appear at specified place and specified time as required by a proclamation published under sub-section (1) of section 82 of this Code.', 'Imprisonment for 3 years, or with fine, or with both.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '175':['Intentionally omitting to produce a document to a public servant by a person legally bound to produce or deliver such document.', 'Simple imprisonment for 1 month, or fine of 500 rupees, or both.', 'Non-Cognizable', 'Bailable', 'The Court in which the offence is committed, subject to the provisions of Chapter XXVI; or, if not committed, in a court, any Magistrate.'],
    '176':['Intentionally omitting to give notice or information to a public servant by a person legally bound to give such notice or information.', 'Simple imprisonment for 1 month, or fine of 500 rupees, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '177':['Knowingly furnishing false information to a public servant.', 'Imprisonment for 6 months, or fine of 1,000 rupees, or both. ' 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '178':['Refusing oath when duly required to take oath by a public servant.', 'Simple imprisonment for 6 months, or fine of 1,000 rupees, or both.', 'Non-Cognizable', 'Bailable', 'The Court in which the offence is committed, subject to the provisions of Chapter XXVI; or, if not committed in a Court, any Magistrate.'],
    '179':['Being legally bound to state truth, and refusing to answer questions.', 'Simple imprisonment for 6 months, or fine of 1,000 rupees, or both.', 'Non-Cognizable', 'Bailable', 'The Court in which the offence is committed, subject to the provisions of Chapter XXVI; or, if not committed in a Court, any Magistrate.'],
    '180':['Refusing to sign a statement made to a public servant when legally required to do so.', 'Simple imprisonment for 3 months, or fine of 500 rupees, or both.', 'Non-Cognizable', 'Bailable', 'The Court in which the offence is committed, subject to the provisions of Chapter XXVI; or, if not committed in a Court, any Magistrate.'],
    '181':['Knowingly stating to a public servant on oath as true that which is false.', 'Imprisonment for 3 years and fine.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '182':['Giving false information to a public servant in order to cause him to use his lawful power to the injury or annoyance of any person.', 'Imprisonment for 6 months, or fine of 1,000 rupees, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '183':['Resistance to the taking of property by the lawful authority of a public servant.', 'Imprisonment for 6 months, or fine of 1,000 rupees, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '184':['Obstructing sale of property offered for sale by authority of a public servant.', 'Imprisonment for 1 month, or fine of 500 rupees, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '185':['Bidding, by a person under a legal incapacity to purchase it, for property at a lawfully authorised sale, or bidding without intending to perform the obligations incurred thereby.', 'Imprisonment for 1 month, or fine of 200 rupees, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '186':['Obstructing public servant in discharge of his public functions.', 'Imprisonment for 3 months, or fine of 500 rupees, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '187':['Omission to assist public servant when bound by law to give such assistance.', 'Simple imprisonment for 1 month, or fine of 200 rupees, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '188':['Disobedience to an order lawfully promulgated by a public servant, if such disobedience causes obstruction, annoyance or injury to persons lawfully employed.', 'Simple imprisonment for 1 month, or fine of 200 rupees, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '189':['Threatening a public servant with injury to him or one in whom he is interested, to induce him to do or forbear to do any official act.', 'Imprisonment for 2 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '190':['Threatening any person to induce him to refrain from making a legal application for protection from injury.', 'Imprisonment for 1 year, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'], 

    '193':['Giving or fabricating false evidence in a judicial proceeding.', 'Imprisonment for 7 years and fine.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '194':['Giving or fabricating false evidence with intent to cause any person to be convicted of capital offence.', 'Imprisonment for life, or rigorous imprisonment for 10 years and fine.', 'Non-Cognizable', 'Non-Bailable', 'Court of Session.'],
    '195':['Giving or fabricating false evidence with intent to procure conviction of an offence punishable with imprisonment for life or with imprisonment for 7 years, or upwards.', 'The same as for the offence.', 'Non-Cognizable', 'Non-Bailable', 'Court of Session.'],
    '195A':['Threatening any person to give false evidence.', 'Imprisonment for 7 years, or fine, or both.', 'Cognizable', 'Non-Bailable', 'Court by which offence of giving false evidence is triable.'],
    '196':['Using in a judicial proceeding evidence known to be false or fabricated.', 'The same as for giving or fabricating false evidence.', 'Non-Cognizable', 'According as offence of giving such evidence is bailable or nonbailable.','Court by which offence of giving or fabricating false evidence is triable.'],
    '197':['Knowingly issuing or signing a false certificate relating to any fact of which such certificate is by law admissible in evidence.', 'The same as for giving or fabricating false evidence.', 'Non-Cognizable', 'Bailable', 'Court by which offence of giving or fabricating false evidence is triable.'],
    '198':['Using as a true certificate one known to be false in a material point.', 'The same as for giving or fabricating false evidence.', 'Non-Cognizable', 'Bailable', 'Court by which offence of giving or fabricating false evidence is triable.'],
    '199':['False statement made in any declaration which is by law receivable as evidence. ', 'The same as for giving or fabricating false evidence.', 'Non-Cognizable', 'Bailable', 'Court by which offence of giving or fabricating false evidence is triable.'],
    '200':['Using as true any such declaration known to be false.', 'The same as for giving or fabricating false evidence.', 'Non-Cognizable', 'Bailable', 'Court by which offence of giving or fabricating false evidence is triable.'],
    '201':['Causing disappearance of evidence of an offence committed, or giving false information touching it to screen the offender, if a capital offence.', 'Imprisonment for 7 years and fine.', 'According as the offence in relation to which disappearance of evidence is caused is cognizable or noncognizable.', 'Bailable', 'Court of Session.'],
    '202':['Intentional omission to give information of an offence by a person legally bound to inform.', 'Imprisonment for 6 months, or fine, or both. ', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],   
    '203':['Giving false information respecting an offence committed.', 'Imprisonment for 2 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],    
    '204':['Secreting or destroying any document to prevent its production as evidence.', 'Imprisonment for 2 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],    
    '205':['False personation for the purpose of any act or proceeding in a suit or criminal prosecution, or for becoming bail or security.', 'Imprisonment for 3 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '206':['Fraudulent removal or concealment, etc., of property to prevent its seizure as a forfeiture or in satisfaction of a fine under sentence, or in execution of a decree.', 'Imprisonment for 2 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '207':['Claiming property without right, or practicing deception touching any right to it, to prevent its being taken as a forfeiture, or in satisfaction of a fine under sentence, or in execution of a decree.', 'Imprisonment for 2 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '208':['Fraudulently suffering a decree to pass for a sum not due, or suffering decree to be executed after it has been satisfied.', 'Imprisonment for 2 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '209':['False claim in a Court of Justice.', 'Imprisonment for 2 years and fine.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '210':['Fraudulently obtaining a decree for a sum not due, or causing a decree to be executed after it has been satisfied.', 'Imprisonment for 2 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '211':['False charge of offence made with intent to injure.', 'Imprisonment for 2 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '212':['Harbouring an offender, if the offence be capital.', 'Imprisonment for 5 years and fine.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '213':['Taking gift, etc., to screen an offender from punishment if the offence be capital.', 'Imprisonment for 7 years and fine.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '214':['Offering gift or restoration of property in consideration of screening offender if the offence be capital.', 'Imprisonment for 7 years and fine.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '215':['Taking gift to help to recover movable property of which a person has been deprived by an offence without causing apprehension of offender.', 'Imprisonment for 2 years, or fine, or both.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '216':['Harbouring an offender who has escaped from custody, or whose apprehension has been ordered, if the offence be capital.', 'Imprisonment for 7 years and fine.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    
    '216A':['Harbouring robbers or dacoits.', 'Rigorous imprisonment for 7 years and fine.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '217':['Public servant disobeying a direction of law with intent to save person from punishment, or property from forfeiture.', 'Imprisonment for 2 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '218':['Public servant framing an incorrect record or writing with intent to save person from punishment, or property from forfeiture.', 'Imprisonment for 3 years, or fine, or both.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '219':['Public servant in a judicial proceeding corruptly making and pronouncing an order, report, verdict, or decision which he knows to be contrary to law.', 'Imprisonment for 7 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '220':['Commitment for trial or confinement by a person having authority, who knows that he is acting contrary to law.', 'Imprisonment for 7 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '221':['Intentional omission to apprehend on the part of a public servant bound by law to apprehend an offender, if the offence be capital.', 'Imprisonment for 7 years, with or without fine.', 'According as the offence in relation to which such omission has been made is cognizable or noncognizable.', 'Bailable', 'Magistrate of the first class.'],
    '222':['Intentional omission to apprehend on the part of a public servant bound by law to apprehend person under sentence of a Court of Justice if under sentence of death.', 'Imprisonment for life, or imprisonment for 14 years, with or without fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '223':['Escape from confinement negligently suffered by a public servant.', 'Simple imprisonment for 2 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '224':['Resistance or obstruction by a person to his lawful apprehension.', 'Imprisonment for 2 years, or fine, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.',],
    '225':['Resistance or obstruction to the lawful apprehension of any person, or rescuing him from lawful custody.', 'Imprisonment for 2 years, or fine, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '225A':['Omission to apprehend, or sufferance of escape on part of public servant, in cases not otherwise provided for:– (a) in case of intentional omission or sufferance.', 'Imprisonment for 3 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '225B':['Resistance or obstruction to lawful apprehension, or escape or rescue in cases not otherwise provided for.', 'Imprisonment for 6 months, or fine, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '227':['Violation of condition of remission of punishment.', 'Punishment of original sentence, or if part of the punishment has been undergone, the residue.', 'Cognizable', 'Bailable', 'The Court by which the original offence was triable.'],
    '228':['Intentional insult or interruption to a public servant sitting in any stage of a judicial proceeding.', 'Simple imprisonment for 6 months, or fine of 1,000 rupees, or both.', 'Non-Cognizable', 'Bailable', 'The Court in which the offence is committed subject to the provisions of Chapter XXVI.'],
    '228A':['Disclosure of identity of the victim of certain offences, etc.', 'Imprisonment for two years and fine.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '229':['Personation of a juror or assessor.', 'Imprisonment for 2 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '229A':['Failure by person released on bail or bond to appear in Court', 'Imprisonment for 1 year, or fine, or both', 'Cognizable', 'Non-Bailable', 'Any Magistrate.'],

    '231':['Counterfeiting, or performing any part of the process of counterfeiting, coin.', 'Imprisonment for 7 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '232':['Counterfeiting, or performing any part of the process of counterfeiting, Indian coin.', 'Imprisonment for life, or imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Sessions.'],
    '233':['Making, buying or selling instrument for the purpose of counterfeiting coin.', 'Imprisonment for 3 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '234':['Making, buying or selling instrument for the purpose of counterfeiting Indian coin.', 'Imprisonment for 7 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Sessions.'],
    '235':['Possession of instrument or material for the purpose of using the same for counterfeiting coin.', 'Imprisonment for 3 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'], 
    '236':['Abetting, in India, the counterfeiting, out of India, of coin.', 'The punishment provided for abetting the counterfeiting of such coin within India.', 'Cognizable', 'Non-Bailable', 'Court of Sessions.'],
    '237':['Import or export of counterfeit coin, knowing the same to be counterfeit.', 'Imprisonment for 3 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '238':['Import or export of counterfeit of Indian coin, knowing the same to be counterfeit.', 'Imprisonment for life, or imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Sessions.'],
    '239':['Having any counterfeit coin known to be such when it came into possession, and delivering, etc., the same to any person.', 'Imprisonment for 5 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '240':['Same with respect to Indian coin.', 'Imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Sessions.'],
    '241':['Knowingly delivering to another any counterfeit coin as genuine, which, when first possessed, the deliverer did not know to be counterfeit.', 'Imprisonment for 2 years, or fine, or 10 times the value of the coin counterfeited, or both.', 'Cognizable', 'Non-Bailable', 'Any Magistrate.'],
    '242':['Possession of counterfeit coin by a person who knew it to be counterfeit when he became possessed thereof.', 'Imprisonment for 3 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'], 
    '243':['Possession of Indian coin by a person who knew it to be counterfeit when he became possessed thereof.', 'Imprisonment for 7 years and fine', 'Cognizable', 'Non-Bailable', 'Any Magistrate.'],
    '244':['Person employed in a Mint causing coin to be of a different weight or composition from that fixed by law.', 'Imprisonment for 7 years and fine', 'Cognizable', 'Non-Bailable', 'Any Magistrate.'],
    '245':['Unlawfully taking from a Mint any coining instrument.', 'Imprisonment for 7 years and fine', 'Cognizable', 'Non-Bailable', 'Any Magistrate.'],
    '246':['Fraudulently diminishing the weight or altering the composition of any coin.', 'Imprisonment for 3 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'], 
    '247':['Fraudulently diminishing the weight or altering the composition of Indian coin.', 'Imprisonment for 7 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '248':['Altering appearance of any coin with intent that it shall pass as a coin of a different description.', 'Imprisonment for 3 years and fine. ', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '249':['Altering appearance of Indian coin with intent that it shall pass as a coin of a different description.', 'Imprisonment for 7 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '250':['Delivery to another of coin possessed with the knowledge that it is altered.', 'Imprisonment for 5 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '251':['Delivery of Indian coin possessed with the knowledge that it is altered.', 'Imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '252':['Possession of altered coin by a person who knew it to be altered when he became possessed thereof', 'Imprisonment for 3 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '253':['Possession of Indian coin by a person who knew it to be altered when he became possessed thereof.', 'Imprisonment for 5 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '254':['Delivery to another of coin as genuine which, when first possessed, the deliverer did not know to be altered.', 'Imprisonment for 2 years or fine, or 10 times the value of the coin.', 'Cognizable', 'Non-Bailable', 'Any Magistrate.'],
    '255':['Counterfeiting a Government stamp.', 'Imprisonment for life, or imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '256':['Having possession of an instrument or material for the purpose of counterfeiting a Government stamp.', 'Imprisonment for 7 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '257':['Making, buying or selling instrument for the purpose of counterfeiting a Government stamp.', 'Imprisonment for 7 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'], 
    '258':['Sale of counterfeit Government stamp.', 'Imprisonment for 7 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '259':['Having possession of a counterfeit Government stamp.', 'Imprisonment for 7 years and fine.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '260':['Using as genuine a Government stamp known to be counterfeit.', 'Imprisonment for 7 years, or fine, or both.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '261':['Effacing any writing from a substance bearing a Government stamp, removing from a document a stamp used for it, with intent to cause a loss to Government.', 'Imprisonment for 3 years, or fine, or both.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '262':['Using a Government stamp known to have been before used.', 'Imprisonment for 2 years, or fine, or both.', 'Cognizable', 'Non-Bailable', 'Any Magistrate.'],
    '263':['Erasure of mark denoting that stamps have been used.', 'Imprisonment for 3 years, or fine, or both.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '263A':['Fictitious stamps', 'Fine of 200 rupees', 'Cognizable', 'Non-Bailable', 'Any Magistrate.'],
    
    '264':['Fraudulent use of false instrument for weighing.', 'Imprisonment for 1 year, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '265':['Fraudulent use of false weight or measure.', 'Imprisonment for 1 year, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '266':['Being in possession of false weights or measures for fraudulent use.', 'Imprisonment for 1 year, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '267':['Making or selling false weights or measures for fraudulent use.', 'Imprisonment for 1 year, or fine, or both.', 'Cognizable', 'Non-Bailable', 'Any Magistrate.'],

    '269':['Negligently doing any act known to be likely to spread infection of any disease dangerous to life.', 'Imprisonment for 6 months, or fine, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '270':['Malignantly doing any act known to be likely to spread infection of any disease dangerous to life.', 'Imprisonment for 2 years, or fine, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '271':['Knowingly disobeying any quarantine rule.', 'Imprisonment for 6 months, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '272':['Adulterating food or drink intended for sale, so as to make the same noxious.', 'Imprisonment for 6 months, or fine of 1,000 rupees, or both', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '273':['Selling any food or drink as food and drink, knowing the same to be noxious.', 'Imprisonment for 6 months, or fine of 1,000 rupees, or both', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '274':['Adulterating any drug or medical preparation intended for sale so as to lessen its efficacy, or to change its operation, or to make it noxious.', 'Imprisonment for 6 months, or fine of 1,000 rupees, or both', 'Non-Cognizable', 'Non-Bailable', 'Any Magistrate.'],
    '275':['Offering for sale or issuing from a dispensary any drug or medical preparation known to have been adulterated.', 'Imprisonment for 6 months, or fine of 1,000 rupees, or both', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '276':['Knowingly selling or issuing from a dispensary any drug or medical preparation as a different drug or medical preparation.', 'Imprisonment for 6 months, or fine of 1,000 rupees, or both', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '277':['Defiling the water of a public spring or reservoir.', 'Imprisonment for 3 months, or fine of 500 rupees, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '278':['Making atmosphere noxious to health.', 'Fine of 500 rupees', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '279':['Driving or riding on a public way so rashly or negligently as to endanger human life, etc.', 'Imprisonment for 6 months, or fine of 1,000 rupees, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '280':['Navigating any vessel so rashly or negligently as to endanger human life, etc.', 'Imprisonment for 6 months, or fine of 1,000 rupees, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '281':['Exhibition of a false light, mark or buoy.', 'Imprisonment for 7 years, or fine, or both.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '282':['Conveying for hire any person by water, in a vessel in such a state, or so loaded, as to endanger his life.', 'Imprisonment for 6 months, or fine of 1,000 rupees, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '283':['Causing danger, obstruction or, injury in any public way or line of navigation.', 'Fine of 200 rupees.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '284':['Dealing with any poisonous substance so as to endanger human life, etc.', 'Imprisonment for 6 months, or fine of 1,000 rupees, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '285':['Dealing with fire or any combustible matter so as to endanger human life, etc.', 'Imprisonment for 6 months, or fine of 1,000 rupees, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '286':['So dealing with any explosive substance.', 'Imprisonment for 6 months, or fine of 1,000 rupees, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '287':['So dealing with any machinery.', 'Imprisonment for 6 months, or fine of 1,000 rupees, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '288':['A person omitting to guard against probable danger to human life by the fall of any building over which he has a right entitling him to pull it down or repair it.', 'Imprisonment for 6 months, or fine of 1,000 rupees, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '289':['A person omitting to take order with any animal in his possession, so as to guard against danger to human life, or of grievous hurt, from such animal.', 'Imprisonment for 6 months, or fine of 1,000 rupees, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '290':['Committing a public nuisance', 'Fine of 200 rupees', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '291':['Continuance of nuisance after injunction to discontinue.', 'Simple imprisonment for 6 months, or fine, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '292':['Sale, etc., of obscene books, etc.', 'On first conviction, with imprisonment for 2 years, and with fine of 2,000 rupees, and, in the event of second or subsequent conviction, with imprisonment for five years, and with fine of 5,000 rupees.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '293':['Sale, etc., of obscene objects to young persons.', 'On first conviction, with imprisonment for 3 years, and with fine of 2,000 rupees, and in the event of second or subsequent conviction, with imprisonment for 7 years, and with fine of 5,000 rupees.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '294':['Obscene songs', 'Imprisonment for 3 months, or fine or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '294A':['Keeping a lottery office', 'Imprisonment for 6 months, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '295':['Destroying, damaging or defiling a place of worship or sacred object with intent to insult the religion of any class of persons.', 'Imprisonment for 2 years, or fine or both.', 'Cognizable', 'Non-Bailable', 'Any Magistrate.'],
    '295A':['Maliciously insulting the religion or the religious beliefs of any class.', 'Imprisonment for 3 years, or fine, or both.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '296':['Causing a disturbance to an assembly engaged in religious worship.', 'Imprisonment for 1 year, or fine, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '297':['Trespassing in place of worship or sepulcher, disturbing funeral with intention to wound the feelings or to insult the religion of any person, or offering indignity to a human corpse.', 'Imprisonment for 1 year, or fine, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '298':['Uttering any word or making any sound in the hearing or making any gesture, or placing any object in the sight of any person, with intention to wound his religious feeling.', 'Imprisonment for 1 year, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
   
    '302':['Murder', 'Death, or imprisonment for life, and fine.', 'Cognizable', 'non-Bailable', 'Court of Session.'],
    '303':['Murder by a person under sentence of imprisonment for life.', 'Death', 'Cognizable', 'non-Bailable', 'Court of Session.'],
    '304':['Culpable homicide not amounting to murder, if act by which the death is caused is done with intention of causing death, etc.', 'Imprisonment for life, or imprisonment for 10 years and fine.', 'Cognizable', 'non-Bailable', 'Court of Session.'],
    '304A':['Causing death by rash or negligent act.', 'Imprisonment for 2 years, or fine, or both.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '304B':['Dowry death.', 'Imprisonment of not less than seven years but which may extend to imprisonment for life.', 'Cognizable', 'non-Bailable', 'Court of Session.'],
    '305':['Abetment of suicide committed by child, or insane or delirious person or an idiot, or a person intoxicated.', 'Death, or imprisonment for life, or imprisonment for 10 years and fine.', 'Cognizable', 'non-Bailable', 'Court of Session.'],
    '306':['Abetting the commission of suicide.', 'Imprisonment for 10 years and fine.', 'Cognizable', 'non-Bailable', 'Court of Session.'], 
    '307':['Attempt to murder', 'Imprisonment for 10 years and fine.', 'Cognizable', 'non-Bailable', 'Court of Session.'],
    '308':['Attempt to commit culpable homicide', 'Imprisonment for 3 years, or fine, or both.', 'Cognizable', 'non-Bailable', 'Court of Session.'],
    '309':['Attempt to commit suicide.', 'Simple imprisonment for 1 year, or fine, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '311':['Being a thug.', 'Imprisonment for life and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '312':['Causing miscarriage.', 'Imprisonment for 3 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '313':['Causing miscarriage without women’s consent.', 'Imprisonment for life, or imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '314':['Death caused by an act done with intent to cause miscarriage.', 'Imprisonment for 10 years and fine', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '315':['Act done with intent to prevent a child being born alive, or to cause it to die after its birth.', 'Imprisonment for 10 years, or fine, or both.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '316':['Causing death of a quick unborn child by an act amounting to culpable homicide.', 'Imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '317':['Exposure of a child under 12 years of age by parent or person having care of it with intention of wholly abandoning it.', 'Imprisonment for 7 years, or fine, or both.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '318':['Concealment of birth by secret disposal of dead body.', 'Imprisonment for 2 years, or fine, or both.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '323':['Voluntarily causing hurt.', 'Imprisonment for 1 year or fine of 1,000 rupees, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '324':['Voluntarily causing hurt by dangerous weapons or means.', 'Imprisonment for 3 years, or fine, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'], 
    '325':['Voluntarily causing grievous hurt.', 'Imprisonment for 7 years and fine.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '326':['Voluntarily causing grievous hurt by dangerous weapons or means.', 'Imprisonment for life, or imprisonment for 10 years and fine', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '326A':['Voluntarily causing grievous hurt by use of acid, etc.', 'Imprisonment for not less than 10 years but which may extend to imprisonment for life and fine to be paid to the victim.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '326B':['Voluntarily throwing or attempting to throw acid.', 'Imprisonment for 5 years but which may extend to 7 years and with fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '327':['Voluntarily causing hurt to extort property or a valuable security, or to constrain to do anything which is illegal or which may facilitate the commission of an offence.', 'Imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '328':['Administering stupefying drug with intent to cause hurt, etc.', 'Imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '329':['Voluntarily causing grievous hurt to extort property or a valuable security, or to constrain to do anything which is illegal, or which may facilitate the commission of an offence.', 'Imprisonment for life, or imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '330':['Voluntarily causing hurt to extort confession or information, or to compel restoration of property, etc.', 'Imprisonment for 7 years and fine.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '331':['Voluntarily causing grievous hurt to extort confession or information, or to compel restoration of property, etc.', 'Imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '332':['Voluntarily causing hurt to deter public servant from his duty.', 'Imprisonment for 3 years or fine or both.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '333':['Voluntarily causing grievous hurt to deter public servant from his duty.', 'Imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'], 
    '334':['Voluntarily causing hurt on grave and sudden provocation, not intending to hurt any other than the person who gave the provocation.', 'Imprisonment for 1 month, or fine of 500 rupees, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '335':['Causing grievous hurt on grave and sudden provocation, not intending to hurt any other than the person who gave the provocation.', 'Imprisonment for 4 years, or fine of 2,000 rupees, or both.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '336':['Doing any act which endangers human life or the personal safety of others.', 'Imprisonment for 3 months, or fine of 250 rupees, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '337':['Causing hurt by an act which endangers human life, etc.', 'Imprisonment for 6 months, or fine of 500 rupees, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '338':['Causing grievous hurt by an act which endangers human life, etc.', 'Imprisonment for 2 years, or fine of 1,000 rupees, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '341':['Wrongfully restraining any person.', 'Simple imprisonment for 1 month, or fine of 500 rupees, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '342':['Wrongfully confining any person.', 'Imprisonment for 1 year, or fine of 1,000 rupees, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '343':['Wrongfully confining for three or more days.', 'Imprisonment for 2 years, or fine, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '344':['Wrongfully confining for 10 or more days.', 'Imprisonment for 3 years and fine.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '345':['Keeping any person in wrongful confinement, knowing that a writ has been issued for his liberation.', 'Imprisonment for 2 years, in addition to imprisonment under any other section.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '346':['Wrongful confinement in secret.', 'Imprisonment for 2 years, in addition to imprisonment under any other section.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '347':['Wrongful confinement for the purpose of extorting property, or constraining to an illegal act, etc.', 'Imprisonment for 3 years and fine.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '348':['Wrongful confinement for the purpose of extorting confession or information, or of compelling restoration of property, etc.', 'Imprisonment for 3 years and fine.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '352':['Assault or use of criminal force otherwise than on grave provocation.', 'Imprisonment for 3 months, or fine of 500 rupees, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '353':['Assault or use of criminal force to deter a public servant from discharge of his duty.', 'Imprisonment for 2 years, or fine, or both.', 'Cognizable', 'Non-Bailable', 'Any Magistrate.'],
    '354':['Assault or use of criminal force to woman with intent to outrage her modesty.', 'Imprisonment of 1 year which may extend to 5 years, and with fine.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '354A':['Sexual harassment of the nature of unwelcome physical contact and advances or a demand or request for sexual favours, showing pornography.', 'Imprisonment which may extend to 3 years or with fine or with both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '354B':['Assault or use of criminal force to woman with intent to disrobe.', 'Imprisonment of not less than 3 years but which may extend to 7 years and with fine.', 'Cognizable', 'Non-Bailable', 'Any Magistrate.'],
    '354C':['Voyeurism.', 'Imprisonment of not less than 1 year but which may extend to 3 years and with fine for first conviction.', 'Cognizable', 'Bailable', 'Any Magistrate.'],    
    '354D':['Stalking.', 'Imprisonment up to 3 years and with fine for first conviction.', 'Cognizable', 'Bailable', 'Any Magistrate.'],    
    '355':['Assault or criminal force with intent to dishonor a person, otherwise than on grave and sudden provocation.', 'Imprisonment for 2 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '356':['Assault or criminal force in attempt to commit theft of property worn or carried by a person.', 'Imprisonment up to 5 years and with fine for second or subsequent conviction.', 'Cognizable', 'Non-vBailable', 'Any Magistrate.', ''],
    '357':['Assault or use of criminal force in attempt wrongfully to confine a person.', 'Imprisonment for 1 year, or fine of 1,000 rupees, or both.', 'Cognizable', 'Bailable', 'Any Magistrate'],
    '358':['Assault or use of criminal force on grave and sudden provocation.', 'Simple imprisonment for one month, or fine of 200 rupees, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate'],
    '363':['Kidnapping.', 'Imprisonment for 7 years and fine.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '363A':['Kidnapping or obtaining the custody of a minor in order that such minor may be employed or used for purposes of begging.', 'Imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '364':['Kidnapping or abducting in order to murder.', 'Imprisonment for life, or rigorous imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '364A':['Kidnapping for ransom, etc.', 'Death, or imprisonment for life and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '365':['Kidnapping or abducting with intent secretly and wrongfully to confine a person.', 'Imprisonment for 7 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '366':['Kidnapping or abducting a woman to compel her marriage or to cause her defilement, etc.', 'Imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '366A':['Procuration of a minor girl.', 'Imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '366B':['Importation of a girl from foreign country.', 'Imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '367':['Kidnapping or abducting in order to subject a person to grievous hurt, slavery, etc.', 'Imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '368':['Concealing or keeping in confinement a kidnapped person.', 'Punishment for kidnapping or abduction.', 'Cognizable', 'Non-Bailable', 'Court by which the kidnapping or abduction is triable.'],
    '369':['Kidnapping or abducting a child with intent to take property from the person of such child.', 'Imprisonment for 7 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '370':['Trafficking of person.', 'Imprisonment of not less than 7 years but which may extend to 10 years and with fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '370A':['Exploitation of a trafficked child.', 'Imprisonment of not less than 5 years but which may extend to 7 years and with fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '371':['Habitual dealing in slaves.', 'Imprisonment for life, or imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '372':['Selling or letting to hire a minor for purposes of prostitution, etc.', 'Imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '373':['Buying or obtaining possession of a minor for the same purposes.', 'Imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '374':['Unlawful compulsory labour.', 'Imprisonment for 1 year, or fine, or both.', 'Cognizable', 'Bailable', 'Any Magistrate'],
    '376':['Rape', 'Rigorous imprisonment of not less than 10 years but which may extend to imprisonment for life and with fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '376A':['Person committing an offence of rape and inflicting injury which causes death or causes the woman to be in a persistent vegetative state.', 'Rigorous imprisonment of not less than 20 years but which may extend to imprisonment for life which shall mean imprisonment for the remainder of that person’s natural life or with death.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '376AB':['Person committing an offence of rape on a woman under twelve years of age.', 'Rigorous imprisonment of not less than 20 years but which may extend to imprisonment for life which shall mean imprisonment for that person’s natural life and with fine or with death.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '376B':['Sexual intercourse by husband upon his wife during separation.', 'Imprisonment for not less than 2 years but which may extend to 7 years and with fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '376C':['Sexual intercourse by a person in authority.', 'Rigorous imprisonment for not less than 5 years but which may extend to 10 years and with fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'], 
    '376D':['Gang rape', 'Rigorous imprisonment for not less than 20 years but which may extend to imprisonment for life which shall mean imprisonment for the remainder of that person’s natural life and with fine to be paid to the victim.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '376DA':['Gang rape on a woman under sixteen years of age.', 'Imprisonment for life which shall mean imprisonment for the remainder of that person’s natural life and with fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '376DB':['Gang rape on woman under twelve years of age.', 'Imprisonment for life which shall mean imprisonment for the remainder of that person’s natural life and with fine or with death.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '376E':['Repeat offenders.', 'Imprisonment for life which shall mean imprisonment for the remainder of that person’s natural life or with death.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '377':['Unnatural offences', 'Imprisonment for life, or imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class'],

    '379':['Theft', 'Imprisonment for 3 years, or fine, or both. ', 'Cognizable', 'Non-Bailable', 'Any Magistrate.'],
    '380':['Theft in a building, tent or vessel', 'Imprisonment for 7 years and fine.', 'Cognizable', 'Non-Bailable', 'Any Magistrate.'],
    '381':['Theft by clerk or servant of property in possession of master or employer.', 'Imprisonment for 7 years and fine.', 'Cognizable', 'Non-Bailable', 'Any Magistrate.'],
    '382':['Theft, after preparation having been made for causing death, or hurt, or restraint, or fear of death, or of hurt, or of restraint, in order to the committing of such theft, or to retiring after committing it, or to retaining property taken by it.', 'Rigorous imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistarte of the first class.'],
    '384':['Extortion', 'Imprisonment for 3 years, or fine, or both.', 'Cognizable', 'Non-Bailable', 'Any Magistarte.'],
    '385':['Putting or attempting to put in fear of injury, in order to commit extortion.', 'Imprisonment for 2 years, or fine, or both.', 'Cognizable', 'Bailable', 'Any Magistarte.'],
    '386':['Extortion by putting a person in fear of death or grievous hurt.', 'Imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistarte of the first class.'],
    '387':['Putting or attempting to put a person in fear of death or grievous hurt in order to commit extortion.', 'Imprisonment for 7 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistarte of the first class.'],
    '388':['Extortion by threat of accusation of an offence punishable with death, imprisonment for life, or imprisonment for 10 years.', 'Imprisonment for 10 years and fine.', 'Cognizable', 'Bailable', 'Magistarte of the first class.'],
    '389':['Putting a person in fear of accusation of an offence punishable with death, imprisonment for life, or imprisonment for 10 years in order to commit extortion.', 'Imprisonment for 10 years and fine.', 'Cognizable', 'Bailable', 'Magistarte of the first class.'],
    '392':['Robbery.', 'Rigorous imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistarte of the first class.'],
    '393':['Attempt to commit robbery.', 'Rigorous imprisonment for 7 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistarte of the first class.'],
    '394':['Person voluntarily causing hurt in committing or attempting to commit robbery, or any other person jointly concerned in such robbery.', 'Imprisonment for life, or rigorous imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistarte of the first class.'],
    '395':['Dacoity', 'Imprisonment for life, or rigorous imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '396':['Murder in dacoity', 'Death, imprisonment for life, or rigorous imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '397':['Robbery or dacoity, with attempt to cause death or grievous hurt.', 'Rigorous imprisonment for not less than 7 years.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '398':['Attempt to commit robbery or dacoity when armed with deadly weapon.', 'Rigorous imprisonment for not less than 7 years.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '399':['Making preparation to commit dacoity.', 'Rigorous imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '400':['Belonging to a gang of persons associated for the purpose of habitually committing dacoity.', 'Imprisonment for life, or rigorous imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '401':['Belonging to a wandering gang of persons associated for the purpose of habitually committing thefts.', 'Rigorous imprisonment for 7 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'], 
    '402':['Being one of five or more persons assembled for the purpose of committing dacoity.', 'Rigorous imprisonment for 7 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '403':['Dishonest misappropriation of movable property, or converting it to one’s own use.', 'Imprisonment for 2 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '404':['Dishonest misappropriation of property, knowing that it was in possession of a deceased person at his death, and that it has not since been in the possession of any person legally entitled to it.', 'Imprisonment for 3 years and fine.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '406':['Criminal breach of trust.', 'Imprisonment for 3 years, or fine, or both.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '407':['Criminal breach of trust by a carrier, wharfinger, etc.', 'Imprisonment for 7 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '408':['Criminal breach of trust by a clerk or servant.', 'Imprisonment for 7 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '409':['Criminal breach of trust by public servant or by banker, merchant or agent, etc.', 'Imprisonment for life, or imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '411':['Dishonestly receiving stolen property knowing it to be stolen.', 'Imprisonment for 3 years, or fine, or both.', 'Cognizable', 'Non-Bailable', 'Any Magistrate.'],
    '412':['Dishonestly receiving stolen property, knowing that it was obtained by dacoity.', 'Imprisonment for life, or rigorous imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '413':['Habitually dealing in stolen property.', 'Imprisonment for life, or imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'], 
    '414':['Assisting in concealment or disposal of stolen property, knowing it to be stolen.', 'Imprisonment for 3 years, or fine, or both.', 'Cognizable', 'Non-Bailable', 'Any Magistrate.'],
    '417':['Cheating', 'Imprisonment for 1 year, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '418':['Cheating a person whose interest the offender was bound, either by law or by legal contract, to protect.', 'Imprisonment for 3 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '419':['Cheating by personation.', 'Imprisonment for 3 years, or fine, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '420':['Cheating and thereby dishonestly inducing delivery of property, or the making, alteration or destruction of a valuable security.', 'Imprisonment for 7 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '421':['Fraudulent removal or concealment of property, etc., to prevent distribution among creditors.', 'Imprisonment for 2 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '422':['Fraudulently preventing from being made available for his creditors a debt or demand due to the offender.', 'Imprisonment for 2 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '423':['Fraudulent execution of deed of transfer containing a false statement of consideration.', 'Imprisonment for 2 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '424':['Fraudulent removal or concealment of property, of himself or any other person or assisting in the doing thereof, or dishonestly releasing any demand or claim to which he is entitled.', 'Imprisonment for 2 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '426':['Mischief.', 'Imprisonment for 3 months or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '427':['Mischief, and thereby causing damage to the amount of 50 rupees or upwards.', 'Imprisonment for 2 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '428':['Mischief by killing, poisoning, maiming or rendering useless any animal of the value of 10 rupees or upwards.', 'Imprisonment for 2 years, or fine, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '429':['Mischief by killing, poisoning, maiming or rendering useless any elephant, camel, horse, etc., whatever may be its value, or any other animal of the value of 50 rupees or upwards.', 'Imprisonment for 5 years, or fine, or both.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'], 
    '430':['Mischief by causing diminution of supply of water for agricultural purposes, etc.', 'Imprisonment for 5 years, or fine, or both.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '431':['Mischief by injury to public road, bridge, navigable river, or navigable channel, and rendering it impassable or less safe for travelling or conveying property.', 'Imprisonment for 5 years, or fine, or both.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '432':['Mischief by causing inundation or obstruction to public drainage attended with damage.', 'Imprisonment for 5 years, or fine, or both.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '433':['Mischief by destroying or moving or rendering less useful a lighthouse or seamark, or by exhibiting false lights.', 'Imprisonment for 7 years, or fine, or both.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '434':['Mischief by destroying or moving, etc., a landmark fixed by public authority.', 'Imprisonment for 1 year, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],    '432':['', '', ''],
    '435':['Mischief by fire or explosive substance with intent to cause damage to an amount of 100 rupees or upwards, or, in case of agricultural produce, 10 rupees or upwards.', 'Imprisonment for 7 years and fine.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '436':['Mischief by fire or explosive substance with intent to destroy a house, etc.', 'Imprisonment for life, or imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'], 
    '437':['Mischief with intent to destroy or make unsafe a decked vessel or a vessel of 20 tonnes burden.', 'Imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'], 
    '438':['The mischief described in the last section when committed by fire or any explosive substance.', 'Imprisonment for life, or imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '439':['Running vessel ashore with intent to commit theft, etc.', 'Imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '440':['Mischief committed after preparation made for causing death, or hurt, etc.', 'Imprisonment for 5 years and fine.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '447':['Criminal trespass', 'Imprisonment for 3 months, or fine of 500 rupees, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '448':['House-trespass.', 'Imprisonment for 1 year, or fine of 1,000 rupees, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '449':['House-trespass in order to the commission of an offence punishable with death.', 'Imprisonment for life, or rigorous imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '450':['House-trespass in order to the commission of an offence punishable with imprisonment for life.', 'Imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '451':['House-trespass in order to the commission of an offence punishable with imprisonment.', 'Imprisonment for 2 years and fine.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '452':['House-trespass, having made preparation for causing hurt, assault, etc.', 'Imprisonment for 7 years and fine.', 'Cognizable', 'Non-Bailable', 'Any Magistrate.'],
    '453':['Lurking house-trespass or house-breaking.', 'Imprisonment for 2 years and fine.', 'Cognizable', 'Non-Bailable', 'Any Magistrate.'],
    '454':['Lurking house-trespass or house-breaking in order to the commission of an offence punishable with imprisonment.', 'Imprisonment for 3 years and fine.', 'Cognizable', 'Non-Bailable', 'Any Magistrate.'],
    '455':['Lurking house-trespass or house-breaking after preparation made for causing hurt, assault, etc.', 'Imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '456':['Lurking house-trespass or house-breaking by night.', 'Imprisonment for 3 years and fine.', 'Cognizable', 'Non-Bailable', 'Any Magistrate.'],
    '457':['Lurking house-trespass or house-breaking by night in order to the commission of an offence punishable with imprisonment.', 'Imprisonment for 5 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '458':['Lurking house-trespass or house-breaking by night, after preparation made for causing hurt, etc.', 'Imprisonment for 5 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '459':['Grievous hurt caused whilst committing lurking house-trespass or house-breaking.', 'Imprisonment for life, or imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '460':['Death or grievous hurt caused by one of several persons jointly concerned in housebreaking by night, etc.', 'Imprisonment for life, or imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '461':['Dishonestly breaking open or unfastening any closed receptacle containing or supposed to contain property.', 'Imprisonment for 2 years or fine, or both.', 'Cognizable', 'Non-Bailable', 'Any Magistrate.'],
    '462':['Being entrusted with any closed receptacle containing or supposed to contain any property, and fraudulently opening the same.', 'Imprisonment for 3 years or fine, or both.', 'Cognizable', 'Bailable', 'Any Magistrate.'],

    '465':['Forgery.', 'Imprisonment for 2 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '466':['Forgery of a record of a Court of Justice or of a Registrar of Births, etc., kept by a public servant.', 'Imprisonment for 7 years and fine', 'Non-Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '467':['Forgery of a valuable security, will, or authority to make or transfer any valuable security, or to receive any money, etc.', 'Imprisonment for life, or imprisonment for 10 years and fine.', 'Non-Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '468':['Forgery for the purpose of cheating.', 'Imprisonment for 7 years and fine.', 'Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '469':['Forgery for the purpose of harming the reputation of any person or knowing that it is likely to be used for that purpose.', 'Imprisonment for 3 years and fine.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '471':['Using as genuine a forged document which is known to be forged.', 'Punishment for forgery of such document.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '472':['Making or counterfeiting a seal, plate, etc., with intent to commit a forgery punishable under section 467 of the Indian Penal Code, or possessing with like intent any such seal, plate, etc., knowing the same to be counterfeit.', 'Imprisonment for life, or imprisonment for 7 years and fine.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '473':['Making or counterfeiting a seal, plate, etc., with intent to commit a forgery punishable otherwise than under section 467 of the Indian Penal Code, or possessing with like intent any such seal, plate, etc., knowing the same to be counterfeit.', 'Imprisonment for 7 years and fine.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '474':['Having possession of a document, knowing it to be forged, with intent to use it as genuine; if the document is one of the description mentioned in section 466 of the Indian Penal Code.', 'Imprisonment for 7 years and fine.', 'Cognizable', 'Bailable', 'Magistrate of the first class.'], 
    '475':['Counterfeiting a device or mark used for authenticating documents described in section 467 of the Indian Penal Code, or possessing counterfeit marked material.', 'Imprisonment for life, or imprisonment for 7 years and fine.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '476':['Counterfeiting a device or mark used for authenticating documents other than those described in section 467 of the Indian Penal Code, or possessing counterfeit marked material.', 'Imprisonment for 7 years and fine.', 'Non-Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '477':['Fraudulently destroying or defacing, or attempting to destroy or deface, or secreting, a will, etc.', 'Imprisonment for life, or imprisonment for 7 years and fine.', 'Non-Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],    
    '477A':['Falsification of accounts.', 'Imprisonment for 7 years or fine, or both.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '482':['Using a false property mark with intent to deceive or injure any person.', 'Imprisonment for 1 year, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '483':['Counterfeiting a property mark used by another, with intent to cause damage or injury.', 'Imprisonment for 2 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '484':['Counterfeiting a property mark used by a public servant, or any mark used by him to denote the manufacture, quality, etc., of any property.', 'Imprisonment for 3 years and fine.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '485':['Fraudulently making or having possession of any die, plate or other instrument for counterfeiting any public or private property mark.', 'Imprisonment for 3 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],    '484':['', '', ''],
    '486':['Knowingly selling goods marked with a counterfeit property mark.', 'Imprisonment for 1 year, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '487':['Fraudulently making a false mark upon any package or receptacle containing goods, with intent to cause it to be believed that it contains goods, which it does not contain, etc.', 'Imprisonment for 3 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '488':['Making use of any such false mark.', 'Imprisonment for 3 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '489':['Removing, destroying or defacing property mark with intent to cause injury.', 'Imprisonment for 1 year, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '490A':['Counterfeiting currency-notes or bank-notes.', 'Imprisonment for life, or imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '489B':['Using as genuine forged or counterfeit currency-notes or banknotes.', 'Imprisonment for life, or imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '489C':['Possession of forged or counterfeit currency-notes or bank-notes.', 'Imprisonment for 7 years, or fine, or both.', 'Cognizable', 'Bailable', 'Court of Session.'],
    '489D':['Making or possessing machinery, instrument or material for forging or counterfeiting currency-notes or bank-notes.', 'Imprisonment for life, or imprisonment for 10 years and fine.', 'Cognizable', 'Non-Bailable', 'Court of Session.'],
    '489E':['Making or using documents resembling currency-notes or banknotes.', 'Fine of 100 rupees.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '490':['On refusal to disclose the name and address of the printer','Fine of 200 rupees','Non-Cognizable', 'Bailable', 'Any Magistrate.'],
   
    '491':['Being bound to attend on or supply the wants of a person who is helpless from youth, unsoundness of mind or disease, and voluntarily omitting to do so.', 'Imprisonment for 3 months, or fine of 200 rupees, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],

    '493':['A man by deceit causing a woman not lawfully married to him to believe, that she is lawfully married to him and to cohabit with him in that belief.', 'Imprisonment for 10 years and fine.', 'Non-Cognizable', 'Non-Bailable', 'Magistrate of the first class.'],
    '494':['Marrying again during the life time of a husband or wife.', 'Imprisonment for 7 years and fine.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '495':['Same offence with concealment of the former marriage from the person with whom subsequent marriage is contracted.', 'Imprisonment for 10 years and fine.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '496':['A person with fraudulent intention going through the ceremony of being married, knowing that he is not thereby lawfully married.', 'Imprisonment for 7 years and fine.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'], 
    '497':['Adultery', 'Imprisonment for 5 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '498':['Enticing or taking away or detaining with a criminal intent a married woman.', 'Imprisonment for 2 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],

    '498A':['Punishment for subjecting a married woman to cruelty.', 'Imprisonment for three years and fine.', 'Cognizable if information relating to the commission of the offence is given to an officer in charge of a police station by the person aggrieved by the offence or by any person related to her by blood, marriage or adoption or if there is no such relative, by any public servant belonging to such class or category as may be notified by the State Government in this behalf.', 'Non-Bailable', 'Magistrate of the first class.'],

    '500':['Defamation against the President or the Vice-President or the Governor of a State or Administrator of a Union territory or a Minister in respect of his conduct in the discharge of his public functions when instituted upon a complaint made by the Public Prosecutor.', 'Simple imprisonment for 2 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Court of Session.'],
    '501':['(a) Printing or engraving matter knowing it to be defamatory against the President or the Vice-President or the Governor of a State or Administrator of a Union territory or a Minister in respect of his conduct in the discharge of his public functions when instituted upon a complaint made by the Public Prosecutor.', 'Simple imprisonment for 2 years, or fine, or both.' 'Non-Cognizable', 'Bailable', 'Court of Session.'],
    '502':['(a) Sale of printed or engraved substance containing defamatory matter, knowing it to contain such matter against the President or the Vice-President or the Governor of a State or Administrator of a Union territory or a Minister in respect of his conduct in the discharge of his public functions when instituted upon a complaint made by the Public Prosecutor.', 'Simple imprisonment for 2 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Court of Session.'],
    

    '504':['Insult intended to provoke breach of the peace.', 'Imprisonment for 2 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '505':['False statement, rumour, etc., circulated with intent to cause mutiny or offence against the public peace.', 'Imprisonment for 3 years, or fine, or both.', 'Non-Cognizable', 'Non-Bailable', 'Any Magistrate.'],
    '506':['Criminal intimidation.', 'Imprisonment for 2 years, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '507':['Criminal intimidation by anonymous communication or having taken precaution to conceal whence the threat comes.', 'Imprisonment for 2 years, in addition to the punishment under above section.', 'Non-Cognizable', 'Bailable', 'Magistrate of the first class.'],
    '508':['Act caused by inducing a person to believe that he will be rendered an object of Divine displeasure.', 'Imprisonment for 1 year, or fine, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],
    '509':['Uttering any word or making any gesture intended to insult the modesty of a woman, etc.', 'Simple imprisonment for 3 years and with fine.', 'Cognizable', 'Bailable', 'Any Magistrate.'],
    '510':['Appearing in a public place, etc., in a state of intoxication, and causing annoyance to any person.', 'Simple imprisonment for 24 hours, or fine of 10 rupees, or both.', 'Non-Cognizable', 'Bailable', 'Any Magistrate.'],

    '511':['Attempting to commit offences punishable with imprisonment for life, or imprisonment, and in such attempt doing any act towards the commission of the offence.', 'Imprisonment for life, or imprisonment not exceeding half of the longest term provided for the offence, or fine, or both', 'According as the offence is cognizable or non-cognizable.', 'According as the offence attempted by the offender is bailable or not.', 'The court by which the offence attempted is triable.'],    
 }
print()
print()
# p=re.compile(r'[0-9]+[A-Z]+')
# p2=re.compile(r'[0-9]+')
p3=re.compile(r'[0-9A-Z]+')
# l1=[]
# l2=[]
l3=[]
for e in d1.keys():
#     m=p.findall(e)
#     m1=p2.findall(e)
      m3=p3.findall(e)
#     # print(m)
#     l1+=m
#     l2+=m1
      l3+=m3
# # l2=list(set(l2))
# l2=list(map(int,l2))
# print(l2)
# # print(b)
# # print(c)
# print(l3)
def check(n):
    t=l3.index(n)
    if t>=l3.index("109") and t<=l3.index("120"):
         print("CHAPTER V","\n","ABETMENT.")
    elif t==l3.index("120B"):
         print("CHAPTER V-A","\n","CRIMINAL CONSPIRACY.")
    elif t>=l3.index("121") and t<=l3.index("130"):
         print("CHAPTER VI","\n","OFENCE AGAINST THE STATE.")
    elif t>=l3.index("131") and t<=l3.index("140"):
         print("CHAPTER VII","\n","OFFENCE RELATING TO THE ARMY, NAVY AND AIR FORCE.")
    elif t>=l3.index("143") and t<=l3.index("160"):
         print("CHAPTER VIII","\n","OFFENCE AGAINST THE PUBLIC TRANQUILLITY.")
    elif t>=l3.index("161") and t<=l3.index("171"):
         print("CHAPTER IX","\n","OFFENCE BY OR RELATING TO PUBLIC SERVANTS.")
    elif t>=l3.index("171E") and t<=l3.index("171I"):
         print("CHAPTER IX-A","\n","OFFENCES RELATING TO ELECTIONS.")
    elif t>=l3.index("172") and t<=l3.index("190"):
         print("CHAPTER X","\n","CONTEMPTS OF THE LAWFUL AUTHORITY OF PUBLIC SERVANTS.")   
    elif t>=l3.index("193") and t<=l3.index("229A"):
         print("CHAPTER XI","\n","FALSE EVIDENCE AND OFFENCES AGAINST PUBLIC JUSTICE.") 
    elif t>=l3.index("231") and t<=l3.index("263A"):
         print("CHAPTER XII","\n","OFFENCES RELATING TO COINS AND GOVERNMENT STAMPS.") 
    elif t>=l3.index("264") and t<=l3.index("267"):
         print("CHAPTER XIII","\n","OFFENCE RELATING TO WEIGTHS AND MEASURES.") 
    elif t>=l3.index("269") and t<=l3.index("294A"):
         print("CHAPTER XIV","\n","OFFENCES AFFECTING THE PUBLIC HEALTH, SAFETY, CONVENIENCE, DECENCY AND MORALS.") 
    elif t>=l3.index("295") and t<=l3.index("298"):
         print("CHAPTER XV","\n","OFFENCES RELATING TO RELEGION.")
    elif t>=l3.index("302") and t<=l3.index("377"):
         print("CHAPTER XVI","\n","OFFENCES AFFECTING THE HUMAN BODY.") 
    elif t>=l3.index("379") and t<=l3.index("462"):
         print("CHAPTER XVII","\n","OFFENCES AGAINST PROPERTY.") 
    elif t>=l3.index("465") and t<=l3.index("490"):
         print("CHAPTER XVIII","\n","OFFENCES RELATING TO DOCUMENTS AND TO PROPERTY MARKS.") 
    elif t==l3.index("491"):
         print("CHAPTER XIX","\n","CRIMINAL BREACH OF CONTRACTS AND SERVICE.") 
    elif t>=l3.index("493") and t<=l3.index("498"):
         print("CHAPTER XX","\n","OFFENCES RELATING TO MARRAIGE.") 
    elif t==l3.index("498A"):
         print("CHAPTER XX-A","\n","OF CRUELTY BY HUSBAND OR RELATIVES OF HUSBAND.") 
    elif t>=l3.index("500") and t<=l3.index("502"):
         print("CHAPTER XXI","\n","DEFAMATION.")
    elif t>=l3.index("504") and t<=l3.index("510"):
         print("CHAPTER XXII","\n","CRIMINAL INTIMIDATION, INSULT AND ANNOYANCE.")   
    elif t==l3.index("511"):
         print("CHAPTER XXIII","\n","ATTEMPTS TO COMMIT OFFENCES.")    
         
    print()
    if n in d1.keys():
      for i,j in d1.items():
          if n==i: 
             print('Offence:-','\n',j[0],'\n')
             print('Punishment:-','\n',j[1],'\n')
             print('Cognizable or non-cognizable:-','\n',j[2],'\n')
             print('Bailable or non-bailable:-','\n',j[3],'\n')
             print('By what court triable:-','\n',j[4],'\n')    
    if n in d2.keys():
      for i1,j1 in d2.items():
          if n==i1:
             print('Offence:-','\n',j1[0],'\n')
             print('Punishment:-','\n',j1[1],'\n')
             print('Cognizable or non-cognizable:-','\n',j1[2],'\n')
             print('Bailable or non-bailable:-','\n',j1[3],'\n')
             print('By what court triable:-','\n',j1[4],'\n')
    if n in d3.keys():
      for i2,j2 in d3.items():
          if n==i2:
             print('Offence:-','\n',j2[0],'\n')
             print('Punishment:-','\n',j2[1],'\n')
             print('Cognizable or non-cognizable:-','\n',j2[2],'\n')
             print('Bailable or non-bailable:-','\n',j2[3],'\n')
             print('By what court triable:-','\n',j2[4],'\n')
    if n in d4.keys():
      for i2,j2 in d4.items():
          if n==i2:
             print('Offence:-','\n',j2[0],'\n')
             print('Punishment:-','\n',j2[1],'\n')
             print('Cognizable or non-cognizable:-','\n',j2[2],'\n')
             print('Bailable or non-bailable:-','\n',j2[3],'\n')
             print('By what court triable:-','\n',j2[4],'\n')
    if n in d5.keys():
      for i2,j2 in d5.items():
          if n==i2:
             print('Offence:-','\n',j2[0],'\n')
             print('Punishment:-','\n',j2[1],'\n')
             print('Cognizable or non-cognizable:-','\n',j2[2],'\n')
             print('Bailable or non-bailable:-','\n',j2[3],'\n')
             print('By what court triable:-','\n',j2[4],'\n')
    if n in d6.keys():
      for i2,j2 in d6.items():
          if n==i2:
             print('Offence:-','\n',j2[0],'\n')
             print('Punishment:-','\n',j2[1],'\n')
             print('Cognizable or non-cognizable:-','\n',j2[2],'\n')
             print('Bailable or non-bailable:-','\n',j2[3],'\n')
             print('By what court triable:-','\n',j2[4],'\n')
def entry():
    print("Enter the section No. of I.P.C:")
    n=input()
    check(n)
entry()
if __name__ == "__main__":
 check("511")
