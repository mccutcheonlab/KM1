# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 14:50:17 2018

@author: James Rig
"""

import JM_general_functions as jmf
import JM_custom_figs as jmfig
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

## Colour scheme
col={}
col['np_cas'] = 'xkcd:silver'
col['np_malt'] = 'white'
col['lp_cas'] = 'xkcd:kelly green'
col['lp_malt'] = 'xkcd:light green'

def nplp2Dfig(df, factor1, factor2, ax):
    dietmsk = df.diet == 'NR'
    
    a = [[df[factor1][dietmsk], df[factor2][dietmsk]],
          [df[factor1][~dietmsk], df[factor2][~dietmsk]]]

    ax, x, _, _ = jmfig.barscatter(a, paired=True,
                 barfacecoloroption = 'individual',
                 barfacecolor = [col['np_cas'], col['np_malt'], col['lp_cas'], col['lp_malt']],
                 scatteredgecolor = ['xkcd:charcoal'],
                 scatterlinecolor = 'xkcd:charcoal',
                 grouplabel=['NR', 'PR'],
                 grouplabeloffset=0.1,
                 barlabels=['Cas', 'Malt', 'Cas', 'Malt'],
                 barlabeloffset=0.025,
                 scattersize = 80,
                 ax=ax)


metafile = 'C:\\Users\\jaimeHP\\Documents\\GitHub\KM1\\KM1_metafile.csv'

df = pd.read_csv(metafile)


mpl.rcParams['figure.subplot.left'] = 0.25
figKM1, ax = plt.subplots(figsize=(3, 4))
nplp2Dfig(df, 'cs-cas', 'cs-md', ax)
ax.set_ylabel('Intake (mL)')
try:
    figKM1.savefig('C:\\Users\\jaimeHP\\Dropbox\\AbstractsAndTalks\\180718_SSIB_Florida\\figs\\KM1.eps')
except FileNotFoundError:
    print('File not saved. Cannot find file path.')