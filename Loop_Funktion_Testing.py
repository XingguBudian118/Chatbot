
"""
    >>> loop()
    Bot--> Hallo, willkommen bei sixpaxx Fitnessstudio, ich bin Ihr BMI Berater.
    You-->hallo
    Bot-->Haben Sie Fragen?
    You-->wie heißt du?
    Bot-->Ich bin ein Chatbot. Haben Sie noch Fragen?
    You-->was kannst du
    Bot--> Sorry, ich bin noch dabei zu lernen, Sie können mich gerne zum BMI fragen.
    Oder rufen Sie bitte diese Nummer an:030-1234567.
    You-->ich habe ein Frage
    Bot--> Sorry, ich bin noch dabei zu lernen, Sie können mich gerne zum BMI fragen.
    Oder rufen Sie bitte diese Nummer an:030-1234567.
    You-->was kannst du?
    Bot-->Sie können mich gerne zum BMI fragen
    >>>
    """
import re
import random
intentions = { 'intents':[
    { 
      'tag': 'greetings',
      'pattern':['hallo', 'hi', 'ja','hey', 'Guten Tag', 'guten morgen', 'guten abend'],
      'responses':['Hallo.', 'Wie kann ich helfen?', 'Haben Sie Fragen?', 'Sie können mich gerne etwas fragen.']
    },

    {
        'tag':'farewell',
        'pattern':['tschüss','nichts','nein danke','nein', 'ciao','nee','auf wiedersehen', 'auf wiederhören', 'bis dann', 'bye','bye bye', 'schönen tag noch', 'schönen abend noch'],
        'responses':['Danke für Ihre Besuch. Auf Wiedersehen!']
    },
    {
        'tag':'grateful',
        'pattern':['super danke','danke','super','super,danke','gut,danke','gut','ok','alles gut'],
        'responses':['Gerne, was kann ich noch helfen?','Gerne, haben Sie noch Fragen?']
    },
    {
        'tag':'quastion',
        'pattern':['wie heißt du?','wie alt bist du?','was ist dein Geschlecht?','hast du freunde?','wer bist du?'],
        'responses':['Ich bin ein Chatbot. Haben Sie noch Fragen?','Ich bin ein Chatbot, haben Sie noch Fragen?']  
    },
    {
       'tag':'quastion_2' ,
       'pattern':['darf ich was fragen?','ich habe eine Frage','bin ich fette?','was kannst du?','wie schlau bist du?'],
       'responses':['Sie können mich gerne zum BMI fragen']
    },
    {
        'tag':'noanswer',
        'pattern':[''],
        'responses':['Sorry, ich habe nicht verstanden.','Bitte geben Sie mir mehr Info.','Bitte sagen Sie mir ein bisschen mehr.']    
    },
  
    {
       'tag':'time',
       'pattern':['wann haben Sie geöffnet?', 'öffnungszeiten', 'wann haben sie geöffnet'],
       'responses':['Unsere Online-Akademie ist 24/7 geöffnet!', '24/7']
    }]
}
inten_list = intentions.setdefault('intents')
def bot_response():
    uz = input("You-->").lower()
    
    for i in range(len(inten_list)):
        antw = False
        x = inten_list[i].get('pattern')
        if uz in x:
            antw = True
            return str("Bot-->" + random.choice(inten_list[i].get('responses')))  
    
    if antw == False:
        mylist=['bmi?','bmi']
        for i in uz:
            i=re.split(r'\s',uz.lower())
            for word in i:
                if word in mylist:
                    return bmi()
    return "Bot--> Sorry, ich bin noch dabei zu lernen, Sie können mich gerne zum BMI fragen.\nOder rufen Sie bitte diese Nummer an:030-1234567."
    
def loop():
    print('Bot--> Hallo, willkommen bei sixpaxx Fitnessstudio, ich bin Ihr BMI Berater.')
    while True:
        u = bot_response()
        print(u)
        if u == "Bot-->" + random.choice(inten_list[1].get('responses')): 
            break    

if __name__ == '__main__':
    import doctest
    doctest.testmod()