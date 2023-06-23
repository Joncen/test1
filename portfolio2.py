import numpy as np
import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt
import seaborn as sns


path = 'C:/Users/Jonathan/Documents/VSB-TUO/5. Semster/Bakalářské práce/Graphics/Portfolio'
# Import data
start_date = '2017/01/01'
end_date = '2022/01/19'

stocks = ['TROW','CRVL','ERIE', 'DHIL','SAFM','LANC','JJSF','DIT','UI', 'IPGP',\
 'NVDA','CDNS','HESAY','LULU','MED','WINA','INSP','SWAV','ABMD', \
 'ISRG','TWLO','FB','ROKU','SE','ROLL','KRDXF','HEI','WSO']

#stocks = ['AAPL','NKE','GOOGL', 'AMZN']

df = data.DataReader(stocks, 'yahoo', start = start_date, end = end_date)
print(df.head())

# Closing price
df = df['Adj Close']

# Log of porcentage change
#Plot Matice kovariace
plt.figure()
cov_matrix =df.pct_change().apply(lambda x: np.log(1 + x)).cov()
#cov_matrix =df.pct_change().cov()
fig_Matrice_Covariace = sns.heatmap(cov_matrix, cmap = 'Blues')
fig_Matrice_Covariace.set(xlabel = None)
fig_Matrice_Covariace.set(ylabel = None)
#plt.title('Matice kovariace', weight = 'bold')
print(cov_matrix)
#cov_matrix.to_excel("cov_matrix.xlsx", sheet_name = "cov_matrix")
plt.savefig(path + '/Matice_kovariace_Total.pdf', bbox_inches = 'tight' )



# Correlation
#corr_matrix = df.pct_change().apply(lambda x: np.log(1 + x)).corr()
#print(corr_matrix)

# Plot Matice korelace
plt.figure()
corr_matrix = df.pct_change().apply(lambda x: np.log(1 + x)).corr()
#corr_matrix = df.pct_change().corr()
#corr_matrix.to_excel("corr_matrix.xlsx", sheet_name = "corr_matrix")
fig_Matrice_correlace = sns.heatmap(corr_matrix, cmap = 'Blues', xticklabels = True, yticklabels = True)
fig_Matrice_correlace.set(xlabel = None)
fig_Matrice_correlace.set(ylabel = None)

plt.savefig(path + '/Matice_korelace_Total.pdf', bbox_inches = 'tight')


# Randomli weighted portafolio's variance
"""

w = {'TROW':0.0357, 'CRVL':0.0357,'ERIE':0.0357, 'DHIL':0.0357,'SAFM':0.0357,\
'LANC':0.0357,'JJSF':0.0357,'DIT':0.0357,'UI':0.0357, 'IPGP':0.0357,\
 'NVDA':0.0357, 'CDNS':0.0357,'HESAY':0.0357, 'LULU':0.0357, 'MED':0.0357,\
  'WINA':0.0357,'INSP':0.0357, 'SWAV':0.0357, 'ABMD':0.0357, \
 'ISRG':0.0357,'TWLO':0.0357,'FB':0.0357,'ROKU':0.0357, 'SE':0.0357,'ROLL':0.0357,\
 'KRDXF':0.0357, 'HEI':0.0357,'WSO':0.0357}

port_var =cov_matrix.mul(w, axis = 0).mul(w, axis = 1).sum().sum()
print(f"portfolio variance {port_var}")
"""
# Yearly returns for individual companies
ind_er = df.resample('Y').last().pct_change().mean()
print(f"Yearly returns for individual companies {ind_er}")
"""
# Portafolio returns
w = [0.0357, 0.0357, 0.0357, 0.0357, 0.0357, 0.0357, 0.0357, 0.0357\
, 0.0357, 0.0357, 0.0357, 0.0357, 0.0357, 0.0357, 0.0357, 0.0357, 0.0357, 0.0357\
, 0.0357, 0.0357, 0.0357, 0.0357, 0.0357, 0.0357, 0.0357, 0.0357, 0.0357, 0.0357]

port_er = (w*ind_er).sum()

print(f"portfolio returns {port_er}")
"""
# Volatility is given by annual standard deviation. We multiply by 250 becausae
# there are 250 trading days/years
ann_sd = df.pct_change().apply(lambda x: np.log(1 + x)).std().apply(lambda x: x*np.sqrt(250))
#ann_sd = df.pct_change().std().apply(lambda x: x*np.sqrt(250))
print("Annual SD")
print(ann_sd)

# Creating a table for visualising returns and volatility of assets
assets = pd.concat([ind_er, ann_sd], axis = 1)*100
assets.columns = ['Ocekavané výnosy', 'Volatilita']
print("Creating a table for visualising returns and volatility of assets")
print(assets)
assets.plot.scatter(x = 'Volatilita', y = 'Ocekavané výnosy', color = 'b', s = 20)
plt.xlabel('Volatilita (%)')
plt.ylabel('Ocekavané výnosy (%)')
# Insert names to stocks
for i, label in enumerate(stocks):
    plt.annotate(label, (assets['Volatilita'][i], assets['Ocekavané výnosy'][i]), fontsize=6)
plt.savefig(path + '/individual_stocks.pdf', bbox_inches = 'tight')



p_ret = []  # Define an empty array for portafolio returns
p_vol = []  # Define an empty array for portafolio volatility
p_weights = [] # Define an empty array for asset weights

num_assets = len(df.columns)
num_portafolios = 1000

for portafolio in range(num_portafolios):
    weights = np.random.random(num_assets)
    weights = weights/np.sum(weights)
    p_weights.append(weights)
    returns = np.dot(weights, ind_er) # Returns are the product of individual
                                    # expected returns of assets and its weights
    p_ret.append(returns)
    # Portafolio Variace
    var = cov_matrix.mul(weights, axis = 0).mul(weights, axis = 1).sum().sum()
    sd = np.sqrt(var) # Dayly standard deviation
    ann_sd = sd*np.sqrt(250) # Annual standard deviation = Volatility
    p_vol.append(ann_sd)

data = {'Ocekavané výnosy': p_ret, 'Volatilita': p_vol}

for counter, symbol in enumerate(df.columns.tolist()):
    # Print(counter, symbol)
    data[symbol] = [w[counter] for w in p_weights]

portafolios = pd.DataFrame(data)*100
print("Here are the head of the portfolios")
portafolios.head() # Dataframe of the 10000 portafolios created
print(portafolios.T)
portafolios.to_excel(path + '/weights.xlsx', sheet_name = "portfolios_weight")

# Plot efficient frontier
portafolios.plot.scatter(x = 'Volatilita', y = 'Ocekavané výnosy', marker = 'o', s = 10, alpha = 0.3)
plt.xlabel('Volatilita (%)')
plt.ylabel('Ocekavané výnosy (%)')
plt.savefig(path + '/portfolios.pdf', bbox_inches = 'tight')


min_vol_port = portafolios.iloc[portafolios['Volatilita'].idxmin()]
# idxmin() gives us the minimum value in the column specified
min_vol_port
print('minimum vol portfilio')
print('='*50)
print(min_vol_port[0:2])
print('='*50)# Ploting the minimum volatility portafoilo
# plt.subplots(figsize = [10, 10])
portafolios.plot.scatter(x = 'Volatilita', y = 'Ocekavané výnosy', marker = 'o', s = 10, alpha = 0.3)
#plt.scatter(portafolios['Volatility'], portafolios['Returns'], marker = 'o', s = 10, alpha = 0.3)
#portafolios['Volatility'], portafolios['Returns'], marker = 'o', s = 10, alpha = 0.3)
plt.scatter(min_vol_port[1], min_vol_port[0], color = 'r', marker = '*', s = 50)
plt.xlabel('Volatilita (%)')
plt.ylabel('Ocekavané výnosy (%)')
plt.savefig(path + '/portfolios_and_minim.pdf', bbox_inches = 'tight')

#plt.scatter(optimal_risky_port[1], optimal_risky_port[0], color = 'g', marker = '*', s = 50)

# Finding the optimal portafolio
rf = 0.01 # risk factor (0.01)
optimal_risky_port =portafolios.iloc[((portafolios['Ocekavané výnosy']-rf)/portafolios['Volatilita']).idxmax()]
print('optimum portfolio')
optimal_risky_port[2:].to_frame().plot.bar(legend = False)
plt.xlabel('Akcie')
plt.savefig(path + '/weights.pdf', bbox_inches = 'tight')

print('='*50)
print(optimal_risky_port[0:2])
print('='*50)
#optimal_risky_port[2:].plot.bar()

#Weight for sectors
sectors = pd.DataFrame()
list = ['FINAN','SP-ANTYC','TECH','SP-CYCL','ZDRAVT','KOMUNK','PRUMSL']
for i in range(0,7):
    sector = optimal_risky_port[4*i+2:4 + 4*i+2].sum()
    sector = pd.Series(sector, index = [list[i]])
    #print(optimal_risky_port[4*i+2:4 + 4*i+2].sum(), optimal_risky_port[4*i:4 + 4*i])
    sectors = pd.concat([sectors, sector.to_frame()])

print(sectors)
sectors.sort_values(by = [0]).plot.bar(legend = False, rot = 0)
plt.xlabel('Odvětví')
plt.savefig(path + '/weights_sector.pdf', bbox_inches = 'tight')

# Ploting optimal portafolio
# plt.subplots(figsize = (10, 10))
#plt.scatter(portafolios['Volatility'], portafolios['Returns'], marker = 'o', s = 10, alpha = 0.3)
portafolios.plot.scatter(x = 'Volatilita', y = 'Ocekavané výnosy', marker = 'o', s = 10, alpha = 0.3)
plt.scatter(min_vol_port[1], min_vol_port[0], color = 'r', marker = '*', s = 50)
plt.scatter(optimal_risky_port[1], optimal_risky_port[0], color = 'r', marker = '*', s = 50)
plt.xlabel('Volatilita (%)')
plt.ylabel('Ocekavané výnosy (%)')
plt.savefig(path + '/portfilio_with_min_and_optim.pdf', bbox_inches = 'tight')


portafolios.plot.scatter(x = 'Volatilita', y = 'Ocekavané výnosy', marker = 'o', s = 10, alpha = 0.3)
plt.scatter(min_vol_port[1], min_vol_port[0], color = 'r', marker = '*', s = 50)
plt.scatter(optimal_risky_port[1], optimal_risky_port[0], color = 'r', marker = '*', s = 50)
plt.scatter(assets['Volatilita'], assets['Ocekavané výnosy'], color = 'b', marker = 'o', s = 20)
for i, label in enumerate(stocks):
    plt.annotate(label, (assets['Volatilita'][i], assets['Ocekavané výnosy'][i]), fontsize=6)

plt.xlabel('Volatilita (%)')
plt.ylabel('Ocekavané výnosy (%)')
plt.savefig(path + '/portfilio_and_individual_stocks.pdf', bbox_inches = 'tight')


plt.show()
