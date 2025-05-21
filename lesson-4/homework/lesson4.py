1. Sort a Dictionary by Value

        # Mevalar va ularning soni ko‘rsatilgan lug‘at
        my_dict = {'apple': 10, 'banana': 2, 'cherry': 7, 'date': 4}
        
        # Qiymatlar bo‘yicha oshish tartibida saralash
        asc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1]))
        print("Oshish tartibida:", asc_sorted)
        
        # Qiymatlar bo‘yicha kamayish tartibida saralash
        desc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
        print("Kamayish tartibida:", desc_sorted)

2. Add a Key to a Dictionary

          d1 = {0:10, 1:20, 2:30}

3. Concatenate Multiple Dictionaries

        dic4 = {**dic1,**dic2,**dic3}

4. Generate a Dictionary with Squares

        n = 5
        squares_dict = {x: x*x for x in range(1, n+1)}
        print(squares_dict)

5.Dictionary of Squares (1 to 15)
  
        n = 15
        squares_dict = {x: x*x for x in range(1, n+1)}
        print(squares_dict)


Set Exercises
1. Create a Set

      my_set = {1, 2, 3, 4, 5}
2.
      
      my_set = {'apple', 'banana', 'cherry'}
      
    
      for item in my_set:
          print(item)


3.
      set1 = {1,2,3,4,5}
      set1.add(7)
      print(set1

4.
        set1 = {1,2,3,4,5}
        set1.remove(3)
        print(set1)

5.

        set1 = {1,2,3,4,5}
        set1.discard(6)
        print(set1)
