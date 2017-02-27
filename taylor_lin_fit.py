import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

data = pd.read_csv("fitness_summary_all_replicates_parameters.csv", sep="\t")
lm_devtime = smf.ols(formula="development ~ a + a1 + a2 + a3 + a4 + a5 +"
                             "b12 + b13 + b14 + b15 + b23 + b24 + b25 + b34 + b35 + b45 +"
                             "c123 + c124 + c125 + c134 + c135 + c145 + c234 + c235 + c245 + c345 +"
                             "d1234 + d1235 + d1245 + d1345 + d2345 + e12345", data=data).fit()
lm_fitness = smf.ols(formula="fitness ~ a + a1 + a2 + a3 + a4 + a5 +"
                             "b12 + b13 + b14 + b15 + b23 + b24 + b25 + b34 + b35 + b45 +"
                             "c123 + c124 + c125 + c134 + c135 + c145 + c234 + c235 + c245 + c345 +"
                             "d1234 + d1235 + d1245 + d1345 + d2345 + e12345", data=data).fit()
model_params = ("a", "a1", "a2", "a3", "a4", "a5", "b12", "b13", "b14", "b15",
                "b23", "b24", "b25", "b34", "b35", "b45", "c123", "c124", "c125",
                "c134", "c135", "c145", "c234", "c235", "c245", "c345", "d1234",
                "d1235", "d1245", "d1345", "d2345", "e12345")

output_file = open("taylor_lin_fit_result.txt", "w")
output_file.write("## Results for development time\n\n")
output_file.write(str(lm_devtime.summary()))
output_file.write(str(lm_devtime.params))
output_file.write("\n\n### Confidence intervals\n\n")
output_file.write(str(lm_devtime.conf_int()))
output_file.write("\n\n\n## Results for fitness\n\n")
output_file.write(str(lm_fitness.summary()))
output_file.write(str(lm_fitness.params))
output_file.write("\n\n### Confidence intervals\n\n")
output_file.write(str(lm_fitness.conf_int()))
output_file.close()

print(lm_devtime.summary())
print(lm_devtime.params)
print(lm_devtime.conf_int())
print(lm_fitness.summary())
print(lm_fitness.params)
print(lm_fitness.conf_int())
