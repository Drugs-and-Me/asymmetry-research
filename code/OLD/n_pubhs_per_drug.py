import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.patches as mpatches
import matplotlib.lines as mlines

file = '/Users/ivanezqrom/OneDrive - University College London/Documentos/Coding/Python/MHEF/asymmetry_research/data/n_pubs_per_drug.csv'
root = '/Users/ivanezqrom/OneDrive - University College London/Documentos/Coding/Python/MHEF/asymmetry_research/'
raw = pd.read_csv(file)

drugs = raw.iloc[:,2:16]
years = raw.iloc[:, 0]


############## Figure publications all
drugs = raw.iloc[:,1:16]
plt.rcParams.update({'font.size': 22})
fig, ax = plt.subplots(figsize = (20, 10))

colors = ['b', 'rosybrown', 'r', 'sienna', 'pink', 'magenta', 'blueviolet', 'black', 'g', 'lime', 'darkorange', 'olivedrab', 'deepskyblue', 'slategrey', 'lawngreen', 'darkviolet']

for z, c in zip(drugs, colors):
    # print(z)
    plt.plot(years, raw[z], color = c, linewidth=3.0, label = z)

ax.set_title('Number of publications for 15 psychoactive drugs.\n Including alcohol')
ax.set_ylabel('Number of publications')
ax.set_xlabel('Years')

ax.set_xticks([1960, 1970, 1980, 1990, 2000, 2010, 2018])

ax.set_xlim([1960, 2018])
# ax.set_ylim([0, 5000.01])

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))

plt.savefig('{}/figures/all.svg'.format(root), transparent = True, bbox_inches='tight')


############## Figure RGR all no alcohol
drugs = raw.iloc[:,2:16]
plt.rcParams.update({'font.size': 22})
fig, ax = plt.subplots(figsize = (20, 10))

colors = ['b', 'rosybrown', 'r', 'sienna', 'pink', 'magenta', 'blueviolet', 'black', 'g', 'lime', 'darkorange', 'olivedrab', 'deepskyblue', 'slategrey', 'lawngreen', 'darkviolet']

for z, c in zip(drugs, colors):
    # print(z)
    plt.plot(years, raw[z], color = c, linewidth=3.0, label = z)

ax.set_title('Number of publications for 14 psychoactive drugs.\n Excluding alcohol')
ax.set_ylabel('Number of publications')
ax.set_xlabel('Years')

ax.set_xticks([1960, 1970, 1980, 1990, 2000, 2010, 2018])

ax.set_xlim([1960, 2018])
ax.set_ylim([0, 5000.01])

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))

plt.savefig('{}/figures/all_no_alc.svg'.format(root), transparent = True, bbox_inches='tight')

drugs
############## Figure number pubs selected_two_axes
drugs_two = ['Cannabis', 'Ketamine', 'MDMA', 'Psilocybin']
alc_two = ['Alcohol']
plt.rcParams.update({'font.size': 22})
fig, ax = plt.subplots(figsize = (20, 10))

colors = ['green', 'grey', 'pink', 'sienna']
lns = []
for z, c in zip(drugs_two, colors):
    l = plt.plot(years, raw[z], color = c, linewidth=3.0, label = z)
    lns.append(l)

ax.set_title('Number of publications for common recreational drugs.\n')
ax.set_ylabel('Number of publications')
ax.set_xlabel('Years')

ax.set_xticks([1960, 1970, 1980, 1990, 2000, 2010, 2018])

ax.set_xlim([1960, 2018])
# ax.set_ylim([0, 5000.01])

ax2 = ax.twinx()
lns_alc = ax2.plot(years, raw['Alcohol'], color='b', label = 'Alcohol')

# added these three lines
# lns.append(lns_alc)


# for l in lns:
#     print(l[0].get_label())
# labs = [l[0].get_label() for l in lns]
# lns = [lns[0], lns[1], lns[2], lns[3], lns[4]]

alc = mlines.Line2D([], [], color='blue', label = 'Alcohol')
can = mlines.Line2D([], [], color='green', label = 'Cannabis')
md = mlines.Line2D([], [], color='pink', label = 'MDMA')
ket = mlines.Line2D([], [], color='grey', label = 'Ketamine')
psi = mlines.Line2D([], [], color='sienna', label = 'Psilocybin')

ax.legend(handles=[alc, can, md, ket, psi])

ax.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)

ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
ax2.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))

plt.savefig('{}/figures/selected_two_axes.svg'.format(root), transparent = True, bbox_inches='tight')


############## Figure WoS
plt.rcParams.update({'font.size': 22})
fig, ax = plt.subplots(figsize = (20, 10))

colors = ['k'] #, 'r', 'sienna', 'pink']
names_iso = ['WoS']  #'Cannabis', 'LSD', 'Psilocybin']

for z, c in zip(names_iso, colors):
    # print(z)
    plt.plot(years, raw[z], color = c, linewidth=3.0, label = 'Web of Science')

ax.legend(frameon=False)
ax.set_title('Total number of research publications')
ax.set_ylabel('Number of publications')
ax.set_xlabel('Years')


ax.set_xlim([1960, 2018])
ax.set_xticks([1960, 1970, 1980, 1990, 2000, 2010, 2018])

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))

plt.savefig('{}/figures/WoS.svg'.format(root), transparent = True, bbox_inches='tight')


############## Figure LSD, Psilocybin, alcohol
plt.rcParams.update({'font.size': 22})
fig, ax = plt.subplots(figsize = (20, 10))

colors = ['lawngreen', 'darkorange'] #, 'r', 'sienna', 'pink']
names_iso = ['LSD', 'Psilocybin']  #'Cannabis', 'LSD', 'Psilocybin']


for z, c in zip(names_iso, colors):
    # print(z)
    plt.plot(years, raw[z], color = c, linewidth=3.0, label = z)

# ax.legend(frameon=False)
ax.set_title('Total number of research publications')
ax.set_ylabel('Number of publications: LSD & Psilocybin')
ax.set_xlabel('Years')

ax.set_xlim([1960, 2018])
ax.set_xticks([1960, 1970, 1980, 1990, 2000, 2010, 2018])

ax2 = ax.twinx()
lns_alc = ax2.plot(years, raw['Alcohol'], color='b', label = 'Alcohol')

# added these three lines
# lns.append(lns_alc)


# for l in lns:
#     print(l[0].get_label())
# labs = [l[0].get_label() for l in lns]
# lns = [lns[0], lns[1], lns[2], lns[3], lns[4]]

alc = mlines.Line2D([], [], color='b', label = 'Alcohol')
psi = mlines.Line2D([], [], color='darkorange', label = 'Psilocybin')
lsd = mlines.Line2D([], [], color='lawngreen', label = 'LSD')

ax.legend(handles=[alc, psi, lsd])

ax.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)

ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
ax2.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
ax2.set_ylabel('Number of publications: Alcohol')
ax2.yaxis.label.set_color('b')
ax2.spines['right'].set_color('b')


plt.savefig('{}/figures/psyche_alc.svg'.format(root), transparent = True, bbox_inches='tight')
