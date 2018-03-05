import pandas as pd


data = pd.read_csv("fitness_summary_all_replicates.csv")
# Add all parameters (Taylor coefficients) as 0 in rows following the data:
for i in range(data.shape[0]):
        for j in range(16, 48):
                data.set_value(i, j, 0)
data.rename(columns={16: "a", 17: "a1", 18: "a2", 19: "a3", 20: "a4", 21: "a5",
        22: "b12", 23: "b13", 24: "b14", 25: "b15", 26: "b23", 27: "b24",
        28: "b25", 29: "b34", 30: "b35", 31: "b45", 32: "c123", 33: "c124",
        34: "c125", 35: "c134", 36: "c135", 37: "c145", 38: "c234", 39: "c235",
        40: "c245", 41: "c345", 42: "d1234", 43: "d1235", 44: "d1245",
        45: "d1345", 46: "d2345", 47: "e12345"}, inplace=True)

# Change coefficients corresponding to present effects to 1:
for index, row in data.iterrows():
	species = row["LP"] + row["LB"] + row["AP"] + row["AT"] + row["AO"]
	if species == "YNNNN":
		data.set_value(index, "a", 1)
		data.set_value(index, "a1", 1)
	if species == "NYNNN":
		data.set_value(index, "a", 1)
		data.set_value(index, "a2", 1)
	if species == "NNYNN":
		data.set_value(index, "a", 1)
		data.set_value(index, "a3", 1)
	if species == "NNNYN":
		data.set_value(index, "a", 1)
		data.set_value(index, "a4", 1)
	if species == "NNNNY":
		data.set_value(index, "a", 1)
		data.set_value(index, "a5", 1)
	if species == "YYNNN":
		data.set_value(index, "a", 1)
		data.set_value(index, "a1", 1)
		data.set_value(index, "a2", 1)
		data.set_value(index, "b12", -1)
	if species == "YNYNN":
		data.set_value(index, "a", 1)
		data.set_value(index, "a1", 1)
		data.set_value(index, "a3", 1)
		data.set_value(index, "b13", -1)
	if species == "YNNYN":
		data.set_value(index, "a", 1)
		data.set_value(index, "a1", 1)
		data.set_value(index, "a4", 1)
		data.set_value(index, "b14", -1)
	if species == "YNNNY":
		data.set_value(index, "a", 1)
		data.set_value(index, "a1", 1)
		data.set_value(index, "a5", 1)
		data.set_value(index, "b15", -1)
	if species == "NYYNN":
		data.set_value(index, "a", 1)
		data.set_value(index, "a2", 1)
		data.set_value(index, "a3", 1)
		data.set_value(index, "b23", -1)
	if species == "NYNYN":
		data.set_value(index, "a", 1)
		data.set_value(index, "a2", 1)
		data.set_value(index, "a4", 1)
		data.set_value(index, "b24", -1)
	if species == "NYNNY":
		data.set_value(index, "a", 1)
		data.set_value(index, "a2", 1)
		data.set_value(index, "a5", 1)
		data.set_value(index, "b25", -1)
	if species == "NNYYN":
		data.set_value(index, "a", 1)
		data.set_value(index, "a3", 1)
		data.set_value(index, "a4", 1)
		data.set_value(index, "b34", -1)
	if species == "NNYNY":
		data.set_value(index, "a", 1)
		data.set_value(index, "a3", 1)
		data.set_value(index, "a5", 1)
		data.set_value(index, "b35", -1)
	if species == "NNNYY":
		data.set_value(index, "a", 1)
		data.set_value(index, "a4", 1)
		data.set_value(index, "a5", 1)
		data.set_value(index, "b45", -1)
	if species == "YYYNN":
		data.set_value(index, "a", 1)
		data.set_value(index, "a1", 1)
		data.set_value(index, "a2", 1)
		data.set_value(index, "a3", 1)
		data.set_value(index, "b12", -1)
		data.set_value(index, "b13", -1)
		data.set_value(index, "b23", -1)
		data.set_value(index, "c123", 1)
	if species == "YYNYN":
		data.set_value(index, "a", 1)
		data.set_value(index, "a1", 1)
		data.set_value(index, "a2", 1)
		data.set_value(index, "a4", 1)
		data.set_value(index, "b12", -1)
		data.set_value(index, "b14", -1)
		data.set_value(index, "b24", -1)
		data.set_value(index, "c124", 1)
	if species == "YYNNY":
		data.set_value(index, "a", 1)
		data.set_value(index, "a1", 1)
		data.set_value(index, "a2", 1)
		data.set_value(index, "a5", 1)
		data.set_value(index, "b12", -1)
		data.set_value(index, "b15", -1)
		data.set_value(index, "b25", -1)
		data.set_value(index, "c125", 1)
	if species == "NYYYN":
		data.set_value(index, "a", 1)
		data.set_value(index, "a2", 1)
		data.set_value(index, "a3", 1)
		data.set_value(index, "a4", 1)
		data.set_value(index, "b23", -1)
		data.set_value(index, "b24", -1)
		data.set_value(index, "b34", -1)
		data.set_value(index, "c234", 1)
	if species == "NNYYY":
		data.set_value(index, "a", 1)
		data.set_value(index, "a3", 1)
		data.set_value(index, "a4", 1)
		data.set_value(index, "a5", 1)
		data.set_value(index, "b34", -1)
		data.set_value(index, "b35", -1)
		data.set_value(index, "b45", -1)
		data.set_value(index, "c345", 1)
	if species == "YNYYN":
		data.set_value(index, "a", 1)
		data.set_value(index, "a1", 1)
		data.set_value(index, "a3", 1)
		data.set_value(index, "a4", 1)
		data.set_value(index, "b13", -1)
		data.set_value(index, "b14", -1)
		data.set_value(index, "b34", -1)
		data.set_value(index, "c134", 1)
	if species == "YNYNY":
		data.set_value(index, "a", 1)
		data.set_value(index, "a1", 1)
		data.set_value(index, "a3", 1)
		data.set_value(index, "a5", 1)
		data.set_value(index, "b13", -1)
		data.set_value(index, "b15", -1)
		data.set_value(index, "b35", -1)
		data.set_value(index, "c135", 1)
	if species == "YNNYY":
		data.set_value(index, "a", 1)
		data.set_value(index, "a1", 1)
		data.set_value(index, "a4", 1)
		data.set_value(index, "a5", 1)
		data.set_value(index, "b14", -1)
		data.set_value(index, "b15", -1)
		data.set_value(index, "b45", -1)
		data.set_value(index, "c145", 1)
	if species == "NYNYY":
		data.set_value(index, "a", 1)
		data.set_value(index, "a2", 1)
		data.set_value(index, "a4", 1)
		data.set_value(index, "a5", 1)
		data.set_value(index, "b24", -1)
		data.set_value(index, "b25", -1)
		data.set_value(index, "b45", -1)
		data.set_value(index, "c245", 1)
	if species == "NYYNY":
		data.set_value(index, "a", 1)
		data.set_value(index, "a2", 1)
		data.set_value(index, "a3", 1)
		data.set_value(index, "a5", 1)
		data.set_value(index, "b23", -1)
		data.set_value(index, "b25", -1)
		data.set_value(index, "b35", -1)
		data.set_value(index, "c235", 1)
	if species == "YYYYN":
		data.set_value(index, "a", 1)
		data.set_value(index, "a1", 1)
		data.set_value(index, "a2", 1)
		data.set_value(index, "a3", 1)
		data.set_value(index, "a4", 1)
		data.set_value(index, "b12", -1)
		data.set_value(index, "b13", -1)
		data.set_value(index, "b14", -1)
		data.set_value(index, "b23", -1)
		data.set_value(index, "b24", -1)
		data.set_value(index, "b34", -1)
		data.set_value(index, "c123", 1)
		data.set_value(index, "c124", 1)
		data.set_value(index, "c134", 1)
		data.set_value(index, "c234", 1)
		data.set_value(index, "d1234", -1)
	if species == "YYYNY":
		data.set_value(index, "a", 1)
		data.set_value(index, "a1", 1)
		data.set_value(index, "a2", 1)
		data.set_value(index, "a3", 1)
		data.set_value(index, "a5", 1)
		data.set_value(index, "b12", -1)
		data.set_value(index, "b13", -1)
		data.set_value(index, "b15", -1)
		data.set_value(index, "b23", -1)
		data.set_value(index, "b25", -1)
		data.set_value(index, "b35", -1)
		data.set_value(index, "c123", 1)
		data.set_value(index, "c125", 1)
		data.set_value(index, "c135", 1)
		data.set_value(index, "c235", 1)
		data.set_value(index, "d1235", -1)
	if species == "YYNYY":
		data.set_value(index, "a", 1)
		data.set_value(index, "a1", 1)
		data.set_value(index, "a2", 1)
		data.set_value(index, "a4", 1)
		data.set_value(index, "a5", 1)
		data.set_value(index, "b12", -1)
		data.set_value(index, "b14", -1)
		data.set_value(index, "b15", -1)
		data.set_value(index, "b24", -1)
		data.set_value(index, "b25", -1)
		data.set_value(index, "b45", -1)
		data.set_value(index, "c124", 1)
		data.set_value(index, "c125", 1)
		data.set_value(index, "c145", 1)
		data.set_value(index, "c245", 1)
		data.set_value(index, "d1245", -1)
	if species == "YNYYY":
		data.set_value(index, "a", 1)
		data.set_value(index, "a1", 1)
		data.set_value(index, "a3", 1)
		data.set_value(index, "a4", 1)
		data.set_value(index, "a5", 1)
		data.set_value(index, "b13", -1)
		data.set_value(index, "b14", -1)
		data.set_value(index, "b15", -1)
		data.set_value(index, "b34", -1)
		data.set_value(index, "b35", -1)
		data.set_value(index, "b45", -1)
		data.set_value(index, "c134", 1)
		data.set_value(index, "c135", 1)
		data.set_value(index, "c145", 1)
		data.set_value(index, "c345", 1)
		data.set_value(index, "d1345", -1)
	if species == "NYYYY":
		data.set_value(index, "a", 1)
		data.set_value(index, "a2", 1)
		data.set_value(index, "a3", 1)
		data.set_value(index, "a4", 1)
		data.set_value(index, "a5", 1)
		data.set_value(index, "b23", -1)
		data.set_value(index, "b24", -1)
		data.set_value(index, "b25", -1)
		data.set_value(index, "b34", -1)
		data.set_value(index, "b35", -1)
		data.set_value(index, "b45", -1)
		data.set_value(index, "c234", 1)
		data.set_value(index, "c235", 1)
		data.set_value(index, "c245", 1)
		data.set_value(index, "c345", 1)
		data.set_value(index, "d2345", -1)
	if species == "YYYYY":
		data.set_value(index, "a", 1)
		data.set_value(index, "a1", 1)
		data.set_value(index, "a2", 1)
		data.set_value(index, "a3", 1)
		data.set_value(index, "a4", 1)
		data.set_value(index, "a5", 1)
		data.set_value(index, "b12", -1)
		data.set_value(index, "b13", -1)
		data.set_value(index, "b14", -1)
		data.set_value(index, "b15", -1)
		data.set_value(index, "b23", -1)
		data.set_value(index, "b24", -1)
		data.set_value(index, "b25", -1)
		data.set_value(index, "b34", -1)
		data.set_value(index, "b35", -1)
		data.set_value(index, "b45", -1)
		data.set_value(index, "c123", 1)
		data.set_value(index, "c124", 1)
		data.set_value(index, "c125", 1)
		data.set_value(index, "c134", 1)
		data.set_value(index, "c135", 1)
		data.set_value(index, "c145", 1)
		data.set_value(index, "c234", 1)
		data.set_value(index, "c235", 1)
		data.set_value(index, "c245", 1)
		data.set_value(index, "c345", 1)
		data.set_value(index, "d1234", -1)
		data.set_value(index, "d1235", -1)
		data.set_value(index, "d1245", -1)
		data.set_value(index, "d1345", -1)
		data.set_value(index, "d2345", -1)
		data.set_value(index, "e12345", 1)
	if species == "NNNNN":
		data.set_value(index, "a", 1)
data.to_csv("fitness_summary_all_replicates_parameters.csv", sep="\t")
