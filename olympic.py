import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv("dataset_olympics.csv")

data.head()

data.info()

print(data.describe())

data.isna().sum()

data.duplicated().sum()

data.drop_duplicates(inplace=True)

data.duplicated().sum()

# sns.countplot(data= data, x ="Sex")
# plt.title("distribution by gender")
# # plt.show()

# sns.histplot(data= data, x= "Age", bins=20, kde=True )
# plt.title("Age Distribution")
# # plt.show()

# sns.histplot(data=data, x="Height",bins=20,kde=True )
# plt.title("Height Distribution")
# # plt.show()

# sns.histplot(data=data, x="Weight",bins=20,kde=True )
# plt.title("weight Distribution")
# # plt.show()

# sns.countplot(data=data, x="Medal" )
# plt.title("Medal Distribution")
# # plt.show()


# sns.countplot(data=data, x="Year", hue="Medal")
# plt.title("medal distribution over the years")
# plt.xticks(rotation=45)
# # plt.show()

year_avg_age=data.groupby("Year")["Age"].mean()
print(year_avg_age)

sport_median_height=data.groupby("Sport")["Height"].median()
print(sport_median_height)

sport_median_height[sport_median_height==190.0]

country_gender_count= data.groupby(["NOC", "Sex"])["ID"].count()
print(country_gender_count)

country_gold_medals=data[data["Medal"]=="Gold"].groupby("NOC")["Medal"].count()
print(country_gold_medals.max())

country_gold_medals[country_gold_medals==747]

sport_gender_avg_weight=data.groupby(["Sport","Sex"])["Weight"].mean()
print(sport_gender_avg_weight["Wrestling"]["F"])

# sport_event_count=data.groupby("Sport")["Event"].nunique().sort_values(ascending=False)
# sport_event_count.plot(kind="bar")
# plt.title("number of unique events per sport")
# plt.xlabel("sport")
# plt.ylabel("number of unique events")
# plt.xticks(rotation=45)
# plt.show()

# year_participant_count=data.groupby("Year")["ID"].nunique()
# year_participant_count.plot(kind="line", mark_right="o")
# plt.title("number of participants over the year")
# plt.xlabel("Year")
# plt.ylabel("number of participants")
# plt.show()

# country_avg_age= data.groupby("NOC")["Age"].mean().sort_values(ascending=False)
# country_avg_age.head(10).plot(kind="bar")
# plt.title("Top 10 Countries with highest average age of participants")
# plt.xlabel("Country")
# plt.ylabel("Average age")
# plt.xticks(rotation=45)
# plt.show()

# sns.boxplot(data=data, x="Season", y="Age")
# plt.title("Distribution of ages by season")
# plt.xlabel("Season")
# plt.ylabel("Age")
# plt.show()

most_medal_country= data["NOC"].value_counts().idxmax()
print("Most medal-winning country:", most_medal_country)

tallest_athelete=data[data["Height"]==data["Height"].max()]
print("tallest_athelete:")
print(tallest_athelete[['ID',"Name","Height", "Sport"]])

heaviest_athelete=data[data["Weight"]==data["Weight"].max()]
print("heaviest_athelete:")
print(heaviest_athelete[['ID',"Name","Height", "Sport"]])

sns.scatterplot(data=data, x="Height",y="Weight", hue="Medal")
plt.title("Athelete Height vs Weight by medal status")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.legend(title="Medal")
plt.show()