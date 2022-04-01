

"""
    >>> bmi()
    Bot-->Ich antworte gerne, ich brauche nur ein paar Fragen.
    Bot-->Bitte geben Sie hier Ihr Gewicht ein (in Kilos): 

    800
    Bot-->BITTE GEBEN SIE GÜLTIGEN BETRAG EIN!
    80
    Bot-->Bitte geben Sie hier Ihr Gewicht ein (in Kilos): 
    80
    Bot-->sehr gut!Jetzt die nächste Frage.
    Bot--> Bitte geben Sie hier Ihre Körpergröße ein (in Meter): 
    9
    Bot-->BITTE GEBEN SIE EINEN GÜLTIGEN BETRAG EIN!
    Bot--> Bitte geben Sie hier Ihre Körpergröße ein (in Meter): 
    1.8
    Bot--> Danke! Ihr BMI ist: 24.69
    'Super! Ihr Gewicht ist gesund. Mit einer ausgewogenen Ernährung und regelmäßiger Bewegung wird das auch langfristig so bleiben.'
    >>>
    """
def bmi(): 
   
    a = 'Achtung: Ein BMI-Wert unter 17,5 ist bedenklich und gilt bei Männern wie Frauen als anorektisch. Um mit einem viel zu niedrigen Körpergewicht nicht die Gesundheit zu gefährden, sollten Sie bei einem solchen Ergebnis dringend einen Arzt aufsuchen.'
    b = 'Ihr BMI ist sehr niedrig. Versuchen Sie, etwas zuzunehmen, um langfristig gesund und leistungsfähig zu bleiben. Die Techniker oder Ihr Arzt unterstützen Sie gern dabei.'
    c = 'Super! Ihr Gewicht ist gesund. Mit einer ausgewogenen Ernährung und regelmäßiger Bewegung wird das auch langfristig so bleiben.'
    d = 'Ihr BMI ist leicht erhöht. Achten Sie auf Ihre Ernährung und bewegen Sie sich regelmäßig. So können Sie das Risiko für mögliche Begleiterkrankungen minimieren.'
    e = 'Ihr BMI weist auf Übergewicht hin. Das birgt die Gefahr von Krankheiten wie etwa Diabetes. Ihr Hausarzt und die Techniker unterstützen Sie gern bei einem gesunden Lebensstil.'
    print('Bot-->Ich antworte gerne, ich brauche nur ein paar Fragen.')
    num = 0
    num_1 = 0
   
    while True:
        weight = ''
        try:
            w=float(input('Bot-->Bitte geben Sie hier Ihr Gewicht ein (in Kilos): \n'))
            if 500 > w > 5:
                weight=w
                print('Bot-->sehr gut!Jetzt die nächste Frage.')
                break
            else: 
                print('Bot-->BITTE GEBEN SIE GÜLTIGEN BETRAG EIN!')
                num+=1
                if num==3:
                    print('Sie haben Drei mal keinen gültigen Betrag eingegeben! Möchten Sie noch weitermachen?')
                    w_= input('You-->')
                    mylist=['ja','okay','ok','klar','natürlich']
                    for i in w_:
                        i=re.split(r'\s',w_.lower())
                        for word in i:
                            if word in mylist:
                                continue 
                            else:
                                print('Bot-->Alles klar. Haben Sie sonst noch Fragen?')
                                return bot_response()
                      
        except ValueError: 
            wi=input('Bot-->Sie haben keinen gültigen Betrag eingegeben. Möchten Sie noch weitermachen?\n')
            mylist=['ja','ok','klar','natürlich']
            for i in wi:
                i=re.split(r'\s',wi.lower())
                for word in i:
                    if word in mylist:
                        continue  
                    else:
                        print('Bot-->Alles klar. Haben Sie sonst noch Fragen?')
                        return bot_response()
    while True:  
        height = ''
        try:
            h=float(input('Bot--> Bitte geben Sie hier Ihre Körpergröße ein (in Meter): \n'))           
            if 3>h>0.5:
                height=h
                break          
            else:
                print('Bot-->BITTE GEBEN SIE EINEN GÜLTIGEN BETRAG EIN!')
                num_1+=1
                if num_1==3:
                    print('Bot-->Sie haben dreimal keinen gültigen Betrag eingegeben. Möchten Sie noch weitermachen?')
                    h_=input('You-->')
                    mylist_1=['ja','ok','klar','natürlich']
                  
                    for g in h_:
                        g=re.split(r'\s',h_.lower())
                        for word in g:
                            if word in mylist_1:
                                continue  
                            else:
                                print('Bot-->Alles klar. Haben Sie sonst noch Fragen?')
                                return bot_response()
                
        except ValueError: 
            hi=input('Bot-->Sie haben keinen gültigen Betrag eingegeben. Möchten Sie noch weitermachen?\n')
            mylist_1=['ja','ok','klar','natürlich']
            for i in hi:
                i=re.split(r'\s',hi.lower())
                for word in i:
                    if word in mylist_1:
                        continue  
                    else:
                        print('Bot-->Alles klar. Haben Sie sonst noch Fragen?')
                        return bot_response()
         
 
    bmi =  round(float(weight / (height**2)),2)
    print('Bot--> Danke! Ihr BMI ist: '+str(bmi))
    if bmi< 17.5:
        return a
    elif  17.5 < bmi < 22:
        return  b
    elif  22 < bmi < 28:
        return c
    elif 28 < bmi < 33:
        return d
    else:
        return e

if __name__ == '__main__':
    import doctest
    doctest.testmod()

  
   