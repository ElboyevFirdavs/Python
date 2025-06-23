1.
      Original_List =  [12.23, 13.32, 100, 36.32]
      array = np.array(Original_List)
      print("orginal list:", Original_List)
      print("one-demisional numpy arry:", array)
2.
      lists = [[2,3,4], [5,6,7], [8,9,10]]
      matrix = np.array(lists)
      matrix  
                                            ## 3*3 ko'rinishda chiqadi

      lists = [[2,3,4], [5,6,7], [8,9,10]]
      lists 
                                            ## 1 ta colum bo'lib chiqadi


3.
      vector = np.zeros(10)
      update_value = vector.copy()
      update_value[6] = 11
      update_value
4.
      numbers = np.arange(12, 38)
      array_values = numbers.copy()
      numbers

5.
      original_array=np.array([1, 2, 3, 4])
      print("Orgina Array:", original_array)
      float_array = original_array.astype(float)
      print("Array converted to float:", float_array)
6.
        # Fahrenheit darajadagi qiymatlar
        fahrenheit = np.array([0, 12, 45.21, 34, 99.91, 32.])
        print("Values in Fahrenheit degrees:", fahrenheit)
        
        # Fahrenheit → Celsius
        celsius = (fahrenheit - 32) * 5 / 9
        print("Values in Centigrade degrees:", np.round(celsius, 2))  # 2 xonagacha yaxlitlandi
        
        # Celsius darajadagi qiymatlar
        celsius2 = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])
        print("Values in Centigrade degrees:", celsius2)
        
        # Celsius → Fahrenheit
        fahrenheit2 = celsius2 * 9 / 5 + 32
        print("Values in Fahrenheit degrees:", np.round(fahrenheit2, 2))
7.
        original_array = np.array([10, 20, 30])
        print("original array:", original_array)
        
        value_apped = [40,50,60,70,80,90]
        new_array = np.append(original_array, value_apped)
        print("After append values to the end of the array:",new_array)


8.
        array = np.random.rand(10)
        print("Random array:", array)
        
        mean_value = np.mean(array)
        print("Mean:", mean_value)
        
        median_value = np.median(array)
        print("Median:", median_value)
        
        std_deviation = np.std(array)
        print("Standar Deviation:", std_deviation)
        

9.
      arrayy = np.random.rand(10*10)
      print("Random array:", arrayy)
      
      min_value = np.min(arrayy)
      print("min value:", min_value)
      
      max_value = np.max(arrayy)
      print("max value:", max_value)
      
      


10.

      arrayys = np.random.rand(3*3*3)
      print("Random array:", arrayys)

