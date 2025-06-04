1.
def is_leap(year):
    # """
    # Berilgan yil kabisa yili (kabisa — 366 kunlik yil) ekanligini aniqlaydi.

    # Yil quyidagi shartlarga ko‘ra kabisa yili bo‘ladi:
    # - Agar yil 4 ga bo‘linadigan bo‘lsa, VA
    # - 100 ga bo‘linmaydigan bo‘lsa, YOKI
    # - 400 ga ham bo‘linadigan bo‘lsa.

    # Parametrlar:
    # year (int): Tekshiriladigan yil.

    # Natija:
    # bool: Agar kabisa yili bo‘lsa True, bo‘lmasa False qaytaradi.
    # """
    if not isinstance(year, int):
        raise ValueError("Yil butun son bo‘lishi kerak.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
  
    print(is_leap(2024))   # True — kabisa yili
    print(is_leap(2100))   # False — 100 ga bo‘linadi, lekin 400 ga emas
    print(is_leap(2000))   # True — 400 ga bo‘linadi
    print(is_leap(2023))   # False — oddiy yil
2.

        n = int(input('entern N number'))
        
        if n%2 ==1: 
            print('Weird')
        elif n % 2 == 0 and 2 <= n <= 5:
            print('not Weird')
        elif n % 2 == 0 and 6 <= n <= 20:
            print('Weird ')
        elif n % 2 == 0 and n > 20:
            print('Not Weird')
