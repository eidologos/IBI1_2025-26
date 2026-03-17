#define dictionary
pop_data = {"UK":(66.7, 69.2),"China":(1426, 1410),"Italy":(59.4, 58.9),"Brazil":(208.6, 212.0),"USA":(331.6, 340.1)}
change={}
for country,(pop20,pop24) in pop_data.items():
    growth_rate=((pop24-pop20)/pop20)*100
    change[country]=growth_rate
#print the population change in descending order
for country in sorted(change, key=change.get, reverse=True):
    print(f"{country}: {change[country]:.2f}%")
#identify which country has the largest increase and largest decrease
max_increase=max(change, key=change.get)
max_decrease=min(change, key=change.get)
print(f"The country with the largest increase in population is: {max_increase} with a growth rate of {change[max_increase]:.2f}%")
print(f"The country with the largest decrease in population is: {max_decrease} with a growth rate of {change[max_decrease]:.2f}%")
#create a bar chart to show the population change for each country
import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt
countries=list(change.keys())
growth_rates=list(change.values())
plt.bar(countries, growth_rates, color="skyblue")
plt.title("Population Growth Rate from 2020 to 2024")
plt.xlabel("Country")
plt.xticks(rotation=45)
plt.ylabel("Growth Rate (%)")
plt.tight_layout()
plt.show()