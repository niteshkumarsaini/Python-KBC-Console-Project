import time
from playsound import playsound
print("WELCOME TO KBC CONSOLE APP !!")
playsound('sounds/intro.mp3')
num=0
time.sleep(1)
win=0
question = ['Q-1 Which one of the following river flows between Vindhyan and Satpura ranges?', 'Q-2 The Central Rice Research Station is situated in?',
        'Q-3 Who among the following wrote Sanskrit grammar?', 'Q-4 Which among the following headstreams meets the Ganges in last?', 'Q-5 The metal whose salts are sensitive to light is?', 'Q-6  Patanjali is well known for the compilation of –', 'Q-7 River Luni originates near Pushkar and drains into which one of the following?', 'Q-8 Which one of the following rivers originates in Brahmagiri range of Western Ghats?', 'Q-9 The country that has the highest in Barley Production?', 'Q-10 Tsunamis are not caused by', 'Q-11 Chambal river is a part of –', 'Q-12 D.D.T. was invented by?', 'Q-13 Volcanic eruption do not occur in the', 'Q-14 Indus river originates in –','Q-15 The hottest planet in the solar system?','Q-16 With which of the following rivers does Chambal river merge?']
options=[['(a) Narmada','(b) Mahanadi','(c) Son','(d) Netravati'],['(a) Chennai','(b) Cuttack','(c) Bangalore','(d) Quilon'],['(a) Kalidasa','(b) Charak','(c) Panini','(d) Aryabhatt'],['(a) Alaknanda','(b) Pindar','(c) Mandakini','(d) Bhagirathi'],['(a) Zinc','(b) Silver','(c) Copper','(d) Aluminum'],['(a) Yoga Sutra','(b) Panchatantra','(c) Brahma Sutra','(d) Ayurveda'],['(a) Rann of Kachchh','(b) Arabian Sea','(c) Gulf of Cambay','(d) Lake Sambhar'],['(a) Pennar','(b) Cauvery','(c) Krishna','(d) Tapti'],['(a) China','(b) India','(c) Russia','(d) France'],['(a) Hurricanes','(b) Earthquakes','(c) Undersea landslides','(d) Volcanic eruptions'],['(a) Sabarmati basin','(b) Ganga basin','(c) Narmada basin','(d) Godavari basin'],['(a) Mosley','(b) Rudolf','(c) Karl Benz','(d) Dalton'],['(a) Baltic sea','(b) Black sea','(c) Caribbean sea','(d) Caspian sea'],['(a) Kinnaur','(b) Ladakh','(c) Nepal','(d) Tibet'],['(a) Mercury','(b) Venus','(c) Mars','(d) Jupiter'],['(a) Banas','(b) Ganga','(c) Narmada','(d) Yamuna']]
answers=('(a) Narmada','(b) Cuttack','(c) Panini','(d) Bhagirathi','(b) Silver','(a) Yoga Sutra','(a) Rann of Kachchh','(b) Cauvery','(c) Russia','(a) Hurricanes','(c) Narmada basin','(a) Mosley','(a) Baltic sea','(d) Tibet','(b) Venus','(d) Yamuna')

amount=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000,70000000]
for i in range (0,14):
    print("Wait your Question is Loading...")
    playsound('sounds/que.mp3')
    print(question[i])
    for j in range(0,4):
       print(options[i][j])
    while True:
       a=input("Enter Option : ")
       if(a=="A" or a=='a'):
            num=0
            break
       elif(a=='B' or a=='b'):
            num=1
            break
       elif(a=='C' or a=='c'):
            num=2
            break
       elif(a=='D' or a=='d'):
            num==3
            break
    if options[i][num]==answers[i]:
         win=win+amount[i]
         print("Correct Answer you won",win,'RS')
         playsound('sounds/correct.mp3')
    else:
        
        print("Sorry you Lost !")
        playsound('sounds/wrong.mp3')
        break

print("Your Final Winning Amount is",win,"Rs")
print("Thanks ..")




