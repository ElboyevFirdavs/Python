Homework 1:
1.
  df.rename(columns={'First Name': 'first_name'}|{'Age':'age'}, inplace=True)
  print(df)

2.
  print(df.head(3))

3.
  age_rank = df['age']
  age_rank.mean()

4.
  print(df[['first_name', 'City']])

5.
  df['Salary'] = np.random.randint(1000, 5001, size=len(df))
  print(df)

6.
  print(df.describe())

Homework 2:
1.
  sales_and_expenses = {'Month': ['Jan', 'Feb', 'Mar', 'Apr'], 'Sales': [5000,6000,7500,8000], 'Expenses':[3000,3500,4000,4500]} 
  sales_and_expenses = pd.DataFrame(sales_and_expenses)

2.
  max_sales = sales_and_expenses['Sales'].max()
  max_expenses = sales_and_expenses['Expenses']. max()
  
  print("Maximum Sales:", max_sales)
  print("Maximum Expenses:", max_expenses)


3.
  min_sales = sales_and_expenses['Sales'].min()
  min_expenses = sales_and_expenses['Expenses']. min()
  
  print("Minimum Sales:", min_sales)
  print("Minimum Expenses:", min_expenses

4.
        avg_sales = sales_and_expenses['Sales'].mean()
        avg_expenses = sales_and_expenses['Expenses'].mean()
        
        print("Average Sales:", avg_sales)
        print("Average Expenses:", avg_expenses)

   Homework 3:
1

  Expnses = {'Category':['Category','Utilities','Groceries','Entertainment'], 'January':[1200,200,300,150], 'February':[1300,220,320,160], 'March': [1400,240,330,170] , 'April': [1500,250,350,180] }
  expenses = pd.DataFrame(Expnses)
  print(exp)



2.
    expenses.set_index('Category', inplace=True)   // bu index maximum ga ham minimum va average ga ham tegishli buladi illakasiga bitta yozsa bo'ladi
    max_expense_per_category = expenses.max(axis=1)
    print("Maximum expense for each category:",max_expense_per_category)
    
3.

    min_expense_per_category = expenses.min(axis=1)
    print("Minimum expense for each category:",min_expense_per_category)

4.
    avg_expense_per_category = expenses.mean(axis=1)
    print("Average expense for each category:",avg_expense_per_category)
























