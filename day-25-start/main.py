import pandas as pd
import os

print(os.getcwd())



with open("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240312.csv") as data_file:
    data = pd.read_csv(data_file)
    dict = {
        "color" : ["Gray", "Cinnamon", "Black"],
        "count" : [len(data[data["Primary Fur Color"] == "Gray"]), len(data[data["Primary Fur Color"] == "Cinnamon"]), len(data[data["Primary Fur Color"] == "Black"])]
    }
    df = pd.DataFrame(dict)
    #df.to_csv("./squirrel_count.csv")
    print(df.size)
    print(df.ndim)