Homework 2:
1.
  data1 = stackoverflow['creationdate']
  sortdata = data1 < '2014-01-01'
  stackoverflow[sortdata]

2.
  score = stackoverflow['score']
  scores = score > 50
  stackoverflow[scores]

3.
  score = stackoverflow['score']
  scores = score.between(50,100)
  stackoverflow[scores]

5.
    stackoverflow.iloc[ :, :5]

    stackoverflow.loc[:, 'id':'answercount']

6.


        # 1. creationdate ni datetime formatga o‘tkazamiz
        stackoverflow['creationdate'] = pd.to_datetime(stackoverflow['creationdate'])
        
        # 2. Faqat Unutbu yozgan javoblar
        unutbu_answers = stackoverflow[(stackoverflow['quest_name'] == 'Unutbu') & 
                                        (stackoverflow['ans_name'] == 'Unutbu')]
        
        # 3. U javob bergan savollar IDlarini olamiz
        question_ids = unutbu_answers['id'].unique()
        
        # 4. 2014-03-01 dan 2014-10-01 gacha, score < 5 bo‘lgan savollarni filter qilamiz
        filtered_questions = stackoverflow[
            (stackoverflow['quest_name'] == 'Unutbu') &
            (stackoverflow['id'].isin(question_ids)) &
            (stackoverflow['creationdate'] >= '2014-03-01') &
            (stackoverflow['creationdate'] <= '2014-10-01') &
            (stackoverflow['score'] < 5)
        ]
        
        # 5. Natijani chiqaramiz
        print(filtered_questions[['id',  'creationdate', 'score', 'quest_name', 'ans_name']])

7.
     
      
      # CSV faylni o‘qish (agar hali o‘qilmagan bo‘lsa)
      df = pd.read_csv('stackoverflow_qa.csv')
      
      # 1. score 5 dan katta va 10 dan kichik OR viewcount > 10000 bo‘lganlarni tanlaymiz
      filtered_df = df[
          ((df['score'] > 5) & (df['score'] < 10)) |
          (df['viewcount'] > 10000)
      ]
      
      # 2. Natijani ko‘rish (id, score, viewcount, title)
      print(filtered_df[['id', 'score', 'viewcount', 'title']])


8.
    
      
      # Faylni o‘qish (agar hali o‘qilmagan bo‘lsa)
      df = pd.read_csv('stackoverflow_qa.csv')
      
      # Scott Boston javob bermagan savollarni tanlash
      not_scott = df[df['ans_name'] != 'Scott Boston']
      
      # Faqat savollarni olish (ya'ni 'title' ustuni bo‘sh bo‘lmaganlar)
      only_questions = not_scott[not_scott['title'].notna()]
      
      # Natijani ko‘rish
      print(only_questions[['id', 'title', 'ans_name']])
      
            
      
Homework 3:

 1.
        filtered = titanic[
            (titanic['Sex']=='female')&
            (titanic['Pclass'] == 1) &
            (titanic['Age'] >=20) &
            (titanic['Age'] <=30)
        ]
        
        print(filtered)
        


2.
        filtered_money = titanic[
            (titanic['Fare'] >= 100 )
        ]
        filtered_money
        

3.
      filtered_alone = titanic[
          (titanic['Survived'] == 1)
      ]
      filtered_alone




4.

      filtered_class_c = titanic[
          (titanic['Embarked']== 'C') &
          (titanic['Fare'] > 50)
      ]
      
      filtered_class_c
      





5.
      family_abroad = titanic[
          (titanic['SibSp'] > 0) & 
          (titanic['Parch'] > 0)
      ]

6.
        filtered_class_c = titanic[
            (titanic['Embarked']== 'C') &
            (titanic['Fare'] > 50)
        ]
        
        filtered_class_c
        
        
   7.
      rich_cabin = titanic[
          (titanic['Cabin'].notna()) &
          (titanic['Fare'] >200)
      ]
      
      rich_cabin




8.
          odd_number_id = titanic[ 
              titanic['PassengerId']%2==1]
          
          odd_number_id
          
9.
        unique_tickets  =titanic[ 
            (titanic['Ticket'].duplicated(keep=False))
        ]
        unique_tickets


10.
miss_class1 = titanic[ 
    (titanic['Name'].str.contains('Miss')) &
    (titanic['Pclass'] == 1) &
    (titanic['Sex'] == 'female')
]
miss_class1



















