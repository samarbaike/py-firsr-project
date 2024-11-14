import os

#Name and Last name
print('What is your first name?')
first_name=str(input())
print('What about your last name?')
last_name=str(input())

#School education certifcate
print('Do you have your school education certificate? ')
print('1 - Yes, I have my school education certificate.')
print("0 - No, I don't have my school education certificate.")
presence=int(input())

#ORT score
print('How much score did you get in ORT?')
ort=int(input())

#English level
print('What is you English proficiencly level')
print('A1')
print('A2')
print('B1')
print('B2')
print('C1')
print('C2')
englis=str(input())

os.system('cls' if os.name == 'nt' else 'clear')    

#results.part1a

if presence==1:
    if ort>=110:
        if englis=='A1' or englis=='A2':
            print('Since you do not have enough english proficiency level you are unabel to study at university.')
            print('We offer you to take foundation year in AIU, wherer you will be able to inhance you english proficiency level.')
            print('After Foundation year you will be able to enroll to university.')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Please, choose you specialty: ')
            print('Computer Engineering 2500$')
            print('Artificial Intelligence 2200$')
            print('Psychology 1900$')
            print('Journalism 1700$')
            print('International Relations 2200$')
            print('Law 1800$')
            print('Management 2200$')
            print('Medicine 3300$')
            specialty=str(input())
            if specialty=='Medicine':
                cost=3300
            elif specialty=='Management':
    cost=2200
elif specialty=='Law':
    cost=1800
elif specialty=='International Relations':
    cost=2200
elif specialty=='Journalism':
    cost=1700
elif specialty=='Psychology':
    cost=1900
elif specialty=='Artificial Intelligence':
    cost=2200
elif specialty=='Computer Engineering':
    cost=2500

os.system('cls' if os.name == 'nt' else 'clear')


#A final message
if 245>=ort>=219:
    print('Dear ', first_name,' ', last_name, ' we congratulate you! You have been admitted to the ', specialty,  ' program at Ala-Too International University. The cost of your tuition with a 100% discount will be ', cost*0 ,'$ per year.',sep='')
elif 218>=ort>=210:
    print('Dear ', first_name,' ', last_name, ' we congratulate you! You have been admitted to the ', specialty,  ' program at Ala-Too International University. The cost of your tuition with a 75% discount will be ', cost*0.75 ,'$ per year.',sep='')
elif 209>=ort>=200:
    print('Dear ', first_name,' ', last_name, ' we congratulate you! You have been admitted to the ', specialty,  ' program at Ala-Too International University. The cost of your tuition with a 50% discount will be ', cost*0.5 ,'$ per year.',sep='')
elif 199>=ort>=175:
    print('Dear ', first_name,' ', last_name, ' we congratulate you! You have been admitted to the ', specialty,  ' program at Ala-Too International University. The cost of your tuition with a 25% discount will be ', cost*0.25 ,'$ per year.',sep='')
elif 174>=ort>=156:
    print('Dear ', first_name,' ', last_name, ' we congratulate you! You have been admitted to the ', specialty,  ' program at Ala-Too International University. The cost of your tuition with a 10% discount will be ', cost*0.1 ,'$ per year.',sep='')
elif 155>=ort>=140:
    print('Dear ', first_name,' ', last_name, ' we congratulate you! You have been admitted to the ', specialty,  ' program at Ala-Too International University. The cost of your tuition with a 5% discount will be ', cost*0.05 ,'$ per year.',sep='')
else:
    print('Dear ', first_name,' ', last_name, ' we congratulate you! You have been admitted to the ', specialty,  ' program at Ala-Too International University. The cost of your tuition will be ', cost*1 ,'$ per year.',sep='')
    else:
        print('You do not have enough ORT score due to it we can not accept you to university.')
elif presence==0:
    print('You do not have School Education Sertifiate due to it we are unable to accept you to university.')



#Addmision
print('Please, choose you specialty: ')
print('Computer Engineering 2500$')
print('Artificial Intelligence 2200$')
print('Psychology 1900$')
print('Journalism 1700$')
print('International Relations 2200$')
print('Law 1800$')
print('Management 2200$')
print('Medicine 3300$')
specialty=str(input())
if specialty=='Medicine':
    cost=3300
elif specialty=='Management':
    cost=2200
elif specialty=='Law':
    cost=1800
elif specialty=='International Relations':
    cost=2200
elif specialty=='Journalism':
    cost=1700
elif specialty=='Psychology':
    cost=1900
elif specialty=='Artificial Intelligence':
    cost=2200
elif specialty=='Computer Engineering':
    cost=2500

os.system('cls' if os.name == 'nt' else 'clear')


#A final message
if 245>=ort>=219:
    print('Dear ', first_name,' ', last_name, ' we congratulate you! You have been admitted to the ', specialty,  ' program at Ala-Too International University. The cost of your tuition with a 100% discount will be ', cost*0 ,'$ per year.',sep='')
elif 218>=ort>=210:
    print('Dear ', first_name,' ', last_name, ' we congratulate you! You have been admitted to the ', specialty,  ' program at Ala-Too International University. The cost of your tuition with a 75% discount will be ', cost*0.75 ,'$ per year.',sep='')
elif 209>=ort>=200:
    print('Dear ', first_name,' ', last_name, ' we congratulate you! You have been admitted to the ', specialty,  ' program at Ala-Too International University. The cost of your tuition with a 50% discount will be ', cost*0.5 ,'$ per year.',sep='')
elif 199>=ort>=175:
    print('Dear ', first_name,' ', last_name, ' we congratulate you! You have been admitted to the ', specialty,  ' program at Ala-Too International University. The cost of your tuition with a 25% discount will be ', cost*0.25 ,'$ per year.',sep='')
elif 174>=ort>=156:
    print('Dear ', first_name,' ', last_name, ' we congratulate you! You have been admitted to the ', specialty,  ' program at Ala-Too International University. The cost of your tuition with a 10% discount will be ', cost*0.1 ,'$ per year.',sep='')
elif 155>=ort>=140:
    print('Dear ', first_name,' ', last_name, ' we congratulate you! You have been admitted to the ', specialty,  ' program at Ala-Too International University. The cost of your tuition with a 5% discount will be ', cost*0.05 ,'$ per year.',sep='')
else:
    print('Dear ', first_name,' ', last_name, ' we congratulate you! You have been admitted to the ', specialty,  ' program at Ala-Too International University. The cost of your tuition will be ', cost*1 ,'$ per year.',sep='')