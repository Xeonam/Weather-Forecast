import matplotlib.pyplot as plt

epochs = [ i for i in range(1, 30)]

datas1=[row.strip().split(sep=";") for row in open("./second_test_modell.csv")]
losses1 = [ float(datas1[i][2]) for i in range(1, 30)]
plt.plot(epochs,losses1,"r.")
datas2=[row.strip().split(sep=",") for row in open("./third_test_modell.csv")]
losses2= [ float(datas2[i][2]) for i in range(1, 30)]
plt.plot(epochs,losses2,"b.")
datas3=[row.strip().split(sep=",") for row in open("./fourth_test_modell.csv")]
losses3 = [ float(datas3[i][2]) for i in range(1, 30)]
plt.plot(epochs,losses3,"g.")

