DataFrame 1: Student Grades
1.
df1['Average'] = df1[['Math', 'English', 'Science']].mean(axis=1)
print(df1[['Student_ID', 'Average']])

2.
top_student = df1.loc[df1['Average'].idxmax()]
print("Top Student:")
print(top_student)

3.
df1['Total'] = df1[['Math', 'English', 'Science']].sum(axis=1)
print(df1[['Student_ID', 'Total']])

4.
import matplotlib.pyplot as plt

# Har bir fan bo‘yicha o‘rta baho
subject_averages = df1[['Math', 'English', 'Science']].mean()

# Chizma
subject_averages.plot(kind='bar', color=['skyblue', 'lightgreen', 'lightcoral'])
plt.title("Average Grades per Subject")
plt.ylabel("Average Grade")
plt.xlabel("Subject")
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


  DataFrame 2: Sales Data
1.
total_sales = df2[['Product_A', 'Product_B', 'Product_C']].sum()
print("Total Sales per Product:")
print(total_sales)

2.
df2['Total_Sales'] = df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)
max_sales_date = df2.loc[df2['Total_Sales'].idxmax(), 'Date']
print("Date with Highest Total Sales:", max_sales_date)

3.
pct_change = df2[['Product_A', 'Product_B', 'Product_C']].pct_change() * 100
pct_change = pct_change.round(2)
print("Percentage Change in Sales:")
print(pct_change)

4.
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(df2['Date'], df2['Product_A'], label='Product A', marker='o')
plt.plot(df2['Date'], df2['Product_B'], label='Product B', marker='s')
plt.plot(df2['Date'], df2['Product_C'], label='Product C', marker='^')

plt.title('Sales Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

DataFrame 3: Employee Information
1.
avg_salary_by_dept = df3.groupby('Department')['Salary'].mean().round(2)
print("Average Salary by Department:")
print(avg_salary_by_dept)

2.
most_experienced = df3.loc[df3['Experience (Years)'].idxmax()]
print("Most Experienced Employee:")
print(most_experienced)

3.
min_salary = df3['Salary'].min()
df3['Salary Increase (%)'] = ((df3['Salary'] - min_salary) / min_salary * 100).round(2)
print(df3[['Name', 'Salary', 'Salary Increase (%)']])

4.
import matplotlib.pyplot as plt

# Hisoblash
department_counts = df3['Department'].value_counts()

# Chizma
department_counts.plot(kind='bar', color='skyblue')
plt.title('Employee Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

DataFrame 4: Customer Orders
1.
total_revenue = df4['Total_Price'].sum()
print("Total Revenue:", total_revenue)

2.
most_ordered = df4.groupby('Product')['Quantity'].sum().idxmax()
print("Most Ordered Product:", most_ordered)

3.
average_quantity = df4['Quantity'].mean()
print("Average Quantity Ordered:", round(average_quantity, 2))

4.
import matplotlib.pyplot as plt

# Mahsulotlar bo‘yicha umumiy savdo qiymati
product_sales = df4.groupby('Product')['Total_Price'].sum()

# Pie chart
plt.figure(figsize=(6, 6))
product_sales.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgreen', 'lightcoral'])
plt.title('Sales Distribution by Product')
plt.ylabel('')
plt.tight_layout()
plt.show()





































