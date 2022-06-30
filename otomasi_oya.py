import os, sys
import pandas as pd
import numpy as np

def run_bash_script(script):
    with open("running", "w") as fout:
        a=0
        os.system("{} < running".format(script))

f_init = np.linspace(0,10,1000)

rho_smg = []
p_smg = []

for f in f_init:
    file = open('alpha_attractor_canonical.ini', 'r')
    text = file.readlines()

    text[17] = 'parameters_smg =  1e-100, \t  {}, 8.530,  0,  3.140, 4.233\n'.format(f)

    with open('alpha_attractor_canonical.ini', 'w') as f:
        for t in text:
            f.write(t)
    try:
        run_bash_script("./class alpha_attractor_canonical.ini")
        data = pd.read_csv('alpha_attractor_canonical_background.dat',delimiter='\s+',skiprows=3)
        rho_smg.append(data.iloc[-1,15])
        p_smg.append(data.iloc[-1,16])
    except:
        rho_smg.append("NaN")
        p_smg.append("NaN")

output_dat = pd.DataFrame({'rho_smg':rho_smg,'p_smg':p_smg})
output_dat.to_csv('output/output_data.csv')

