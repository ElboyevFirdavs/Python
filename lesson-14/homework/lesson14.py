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


product_sales = df4.groupby('Product')['Total_Price'].sum()


plt.figure(figsize=(6, 6))
product_sales.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgreen', 'lightcoral'])
plt.title('Sales Distribution by Product')
plt.ylabel('')
plt.tight_layout()
plt.show()
