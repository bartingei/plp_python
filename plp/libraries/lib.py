import matplotlib.pyplot as plt


#Simple Line Plot:
# Plotting Age vs. Name
plt.plot(df['Name'], df['Age'])
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('Name vs Age')
plt.show()

# Plotting a bar chart for Age by City
df.groupby('City')['Age'].mean().plot(kind='bar')
plt.xlabel('City')
plt.ylabel('Average Age')
plt.title('Average Age by City')
plt.show()

# Plotting a histogram for Age
df['Age'].plot(kind='hist', bins=10)
plt.xlabel('Age')
plt.title('Age Distribution')
plt.show()

# Plotting a scatter plot of Age vs. City
df.plot(kind='scatter', x='City', y='Age')
plt.title('City vs Age')
plt.show()

#Customizing Plots
#Adding Labels and Title
plt.xlabel('City')
plt.ylabel('Average Age')
plt.title('Average Age by City')

#Color and Style
df['Age'].plot(kind='line', color='green', linestyle='--', linewidth=2)