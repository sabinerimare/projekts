print("Ko jus gribat uzzinat?")
print("")
print("1. Manu risku saslimt ar slimibam, ko izraisa virusi un bakterijas;") 
print("2.Vai man ir jaapmekle arst")
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
if sakums==2: print("hehe")
    