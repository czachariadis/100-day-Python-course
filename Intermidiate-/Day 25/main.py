# # with open ("weather-data.csv","r") as d_file:
# #     data = d_file.readlines()
# #     print(data)


# # import csv


# # with open ("weather-data.csv","r") as d_file:
# #     data = csv.reader(d_file)
# #     temperatures = []
# #     # Skip the header
# #     next(data)
# #     for row in data:
# #         temperature = row[1].strip(",")
# #         temperature = int(temperature)
# #         temperatures.append(temperature)
        
        
# import pandas as pd


# data = pd.read_csv("weather-data.csv")
# data_dict = data.to_dict()
# temp_list = data["temp"].to_list()
# average = sum(temp_list) / len(temp_list)
# print(average)
# print(data["temp"].mean())


import pandas as pd


colors_count = {"gray": 0, "red": 0, "black": 0}
data = pd.read_csv("squirel_data.csv")
colors = data["Primary Fur Color"].tolist()

for color in colors:
    if (color == "Gray"):
        colors_count["gray"] += 1
    elif (color == "Cinnamon"):
        colors_count["red"] += 1
    elif (color == "Black"):
        colors_count["black"] += 1

# Create a DataFrame from the color counts. // DON'T FORGET TO USE THE items() FUNCTION HERE!!! //
df = pd.DataFrame(list(colors_count.items()), columns=['Fur Color', 'Count'])

# Save the DataFrame to a CSV file with tab separator
df.to_csv('squirel_count.csv', sep='\t', index=False)

# Read the saved CSV file into a new DataFrame
new_df = pd.read_csv('squirel_count.csv', sep='\t')