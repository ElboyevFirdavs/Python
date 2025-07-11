1.

import pandas as pd

# Ma'lumotlarni o'qish
df = pd.read_csv("sales_data.csv")  # Faylingiz nomi shu bo‘lishi kerak

# --- Task 1: Kategoriya bo‘yicha umumiy tahlil ---
category_stats = df.groupby('Category').agg(
    Total_Quantity=('Quantity', 'sum'),
    Avg_Price=('Price', 'mean'),
    Max_Single_Quantity=('Quantity', 'max')
).reset_index()

print("📊 Task 1: Category-wise Summary")
print(category_stats)

# --- Task 2: Har bir kategoriya bo‘yicha eng ko‘p sotilgan mahsulot ---
top_products = df.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()
top_products = top_products.sort_values(['Category', 'Quantity'], ascending=[True, False])
top_per_category = top_products.groupby('Category').first().reset_index()

print("\n🏆 Task 2: Top-Selling Product by Category")
print(top_per_category)

# --- Task 3: Eng yuqori savdo bo‘lgan sana (Quantity * Price) ---
df['Total'] = df['Quantity'] * df['Price']
total_sales_by_date = df.groupby('Date')['Total'].sum().reset_index()
max_sales_day = total_sales_by_date.loc[total_sales_by_date['Total'].idxmax()]

print("\n📅 Task 3: Date with Highest Total Sales")
print(max_sales_day)


2.

import pandas as pd

# 1. Ma'lumotni yuklash
df = pd.read_csv("customer_orders.csv")

# --- Task 1: 20 tadan kam buyurtma qilgan mijozlarni filtrlash ---
order_counts = df.groupby('CustomerID')['OrderID'].count().reset_index()
order_counts = order_counts[order_counts['OrderID'] >= 20]

# 20 tadan ortiq buyurtma qilgan mijozlar
valid_customers = order_counts['CustomerID']
filtered_orders = df[df['CustomerID'].isin(valid_customers)]

print("✅ Customers with 20 or more orders:")
print(filtered_orders)

# --- Task 2: O‘rtacha narxi $120 dan yuqori bo‘lgan mahsulotlarni buyurtma qilgan mijozlar ---
avg_price = df.groupby('CustomerID')['Price'].mean().reset_index()
high_price_customers = avg_price[avg_price['Price'] > 120]

print("\n✅ Customers with average product price > $120:")
print(high_price_customers)

# --- Task 3: Har bir mahsulot uchun jami son va narx, va quantity >= 5 ---
df['TotalPrice'] = df['Quantity'] * df['Price']

product_summary = df.groupby('Product').agg(
    Total_Quantity=('Quantity', 'sum'),
    Total_Price=('TotalPrice', 'sum')
).reset_index()

filtered_products = product_summary[product_summary['Total_Quantity'] >= 5]

print("\n✅ Products with total quantity >= 5:")
print(filtered_products)


3.
import pandas as pd
import sqlite3

# 1. SQL orqali ma'lumotlarni o‘qish
conn = sqlite3.connect("population.db")
df_pop = pd.read_sql_query("SELECT * FROM population", conn)
conn.close()

# 2. Salary band faylini o‘qish
salary_band = pd.read_excel("population salary analysis.xlsx")

# Salary band oralig‘i toifasini yaratish uchun `pd.cut` funksiyasiga tayyorlanamiz
bins = salary_band['Lower Bound'].tolist() + [float('inf')]
labels = salary_band['Band'].tolist()

# 3. Ma'lumotlarga salary bandni qo‘shamiz
df_pop['Salary Band'] = pd.cut(df_pop['Salary'], bins=bins, labels=labels, right=False)

# 4. Har bir salary band bo‘yicha umumiy statistikalar
overall_summary = df_pop.groupby('Salary Band').agg(
    Population=('Salary', 'count'),
    Average_Salary=('Salary', 'mean'),
    Median_Salary=('Salary', 'median')
).reset_index()

# Aholining foizini hisoblaymiz
total_population = len(df_pop)
overall_summary['Population %'] = round((overall_summary['Population'] / total_population) * 100, 2)

print("✅ Overall Salary Band Statistics:")
print(overall_summary)

# 5. Har bir State va Salary Band bo‘yicha tahlil
state_summary = df_pop.groupby(['State', 'Salary Band']).agg(
    Population=('Salary', 'count'),
    Average_Salary=('Salary', 'mean'),
    Median_Salary=('Salary', 'median')
).reset_index()

# Har bir State bo‘yicha umumiy aholini hisoblab, foizni hisoblash
state_totals = df_pop.groupby('State')['Salary'].count().to_dict()
state_summary['Population %'] = state_summary.apply(
    lambda row: round((row['Population'] / state_totals[row['State']]) * 100, 2), axis=1
)

print("\n✅ State-wise Salary Band Statistics:")
print(state_summary)
