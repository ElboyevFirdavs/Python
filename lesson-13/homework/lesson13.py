1.
    from datetime import datetime                #har doim datetime qilinganda yoziladi 
    year = int(input("Tug'ulgan yilingizni kiriting"))
    month = int(input("Tug'ulgan oyingizni kiriting"))
    day = int(input("Tug'ulgan kuningizni kiriting"))
    
    age = datetime(day=day, month=month, year=year)
    print(age.day, age.month, age.year)
2.
      from datetime import datetime
      
      month = int(input("Tug'ulgan oyingizni kiriting"))
      day = int(input("Tug'ulgan kuningizni kiriting"))
      
      today = datetime.today()
      this_year = today.year
      
      next_birthday = datetime(this_year, month, day)
      
      if next_birthday < today:
          next_birthday = datetime(this_year+1, month, day)
      
      days_remaining = (next_birthday - today).days
      print(f"Sizning keyingi tug'ulgan kuningizga {days_remaining} kun qoldi")

3.
    from datetime import datetime, timedelta
    year = int(input("hozirgi yilni kiriting"))
    month = int(input("hozirgi oyni kiriting"))
    day = int(input("hozirgi kunni  kiriting"))
    hour = int(input("hozirgi soatni kiriting"))
    minuts = int(input("hozirgi minuti kiriting"))
    
    duration_hours = int(input("uchrashuv davomiyligini kiriting"))
    dusraton_minuts = int(input("uchrashuv davomiyligi daqiqasi"))
    
    start_time = datetime(year=year, month=month, day=day, hour=hour, minuts=minuts,)
    
    meeting_duration = timedelta(hours=duration_hours, minutes=dusraton_minuts)
    end_time = start_time + meeting_duration
    
    print("uchrashuv tugash vaqti", end_time)

4.
    from datetime import datetime
    import pytz
    
    # Foydalanuvchidan sana-vaqt kiritiladi
    date_str = input("Sana va vaqtni kiriting (YYYY-MM-DD HH:MM): ")
    user_timezone = input("Hozirgi vaqt zonangizni kiriting (masalan, Asia/Tashkent): ")
    target_timezone = input("Qaysi vaqt zonaga o‘girishni xohlaysiz? (masalan, Europe/London): ")
    
    # Sana va vaqtni datetime formatiga o‘tkazamiz
    local_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    
    # Vaqt zonalarini yuklaymiz
    user_tz = pytz.timezone(user_timezone)
    target_tz = pytz.timezone(target_timezone)
    
    # Kiritilgan vaqtdan user vaqt zonasini belgilaymiz
    localized_time = user_tz.localize(local_time)
    
    # Endi uni boshqa vaqt zonasiga o‘tkazamiz
    converted_time = localized_time.astimezone(target_tz)
    
    # Natijani chiqaramiz
    print("Konvertatsiya qilingan vaqt:", converted_time.strftime("%Y-%m-%d %H:%M"))
    
    
5.
from datetime import datetime
import time

# Foydalanuvchidan kelajak vaqti olinadi
target_str = input("Kelajakdagi vaqtni kiriting (YYYY-MM-DD HH:MM:SS): ")
target_time = datetime.strptime(target_str, "%Y-%m-%d %H:%M:%S")

# Countdown boshlanadi
while True:
    now = datetime.now()
    remaining = target_time - now

    if remaining.total_seconds() <= 0:
        print(" Vaqt tugadi!")
        break

    # Qolgan vaqtni formatlab chiqaramiz
    days = remaining.days
    hours, rem = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(rem, 60)

    print(f"\rQolgan vaqt: {days} kun, {hours:02}:{minutes:02}:{seconds:02}", end="")
    time.sleep(1)

7.
number = input("Telefon raqamni kiriting (10 ta raqam, masalan: 1234567890): ")

if len(number) == 10 and number.isdigit():
    formatted = f"({number[:3]}) {number[3:6]}-{number[6:]}"
    print("Formatlangan raqam:", formatted)
else:
    print(" Noto‘g‘ri format. Faqat 10 ta raqamdan iborat bo‘lishi kerak.")
9.
text = """Bu yerda siz har xil so‘zlarni izlab topishingiz mumkin.
So‘zlar ko‘p va ular turli shakllarda bo‘lishi mumkin."""

word = input("Qidirilayotgan so‘zni kiriting: ")

matches = [i for i in text.lower().split() if word.lower() in i]

if matches:
    print(f"✅ '{word}' so‘zi {len(matches)} marta uchradi:")
    for m in matches:
        print("-", m)
else:
    print(f" '{word}' topilmadi.")









