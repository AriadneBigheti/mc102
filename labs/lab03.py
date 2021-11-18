var_tosse = input()
tosse = var_tosse == "True"

var_febre =  input()
febre = var_febre == "True"

var_dif_respirar = input()
dificuldade_para_respirar = var_dif_respirar == "True"

covid_19 = tosse and febre and dificuldade_para_respirar

print("Tosse:", var_tosse)
print("Febre:", var_febre)
print("Dificuldade para respirar:", var_dif_respirar)
print("Provavelmente eh COVID-19:", covid_19)


