# Chatbot
def bmi():
    print (str.center('WILLKOMMEN BEI SIXPAXX', 26))

    print()
    while True:
        print (str.center("Zuerst lass uns kennenlernen, ich bin Bobby!", 30))
        print()
        name = input("Wie heißt du?")


        print()

        if len(name) > 5:
            print(name + ','"Das ist ein wunderschöner Name!" )
        else:
            print("Schön, dein Name ist leicht zu merken!") 

        print()

        print("Hello " + name + "! Schön dich kennenzulernen!")
        print()
        print('Jetzt möchte ich dir ein paar persönliche Fragen stellen. Aber keine Sorge,ich verrate es nicht anderen Kollegen.')
        print()
        age = float(input("wie alt bist du ?"))
        if age <= 30:
            print("Wow, du bist erst " + str(age) + " Jahre alt !Ich war auch mal so unglaublich jung wie du")
        else:
            print('du bist " + str(age) + " Jahre alt!')

        print()


        weight = float(input("Wieviel wiegst du? (in Kilos)"))
        print()
        if weight > 500:
            print("Bitte ein richtiges Gewicht.")
        elif weight < 0:
            print("Bitte ein richtiges Gewicht.")
        else:
            print("Ich bin froh, dass du diesen wichtigen ersten Schritt machst, um gesund zu werden " + name + "!")


        print()

        height_cm = float(input("OK, wie groß bist du? (in cm)"))
        if height_cm > 182:
            print ("Wow! du bist groß!")
        elif height_cm < 50:
            print ("ok")

        height_m = height_cm * 0.01
        BMI = round(float(weight / (height_m**2)),2)

        print()



        print('dein BMI ist: '+str(BMI))
        print()

      
        if BMI < 17.5:
            print ('Achtung: Ein BMI-Wert unter 17,5 ist bedenklich und gilt bei Männern wie Frauen als anorektisch. Um mit einem viel zu niedrigen Körpergewicht nicht die Gesundheit zu gefährden, sollten Sie bei einem solchen Ergebnis dringend einen Arzt aufsuchen.')
        if BMI < 17.5 and BMI > 22: 
            print  ('dein BMI ist sehr niedrig. Versuchen Sie, etwas zuzunehmen, um langfristig gesund und leistungsfähig zu bleiben. Die Techniker oder Ihr Arzt unterstützen Sie gern dabei.')
        if BMI > 22 and BMI < 28:
            print ( 'Super! dein Gewicht ist gesund. Mit einer ausgewogenen Ernährung und regelmäßiger Bewegung wird das auch langfristig so bleiben.')
        if BMI < 28 and BMI > 33:
            print ('dein BMI ist leicht erhöht. Achten Sie auf Ihre Ernährung und bewegen Sie sich regelmäßig. So können Sie das Risiko für mögliche Begleiterkrankungen minimieren.')
        else:
            print ('dein BMI weist auf Übergewicht hin. Das birgt die Gefahr von Krankheiten wie etwa Diabetes. Ihr Hausarzt und die Techniker unterstützen Sie gern bei einem gesunden Lebensstil.')
        
        print()
        print('danke für dein Besuch ' + name + ' bis zum nächsten Mal! ')
       
        
        break

 
