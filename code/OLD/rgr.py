import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = 'rgr.csv'

raw = pd.read_csv(file)

drugs = raw.iloc[:,1:16]

names = []
for i in drugs:
    names.append(i)

raw

############## Figure RGR
plt.rcParams.update({'font.size': 22})
fig, ax = plt.subplots(figsize = (20, 10))

colors = ['b', 'rosybrown', 'r', 'sienna', 'pink', 'magenta', 'blueviolet', 'black', 'g', 'lime', 'darkorange', 'olivedrab', 'deepskyblue', 'slategrey', 'lawngreen']

for z, c in zip(names, colors):
    # print(z)
    plt.plot(raw['X-Values'][1:7], raw[z][1:7], color = c, linewidth=3.0)

ax.legend(frameon=False)
ax.set_title('Relative Growth per decades')
ax.set_ylabel('Relative growth rate')
ax.set_xlabel('Decades')

ax.set_xticks([1970, 1980, 1990, 2000, 2010, 2018])

ax.set_xlim([1970, 2018])
ax.set_ylim([0, 14])

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.savefig('rgr.svg', transparent = True, bbox_inches='tight')


############## Figure RGR alcohol, cannabis, LSD,
plt.rcParams.update({'font.size': 22})
fig, ax = plt.subplots(figsize = (20, 10))

colors = ['b', 'rosybrown', 'r', 'sienna', 'pink']
names_iso = ['Alcohol', 'WoS', 'Cannabis', 'LSD', 'Psilocybin']

for z, c in zip(names_iso, colors):
    # print(z)
    plt.plot(raw['X-Values'][1:7], raw[z][1:7], color = c, linewidth=3.0)

ax.legend(frameon=False)
ax.set_title('Relative Growth per decades')
ax.set_ylabel('Relative growth rate')
ax.set_xlabel('Decades')

ax.set_xticks([1970, 1980, 1990, 2000, 2010, 2018])

ax.set_xlim([1970, 2018])
ax.set_ylim([0, 14])

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.savefig('rgr_iso.svg', transparent = True, bbox_inches='tight')




raw['Cocaine'][1:8]
