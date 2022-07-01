import os, sys
import pandas as pd
import numpy as np

def run_bash_script(script):
    with open("running", "w") as fout:
        a=0
        os.system("{} < running".format(script))

f_init = np.linspace(0,10,10)

rho_smg = []
p_smg = []
wanted = []
par_c = []

start = time.time()
for f in f_init:
    file = open('gravity_models/alpha_attractor_canonical.ini', 'r')
    text = file.readlines()

    text[17] = 'parameters_smg =  1e-100, \t  {}, 8.530,  0,  3.140, 4.233\n'.format(f)  #f_prime_ini, f_ini, alpha, c^2, p, n
    #text[17] = 'parameters_smg =  1e-100, \t  {}, 8.530,  0,  3.140, 4.233\n'.format(f) #f_prime_ini, f_ini, alpha, c^2, p, n default

    with open('alpha_attractor_canonical.ini', 'w') as f:
        for t in text:
            f.write(t)
    try:
        run_bash_script("./class alpha_attractor_canonical.ini")
        data = pd.read_csv('gravity_models/output/alpha_attractor_canonical_background.dat',delimiter='\s+',skiprows=3)
        rho_smg.append(data.iloc[-1,15])
        p_smg.append(data.iloc[-1,16])
        
        data2 = pd.read_csv('gravity_models/output/alpha_attractor_canonical_nebengparameters.dat',delimiter='\s+',skiprows=0)
        wanted.append(data2.iloc[0,0]) #Omega smg wanted
        par_c.append(data2.iloc[0,1])
    except:
        rho_smg.append("NaN")
        p_smg.append("NaN")
        wanted.append("NaN") #Omega smg wanted
        par_c.append("NaN")

output_dat = pd.DataFrame({'f_init':f_init,'rho_smg':rho_smg,'p_smg':p_smg,'wanted_value':wanted,'c':par_c})
output_dat.to_csv('gravity_models/output/output_data.csv',index=False)
