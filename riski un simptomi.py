print("Ko jus gribat uzzinat?")
print("")
print("1. Manu risku saslimt ar slimibam, ko izraisa virusi un bakterijas;") 
print("2.Vai man ir jaapmekle arsts")
print("*Izveleties visvairak piemerotu jums atbildes variantu")
print("*Atbilde rakstiet ciparu")
sakums=int(input())
if sakums==1: 
    print("1.Vai esi vakcinejis no iedomatas slimibas?")
    print("")
    print("1.Ja")
    print("2.Ne")
    vakcina=int(input())
    slim=0
    if vakcina==1: slim=0-5
    elif vakcina==2: slim=0+5
    else: print("nav tadas atbildes")
    print("")
    print("2.Vai jus valkat sejas masku publikas vietas?")
    print("")
    print("1.Ja")
    print("2.Ne")
    maska=int(input())
    if maska==1: slim=0-2
    elif maska==2: slim=0+2
    else: print("nav tadas atbildes")
    print("")
    print("3.Vai jus mazgajat/dezinficejat rokas pec pastaigas ara, mijiedarbibas ar dzivniekiem, tualetes apmeklesanas un pirms esanas?")
    print("")
    print("1.Ja")
    print("2.Ne")
    rokas=int(input())
    if rokas==1: slim=0-3
    elif rokas==2: slim=0+3
    else: print("nav tadas atbildes")
    print("")
    print("4.Vai jus ieverojat socialo distanci (2m) publiskas vietas?")
    print("")
    print("1.Ja")
    print("2.Ne")
    metri=int(input())
    if metri==1: slim=0-3
    elif metri==2: slim=0+3
    else: print("nav tadas atbildes")
    print("")
    print("5. Cik biezi jus apmeklejat publikas vietas/atradaties starp liela cilveku skaita?")
    print("")
    print("1.loti biezi")
    print("2.biezi")    
    print("3.reti")
    print("4.gandriz nekad")
    laudis=int(input())
    if laudis==1: slim=0+3
    elif laudis==2: slim=0+2
    elif laudis==3: slim=0+0
    elif laudis==4: slim=0-2
    else: print("nav tadas atbildes")
    print("")
    print("6. Vai jus pastiprinat savu imunitati?")
    print("*Sportojiet, jums ir veseligs uzturs, biezi pastajgajaties svaiga gaisa u.c.")
    print("1.Ja")
    print("2.Ne")
    imun=int(input())
    if imun==1: slim=0-4
    elif imun==2: slim=0+4
    else: print("nav tadas atbildes") 
    print("")
    print("7.Vai jums ir kadas hroniskas slimibas?")
    print("1.Ja")
    print("2.Ne")
    hron=int(input())
    if hron==1: slim=0+5
    elif hron==2: slim=0-5
    else:print("nav tadas atbildes")
    if -25<=slim<-10: print("Tavs risks saslimt ar vienu no slimibam, ko izraisa virusi un bakterijas ir loti zems. Tev nav jauztraucas!")
    elif -10<=slim<0: print("Tavs risks saslimt ar vienu no slimibam, ko izraisa virusi un bakterijas ir zems. Tev nav jauztraucas!")
    elif slim==0: print("Tavs risks saslimt ar vienu no slimibam, ko izraisa virusi un bakterijas ir videjs. Neaizmirsi verot savu veselibu!")
    elif 0<slim<=10: print("Tavs risks saslimt ar vienu no slimibam, ko izraisa virusi un bakterijas ir augsts. Esi uzmanigs!")
    else:  print("Tavs risks saslimt ar vienu no slimibam, ko izraisa virusi un bakterijas ir parak augsts. Esi loti uzmanigs!")
    print("")
    print("Vai velies velreiz pildit so testu?")
    print("1.Ja")
    print("2.Ne")
    test1=int(input())
    if test1==2: print("Jauku dienu!")
if sakums==2: 
   print("1. Pedejas dienas jus jitaties nogurusi?")
   print("1.Ja")
   print("2. Ne")
   nog=int(input())
   slim2=0
   if nog==1: slim2=0+2
   elif nog==2: slim2=0+0
   else: print("nav tadas atbildes.")
   print("")
   print("2. Jums ir paaugstinata kermena temperatura?")
   print("1. Ja, mana temperatura ir 38-40 gr.")
   print("2. Ja, mana temperatura ir 37 gr.")
   print("3. Ne")
   tem=int(input))
   if tem==1: slim2=0+4
   elif tem==2: slim2=0+1
   elif tem==3: slim2=0+0
   print("")
   print("3.Vai jums ir iesnas?")
   print("1.Ja")
   print("2. Ne")
   ies=int(input())
   if ies==1: slim2=0+2
   elif ies==: slim2=0+0
   print("")
   print("4. Vai jus zaudejat ozu?")
   print("1.Ja")
   print("2. Ne")
   oza=int(input())
   if oza==1: slim2=0+4
   elif oza==2: slim2=0+0
   else: print("nav tadas atbildes")
   print("")
   print("5. Jusu acis atri nogurst un sap?")
   print("1.Ja")
   print("2. Ne")
   acis=int(input())
   if acis==1: slim2=0+4
   elif acis==2: slim2=0+0
   else: print("nav tadas atbildes")
   print("")
   print("6.Jums ir smags klepus / iekaisis kakls?")
   print("1.Ja")
   print("2. Ne")
   klepus=int(input())
   if klepus==1: slim2=0+2
   elif klepus==2: slim2=0+0
   else: print("nav tadas atbildes")
   print("")
   print("7.Jums ir slikta dusa,kurs nepariet visu dienu")
   print("1.Ja")
   print("2. Ne")
   dusa=int(input())
   if dusa==1: slim2=0+2
   elif dusa==2: slim2=0+0
   else: print("nav tadas atbildes")
   print("")
   print("8.Jums ir vemšana / caureja?")
   print("1.Ja")
   print("2. Ne")
   vem=int(input())
   if vem==1: slim2=0+2
   elif vem==2: slim2=0+0
   else: print("nav tadas atbildes")
   print("")
   print("9. Vai jums biezi sap galva?")
   print("1.Ja")
   print("2. Ne")
   galva=int(input())
   if galva==1: slim2=0+2
   elif galva==2: slim2=0+0
   else: print("nav tadas atbildes")
   print("")
   print("Jusu dzimums ir...")
   print("1. sieviesu")
   print("2. viriesu")
   dzimums=int(input))
   if dzimums==1:
      print("")
      print("Vai jums sobrid ir menesreizes/ driz saksies?")
      print("1.Ja")
      print("2. Ne")
      men=int(input())
      if men==1: slim2=0-4
      elif men==2: slim2=0+0
      else: print("nav tadas atbildes")
   if slim2==0: print("Jums nav par ko uztraukties!")
   elif 0<slim2<=12: print("Palieciet gulta un noverojiet savu veselibu, ja nejutaties labak, apmeklejiet arstu.")
   elif 12<slim2<=24: print("Jums ir obligati jaapmekle artsts!")
   print("")
   print("Vai velies velreiz pildit so testu?")
   print("1.Ja")
   print("2.Ne")
   test1=int(input())
   if test1==2: print("Jauku dienu!")
