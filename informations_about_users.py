"""
11/02/2023
Programm that gives informations about users
Creator: Shahzod Bahronov
"""

def informations(ism,fam,t_yil,t_joy,email,nomer):
    information = {
        'ismi' : ism,
        'familyasi' : fam,
        'tyil' : t_yil,
        'tjoy' : t_joy,
        'email' : email,
        'raqami' : nomer,}
    return information

print("\nFoydalanuvchilar haqida ma'lumotlar: ")
malumotlar = []
while True:
    ism = input("Foydalanuvchi ismi: ")
    fam = input("Foydalanuvchi familyasi: ")
    t_joy = input("Tug`ilgan joyi: ")
    t_yil = int(input("Tug'ilgan yili: "))
    email = input("Pochta manzili: ")
    nomer = input("Telefon raqami: ")
    print("------------------------")
    
    malumotlar.append(informations(ism,fam,t_yil,t_joy,email,nomer))
    
    javob = input("Yana foydalanuvhi qo`shasizmi ? (ha/yo'q): ")
    if javob == 'ha':
        continue
    else:
        break
for malumot in malumotlar:
    for n in range(len(malumotlar)):
        print(f"{n+1}-foydalanuvchi haqida ma`lumotlar: ")
        print(f"{malumot['ismi'].title()} {malumot['familyasi'].title()} "
        f"{2023-malumot['tyil']} yoshda."
        f" {malumot['tjoy'].title()} viloyatida tug'ilgan."
        f"Pochta manzili: {malumot['email']}@gmail.com."
        f"Telefon raqami: {malumot['raqami']}")