import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Load the dataset
df = pd.read_csv('Customer-Churn.csv')

# df.info()
# print(df.head())

# -------Check for missing values
# print(df.isnull().sum())

# -------Check for duplicates 
# print(df.duplicated().sum())

#------- Check for data types
# print(df.dtypes)

# -------Check for unique values in each column
# print(df.nunique())
  
df['TotalCharges'] = df['TotalCharges'].replace({" ": '0'})
df['TotalCharges'] = df['TotalCharges'].astype(float)

# print(df.describe())

# ax = sns.countplot(data=df, x='Churn')

# ax.bar_label(ax.containers[0], label_type='edge', fontsize=12, color='black', weight='bold')
# ax.set_title('Customer Churn Count', fontsize=16, weight='bold')
# plt.show()

# -------Check % of churn count in pie chart
# gb = df['Churn'].value_counts()
# plt.pie(gb, labels=gb.index, autopct='%1.2f%%')
# plt.title('Churn Count in %')
# plt.show()

#--------- cheking data according Gender

# # Create the countplot
# ax = sns.countplot(data=df, x='gender', hue='Churn', palette='Set2')

# # Add count labels on top of each bar
# ax.bar_label(ax.containers[0], label_type='edge', fontsize=12, color='black', weight='bold')
# plt.title("Gender Count")
# plt.show()


# Create the countplot for SeniorCitizen
# ax = sns.countplot(data=df, x='SeniorCitizen', hue='Churn', palette='Set2')
# # Add count labels on top of each bar
# ax.bar_label(ax.containers[0], label_type='edge', fontsize=12, color='black', weight='bold')
# plt.title("Senior Citizen Count")
# plt.show()

# # Create the countplot for SeniorCitizen with percentage labels
# count_data = pd.crosstab(df['SeniorCitizen'], df['Churn'])

# # Convert to percentage
# percentage_data = count_data.div(count_data.sum(axis=1), axis=0) * 100

# # Plot the stacked bar chart
# ax = percentage_data.plot(kind='bar', stacked=True, figsize=(8, 6), colormap='Set2')

# # Add percentage labels on top of each segment
# for container in ax.containers:
#     for bar in container:
#         height = bar.get_height()
#         if height > 0:
#             ax.text(
#                 bar.get_x() + bar.get_width() / 2,
#                 bar.get_y() + height / 2,
#                 f'{height:.1f}%',
#                 ha='center',
#                 va='center',
#                 fontsize=11,
#                 fontweight='bold'
#             )

# # Customizing plot
# plt.title("Senior Citizen Churn Distribution (%)", fontsize=14)
# plt.xlabel("Senior Citizen")
# plt.ylabel("Percentage")
# plt.xticks([0, 1], ['Not Senior', 'Senior'])  # Rename x-axis labels if needed
# plt.legend(title="Churn")
# plt.tight_layout()
# plt.show()



# # # Create the Histogram for Tenure Count
# sns.histplot(data=df, x='tenure', bins=72, hue = 'Churn')
# plt.title("Tenure Count")
# plt.xlabel("Tenure")
# plt.ylabel("Count")
# plt.show()


# List of columns to plot
columns = ['PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
    'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies'
]

# Set the number of rows and columns for subplots
n_cols = 3
n_rows = -(-len(columns) // n_cols)  # ceiling division

# Create figure and axes
fig, axes = plt.subplots(n_rows, n_cols, figsize=(8, n_rows * 4))
axes = axes.flatten()  # Flatten in case it's 2D array

# Plot each column
for i, col in enumerate(columns):
    ax = axes[i]
    
    if col == 'tenure':
        # Plot a histogram or boxplot for numerical 'tenure'
        sns.histplot(data=df, x=col,hue='Churn',  ax=ax)
    else:
        # Categorical columns
        sns.countplot(data=df, x=col, hue='Churn', ax=ax,)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=0, ha='right')

    ax.set_title(f'{col} vs Churn')

# Remove empty plots if any
for j in range(i+1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()