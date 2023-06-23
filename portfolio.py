#-------------------------------------------------------------------------------
# This Script is based in the code developed by Shruti Dash
# https://www.machinelearningplus.com/machine-learning/portfolio-optimization-python-example/
#-------------------------------------------------------------------------------

import numpy as np
import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt
import seaborn as sns

path = 'C:/Users/Jonathan/Documents/VSB-TUO/5. Semster/Bakalářské práce/Graphics/Portfolio'

start_date = '2017/01/01'
end_date = '2022/01/19'
stocks = ['TROW','CRVL','ERIE', 'DHIL','SAFM','LANC','JJSF','DIT','UI', 'IPGP',\
 'NVDA','CDNS','HESAY','LULU','MED','WINA','INSP','SWAV','ABMD', \
 'ISRG','TWLO','FB','ROKU','SE','ROLL','KRDXF','HEI','WSO']

# Import data
df = data.DataReader(stocks, 'yahoo', start = start_date, end = end_date)
print(df.head())
df = df['Adj Close']

# Calculation and plot's covariance matrix
plt.figure()
covariance_matrix = df.pct_change().apply(lambda x: np.log(1 + x)).cov()
fig_Covariace_Matrix = sns.heatmap(covariance_matrix, cmap = 'Blues', xticklabels = True, yticklabels = True )
fig_Covariace_Matrix.set(xlabel = None)
fig_Covariace_Matrix.set(ylabel = None)
print(covariance_matrix)
#cov_matrix.to_excel("cov_matrix.xlsx", sheet_name = "cov_matrix")
plt.savefig(path + '/Covariance_Matrix_Total.pdf', bbox_inches = 'tight' )

# Calculation and plot's Correlation matrix
plt.figure()
Correlation_matrix = df.pct_change().apply(lambda x: np.log(1 + x)).corr()
fig_Correlation_Matrix = sns.heatmap(Correlation_matrix, cmap = 'Blues', xticklabels = True, yticklabels = True)
fig_Correlation_Matrix.set(xlabel = None)
fig_Correlation_Matrix.set(ylabel = None)
plt.savefig(path + '/Correlation_Matrix_Total.pdf', bbox_inches = 'tight')

# Yearly returns for individual companies
individual_earnings = df.resample('Y').last().pct_change().mean()

# Volatility is given by annual standard deviation. We multiply by 250 becausae
# there are 250 trading days/years
annual_std = df.pct_change().apply(lambda x: np.log(1 + x)).std().apply(lambda x: x*np.sqrt(250))
print(annual_std)

# Creation a table for visualising returns and volatility of individual assets
assets = pd.concat([individual_earnings, annual_std], axis = 1)*100
assets.columns = ['Ocekavané výnosy', 'Volatilita']
print(assets)
# Plot earnings vs standard deviation for individual assets
assets.plot.scatter(x = 'Volatilita', y = 'Ocekavané výnosy', color = 'b', s = 20)
plt.xlabel('Volatilita (%)')
plt.ylabel('Ocekavaný výnos (%)')
#Insertion's ticket according stock's name.
for i, label in enumerate(stocks):
    plt.annotate(label, (assets['Volatilita'][i], assets['Ocekavané výnosy'][i]), fontsize=6)
plt.savefig(path + '/individual_stocks.pdf', bbox_inches = 'tight')

# Simulation's portfilios
portfolio_returns = []  # Define an empty array for portafolio returns
portfolio_volatility = []  # Define an empty array for portafolio volatility
portfolio_weights = [] # Define an empty array for asset weights
num_assets = len(df.columns)
# Number of simulations
num_portafolios = 25000

for portafolio in range(num_portafolios):
    weights = np.random.random(num_assets)
    weights = weights/np.sum(weights)
    portfolio_weights.append(weights)
    returns = np.dot(weights, individual_earnings)

    portfolio_returns.append(returns)
    Variance = covariance_matrix.mul(weights, axis = 0).mul(weights, axis = 1).sum().sum()
    standard_dev = np.sqrt(Variance) # Dayly standard deviation
    annual_std = standard_dev*np.sqrt(250) # Annual standard deviation = Volatility
    portfolio_volatility.append(annual_std)

data = {'Ocekavané výnosy': portfolio_returns, 'Volatilita': portfolio_volatility}

# Organize data to report
for counter, symbol in enumerate(df.columns.tolist()):
    data[symbol] = [w[counter] for w in portfolio_weights]

portafolios = pd.DataFrame(data)*100
portafolios.head() # Dataframe of the 10000 portafolios created
print(portafolios.T)
portafolios.to_excel(path + '/weights.xlsx', sheet_name = "portfolios_weight")

# Plot efficient frontier
portafolios.plot.scatter(x = 'Volatilita', y = 'Ocekavané výnosy', marker = 'o', s = 10, alpha = 0.3)
plt.xlabel('Volatilita (%)')
plt.ylabel('Ocekavaný výnos (%)')
#plt.savefig(path + '/portfolios.pdf', bbox_inches = 'tight')

# Portfolio with the minimum volatility
min_volatility_portfolio = portafolios.iloc[portafolios['Volatilita'].idxmin()]
# idxmin() gives us the minimum value in the column specified
print('minimum vol portfilio')
print('='*50)
print(min_volatility_portfolio[0:2])
print('='*50)
# Plot the minimum volatility portafoilo with the other portfolios
portafolios.plot.scatter(x = 'Volatilita', y = 'Ocekavané výnosy', marker = 'o', s = 10, alpha = 0.3)
plt.scatter(min_volatility_portfolio[1], min_volatility_portfolio[0], color = 'r', marker = '*', s = 50)
plt.xlabel('Volatilita (%)')
plt.ylabel('Ocekavaný výnos (%)')
#plt.savefig(path + '/portfolios_and_minim.pdf', bbox_inches = 'tight')


# Finding the optimal portafolio
rf = 0.00160#0.0199 # risk free
optimal_risky_portfolio = portafolios.iloc[((portafolios['Ocekavané výnosy']-rf)/portafolios['Volatilita']).idxmax()]
print('optimum portfolio')
#optimal_risky_portfolio[2:].to_frame().sort_values(by = [13], ascending = False).plot.barh(legend = False)
#print(optimal_risky_portfolio)
#optimal_risky_portfolio[2:].to_frame().plot.barh(legend = False)
optim_portfolio = optimal_risky_portfolio[2:].to_frame()
optim_portfolio.columns = ['V']
print('='*50)
print('='*50)
print(optim_portfolio)
optim_portfolio = optim_portfolio.sort_values(by ='V')
optim_portfolio.plot.barh(legend = False)
#dfZD = dfZ.sort_values(by = [0], ascending = False)
plt.ylabel('Akcie')
plt.xlabel('Váha (%)')
plt.savefig(path + '/weights.pdf', bbox_inches = 'tight')

print('='*50)
print(optimal_risky_portfolio[0:2])
print('='*50)

#Weight for sectors
sectors = pd.DataFrame()
list = ['Finanční ','Spot.\nanticyklické','Tech','Spot.\ncyklické ','Zdravt','Komunik','Průmysl']
for i in range(0,7):
    sector = optimal_risky_portfolio[4*i+2:4 + 4*i+2].sum()
    sector = pd.Series(sector, index = [list[i]])
    sectors = pd.concat([sectors, sector.to_frame()])

print(sectors)
sectors.sort_values(by = [0], ascending = False).plot.bar(legend = False, rot = 0)
#plt.xlabel('Odvětví')
plt.savefig(path + '/weights_sector.pdf', bbox_inches = 'tight')

# Plot optimal portafolio with other portfolios
portafolios.plot.scatter(x = 'Volatilita', y = 'Ocekavané výnosy', marker = 'o', s = 10, alpha = 0.3)
plt.scatter(min_volatility_portfolio[1], min_volatility_portfolio[0], color = 'r', marker = '*', s = 50)
plt.scatter(optimal_risky_portfolio[1], optimal_risky_portfolio[0], color = 'r', marker = '*', s = 50)
plt.xlabel('Volatilita (%)')
plt.ylabel('Ocekavaný výnos (%)')
plt.savefig(path + '/portfilio_with_min_and_optim', bbox_inches = 'tight')

# Plot's individual stocks to compare with portfolios
portafolios.plot.scatter(x = 'Volatilita', y = 'Ocekavané výnosy', marker = 'o', s = 10, alpha = 0.3)
plt.scatter(min_volatility_portfolio[1], min_volatility_portfolio[0], color = 'r', marker = '*', s = 50)
plt.scatter(optimal_risky_portfolio[1], optimal_risky_portfolio[0], color = 'r', marker = '*', s = 50)
plt.scatter(assets['Volatilita'], assets['Ocekavané výnosy'], color = 'b', marker = 'o', s = 20)
#Insertion's ticket according stock's name.
for i, label in enumerate(stocks):
    plt.annotate(label, (assets['Volatilita'][i], assets['Ocekavané výnosy'][i]), fontsize=6)

plt.xlabel('Volatilita (%)')
plt.ylabel('Ocekavaný výnos (%)')
plt.savefig(path + '/portfilio_and_individual_stocks', bbox_inches = 'tight')

# Plot relation with other amount of simultions
portafolios.plot.scatter(x = 'Volatilita', y = 'Ocekavané výnosy', marker = 'o', s = 10, alpha = 0.3)
plt.scatter(optimal_risky_portfolio[1], optimal_risky_portfolio[0], color = 'r', marker = '*', s = 50,)
plt.scatter(x =22.151137 , y =41.487637 , color = 'k', marker = '*', s = 50)
plt.scatter(x =22.086006 , y =41.454814 , color = 'y', marker = '*', s = 50)
plt.scatter(x =22.52136 , y =40.870997, color = 'm', marker = '*', s = 50)
plt.scatter(x = 22.687744, y =40.127919 , color = 'k', marker = '*', s = 50)
plt.xlabel('Volatilita (%)')
plt.ylabel('Ocekavaný výnos (%)')
X = [21.686006, 21.686006, 22.52136, 22.687744]
Y = [42.04814, 40.870997, 40.870997, 40.127919 ]
labels = [100000, 50000, 10000, 5000]
for x, y, label in zip(X, Y, labels):
    plt.annotate(label, (x,y), fontsize=6)
plt.savefig(path + '/portfilio_relation_with_other_amount_of_simultions', bbox_inches = 'tight')

portf_compar = pd.read_csv(r"C:\Users\Jonathan\Documents\VSB-TUO\5. Semster\Bakalářské práce\Graphics\Portfolio\portfolio comparation.csv", index_col = 0,
 parse_dates = True)
portf_compar.index = list
portf_compar.sort_values(by = '25000', ascending = False).plot.bar(rot=0)
plt.savefig(path + '/weights_relations_per_areas.pdf', bbox_inches = 'tight')
print(portf_compar)



plt.show()
