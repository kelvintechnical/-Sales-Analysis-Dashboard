from dash import Dash, dcc, html
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('ESD.csv', encoding='latin1')

print(data.head())
print(data.info())
print(data.describe())
data.info()
data.describe()
data.isnull().sum()


# categories = data['Department']

# sales = data['Annual Salary']

# plt.bar(categories, sales, color='green', label='Total Sales')
# plt.legend()

# plt.title("Sales by Department")
# plt.xlabel("Departments")

# plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.ylabel("Annual Salary")

data['Annual Salary'] = data['Annual Salary'].replace('[\\$,]', '', regex=True).astype(float)

# Aggregate data by department
aggregated_data = data.groupby('Department')['Annual Salary'].sum()
categories = aggregated_data.index
sales = aggregated_data.values

plt.clf()
plt.close()

aggregated_data = data.groupby('Department')['Annual Salary'].sum()
categories = aggregated_data.index
sales = aggregated_data.values

fig, ax = plt.subplots(1, 2, figsize=(15, 7))

#to display bar chart

ax[0].bar(categories, sales, color='magenta', label='Total Sales')
ax[0].legend()
ax[0].set_title("Total Annual Salary by Department")
ax[0].set_xlabel("Department")
ax[0].set_ylabel("Total Annual Salary")
ax[0].grid(axis='y', linestyle='--', alpha=0.7)
ax[0].tick_params(axis='x', rotation=45)

#pie chart:

ax[1].pie(sales, labels=categories, autopct='%1.1f%%', startangle=90)
ax[1].set_title("")
#plt.xticks(rotation=45)

# plt.pie(sales, labels=categories, autopct='%1.1f%%', startangle=90)
# plt.title("Sales Distribution by Department")
# plt.show()

plt.tight_layout()
plt.show()