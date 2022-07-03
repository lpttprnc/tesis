# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 18:55:34 2022

@author: lpttprnc
"""

import numpy as n
import pandas as pd
import matplotlib.pyplot as p

def burik (file):
    df=pd.read_csv(file)
    fini=df['f_init']
    rho=df['rho_smg']
    pres=df['p_smg']
    w=pres/rho
    return (fini,w)
    
d={} #d["string{0}".format(x)] =
#α=1, p= , n=1
for i in range(6):
    d["fp{0}".format(i)],d["wp{0}".format(i)]=burik('D:/Local Disk D/E/TA/coba/remake paper p 0-5 n 1 300x/a1p'+str(i)+'n1/output_data.csv')
    d["fn{0}".format(i)],d["wn{0}".format(i)]=burik('D:/Local Disk D/E/TA/coba/remake paper p 0-5 n 1 300x/a1p2n'+str(i)+'/output_data.csv')

p.title('plot 'r'$w_0$'' vs 'r'$\psi_{ini}$')
for ss in range(6):
    p.plot(d['fp'+str(ss)],d['wp'+str(ss)],label=r'$p=$'+str(ss))
#[21][22] patah
p.ylabel(r'$w_0$')
p.xlabel(r'$\psi_{ini}$')
p.legend()
p.show()

#α=1, p=2 , n=
p.title('plot 'r'$w_0$'' vs 'r'$\psi_{ini}$')
for ss in range(6):
    p.plot(d['fn'+str(ss)],d['wn'+str(ss)],label=r'$n=$'+str(ss))
p.ylabel(r'$w_0$')
p.xlabel(r'$\psi_{ini}$')
p.legend()
p.show()