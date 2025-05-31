  1.
      name = input("ismingiz nima ")
      date = input("Tugilgan yilingizni kiriting")
      age = 2025-int(date)
      
      print("Salom,", name + "!", "Sizning yoshingiz:", age)

2.

      txt = 'LMaasleitbtui'
      print(txt[1:20:2])



3.
        txt = 'MsaatmiazD'
        txt_lower= txt.lower()
        print(txt[0:10:2])

4.
        txt = "I'am John. I am from London"
        qism = txt.split("from")[1]  
        print("Yashash joyi:", joy)
5.
        # Foydalanuvchidan matnni olamiz
        matn = input("Matn kiriting: ")
        
        # Matnni teskari qilib chiqaramiz
        teskari = matn[::-1]
        
        # Natijani chiqaramiz
        print("Teskari matn:", teskari)

6.
      text=input('matn kiriting')
      
      print(text.count('aeiouAEIOU'))
      

7.
      # Foydalanuvchidan raqamlarni vergul bilan ajratib olish shaklida so'raymiz
      raqamlar = input("Raqamlarni vergul bilan ajrating (masalan: 3,5,9,1): ")
      
      # Kiritilgan matnni ro'yxatga aylantiramiz va har bir elementni int ga o'tkazamiz
      raqamlar_list = [int(x) for x in raqamlar.split(",")]
      
      # Eng katta raqamni topamiz
      max_raqam = max(raqamlar_list)
      
      print("Eng katta raqam:", max_raqam)

8.
      soz = input("So'z kiriting: ")
      
      if soz == soz[::-1]:
          print("Bu so'z palindrom.")
      else:
          print("Bu so'z palindrom emas.")
      

9.
      # Foydalanuvchidan email manzilini olish
      email = input("Email manzilingizni kiriting: ")
      
      # '@' belgisidan keyingi qismni ajratib olish
      domen = email.split('@')[1]
      
      print("Domen:", domen)


10.
      import random
      import string
      
      # Parol uzunligini so'raymiz
      uzunlik = int(input("Parol uzunligini kiriting: "))
      
      # Harflar, raqamlar va maxsus belgilar
      harflar = string.ascii_letters    # a-zA-Z
      raqamlar = string.digits          # 0-9
      maxsus_belgilar = string.punctuation  # !@#$ va boshqa
      
      # Barcha belgilarni birlashtiramiz
      belgilar = harflar + raqamlar + maxsus_belgilar
      
      # Tasodifiy parol yaratamiz
      parol = ''.join(random.choice(belgilar) for _ in range(uzunlik))
      
      print("Tasodifiy parol:", parol)

      











