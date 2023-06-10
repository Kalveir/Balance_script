import pandas as pd

csv_input = input("masukan nama csv file = ")
csv_output = input("masukan nama output csv file = ")
df = pd.read_csv(csv_input)

ones_subset = df.loc[df["Hasil"] == 1, :]
number_of_1s = len(ones_subset)

zeros_subset = df.loc[df["Hasil"] == 0, :]
sampled_zeros = zeros_subset.sample(number_of_1s)

clean_df = pd.concat([ones_subset, sampled_zeros], ignore_index=True)

clean_df.to_csv(csv_output,".csv")
