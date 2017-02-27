import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("fitness_summary_all_replicates.csv")
for i in range(data.shape[0]):
	for j in range(16, 48):
		data.set_value(i, j, 0)
data.rename(columns={16: "a", 17: "a1", 18: "a2", 19: "a3", 20: "a4", 21: "a5",
	22: "b12", 23: "b13", 24: "b14", 25: "b15", 26: "b23", 27: "b24",
	28: "b25", 29: "b34", 30: "b35", 31: "b45", 32: "c123", 33: "c124",
	34: "c125", 35: "c134", 36: "c135", 37: "c145", 38: "c234", 39: "c235",
	40: "c245", 41: "c345", 42: "d1234", 43: "d1235", 44: "d1245",
	45: "d1345", 46: "d2345", 47: "e12345"}, inplace=True)
data.to_csv("fitness_summary_all_replicates_parameter_columns.csv", sep="\t")

