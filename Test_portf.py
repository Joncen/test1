import numpy as np
import pandas as pd
#from pandas_datareader import data
import pandas_datareader as pdr
import matplotlib.pyplot as plt
from datetime import date
import mplfinance as mpf
import seaborn as sns
sns.set_style("darkgrid")

#http://serverarekore.blogspot.com/2020/10/mplfinance.html


# Path according local position
path = 'C:/Users/Jonathan/Documents/VSB-TUO/5. Semster/Bakalářské práce/Graphics'
#Interval for data extraction
today = date.today()
start_date = '2017/01/01'
end_date = '2022/01/19'

Financial_services = [
'TROW', 'CRVL',	'ERIE', 'DHIL']#'V'

Consumer_defensive = ['SAFM','LANC','JJSF',	'DIT']

#Technology = ['SITM',	'SNOW',	'NVDA',	'MNDY']#'VRSN','AMBA'
Technology = ['UI', 'IPGP', 'NVDA', 'CDNS']
Consumer_cyclical = ['HESAY', 'LULU', 'MED', 'WINA']

Healthcare = ['INSP', 'SWAV', 'ABMD', 'ISRG']

Comunication_services = ['TWLO', 'FB', 'ROKU', 'SE']

Industrials = ['ROLL',	'KRDXF', 'HEI',	'WSO']

#"""

sectors = [Financial_services, Consumer_defensive, Technology, \
Consumer_cyclical, Healthcare, Comunication_services, Industrials]

#Preliminar list of stocks
#list_company = ['TROW', 'CRVL', 'ERIE','DHIL', 'ADBE', 'CSCO', 'GE']
# Import data from yahoo
#df = data.DataReader(list_company, 'yahoo', start = date_start, end = date_end)
#df = pdr.get_data_yahoo(list_company, start = start_date, end = end_date)

#df_monthly = pdr.get_data_yahoo(list_company, start = '2017/01/01', end = end_date, interval = 'mo')
#print(df_monthly.head())
#'2021/08/20' start candles
print("head values")
#print(df.head())


#df_total = df['Adj Close']
"""
# Plot Matice korelace
plt.figure()
corr_matrix = df_total.pct_change().apply(lambda x: np.log(1 + x)).corr()
print(corr_matrix)
corr_matrix.to_excel("corr_matrix.xlsx", sheet_name = "corr_matrix")
fig_Matrice_correlace = sns.heatmap(corr_matrix, cmap = 'Blues')
fig_Matrice_correlace.set(xlabel = None)
fig_Matrice_correlace.set(ylabel = None)
#plt.title('Matice korelace', weight = 'bold')
plt.savefig(path + '/Matice_korelace_Total.pdf')

#Plot Matice kovariace
plt.figure()
cov_matrix =df_total.pct_change().apply(lambda x: np.log(1 + x)).cov()
fig_Matrice_Covariace = sns.heatmap(cov_matrix, cmap = 'Blues')
fig_Matrice_Covariace.set(xlabel = None)
fig_Matrice_Covariace.set(ylabel = None)
#plt.title('Matice kovariace', weight = 'bold')
print(cov_matrix)
cov_matrix.to_excel("cov_matrix.xlsx", sheet_name = "cov_matrix")
plt.savefig(path + '/Matice_kovariace_Total.pdf')
"""

#Final list of stocks
i = 0
for company in sectors:
    df_monthly = pdr.get_data_yahoo(company, start = start_date, end = end_date, interval = 'mo')
    i = i + 1
    #company = ['TROW', 'CRVL', 'ERIE','DHIL']
    """
    #Interchamge headers, helps to choose according company
    df_swap = df.swaplevel(0,1, axis = 1).sort_index(axis = 1)
    df_selected = df_swap[company]
    # Selection of only Closing price
    df1 = df_selected.xs('Adj Close', axis = 1, level = 1)
    print(df1.head())
    """
    """
    # Plot of Vynos pro kazde akcií
    df_vynos = df1.pct_change()
    df_vynos.plot(subplots = True)
    plt.xlabel('Rok', weight = 'bold')
    plt.savefig(path + '/Vynos somostatne akcií v portfolia.pdf')
    """
    #Interchamge headers, helps to choose according company
    df_swap = df_monthly.swaplevel(0,1, axis = 1).sort_index(axis = 1)
    """
    df_selected = df_swap[company]
    # Selection of only Closing price
    df1 = df_selected.xs('Adj Close', axis = 1, level = 1)
    print(df1.head())
    """
    """

    # Plot of Vynos pro kazde akcií
    df_vynos = df1.pct_change()*100

    #df_vynos.plot(subplots =True)
    #plt.xlabel('Rok')
    #plt.savefig(path + f'/Mesicni Vynos somostatne akcií v portfoliu_{i}.pdf')


    fig, axes = plt.subplots()
    axes = df_vynos.plot.bar(subplots = True, sharex = False, rot = 0, ax = axes)
    # -----------------------------------------------------------------------
    # This part is based on the code of Patrick FitzGerald
    #https://stackoverflow.com/questions/66334236/matplotlib-python\
    #-bar-plot-how-to-show-months-only-rather-than-showing-dates-fo
    ticks = [idx for idx, timestamp in enumerate(df_vynos.index) \
         if (timestamp.month != df_vynos.index[idx-1].month) | (idx == 0)]
    labels = [tick.strftime('%Y') if (df_vynos.index[ticks[idx]].year \
          != df_vynos.index[ticks[idx-1]].year) | (idx == 0) else\
           tick.strftime('')\
          for idx, tick in enumerate(df_vynos.index[ticks])]
    # -----------------------------------------------------------------------
    plt.subplots_adjust(hspace = 0.4)
    for k in range(0,4):
        axes[k].set_title('')
        axes[k].set_xticklabels(labels)
        if k ==3:
            axes[k].set_xlabel('Rok')
        else:
            axes[k].set_xlabel('')

        #ymin, ymax = axes[k].get_ylim()
        #plt.sca(axes[ymin,ymax])
        #plt.xticks([])
        #plt.ylim([ymin, ymax])
        #fig.update_yaxis(range = [ymin, ymax])
    plt.savefig(path + f'/Mesicni Vynos somostatne akcií v portfoliu_{i}.pdf')
    """
    """

    #  plot of all stocks in the selected portfolio
    df1.plot()
    #plt.title('Roční evoluce akcií portfolia', fontweight = 'bold')
    plt.xlabel('Rok')
    plt.ylabel('Cena (USD)')
    plt.legend()
    plt.savefig(path + '/Roční evoluce akcií portfolia.pdf')


    """


    # ------------OBS> IS neccesary -LESS DATA-------
    # ------Candles Plot for every stock---------------------------
    #"""
    df_swap2 = df_monthly.swaplevel(0,1, axis = 1).sort_index(axis = 1)

    for stock in company:
        df_stock= df_swap2.xs(stock, axis = 1)
        filename = path + f'/Candle_{stock}_{i}.pdf'
        #cs  = mpf.make_mpf_style(gridcolor="lightgray", mavcolors=['red', 'green', '#405173'])
        df_vynos = df_stock['Adj Close'].pct_change()*100

        monthly_return = [mpf.make_addplot((df_vynos), panel = 1, type = 'bar', ylabel = 'Měsíční výnos (%)')]
        #fig, axes = mpf.plot(df_stock, type = 'candle', style = 'sas', tight_layout = True, ylabel = 'Price (USD)', mav = (5, 14, 30), volume = True, returnfig = True, savefig = filename)
        fig, axes = mpf.plot(df_stock, addplot = monthly_return, type = 'candle', style = 'sas', ylabel = 'Cena (USD)', tight_layout = True, mav = (5, 14, 30), volume = False, returnfig = True, savefig = filename)
        fig.set_xlabel('Cena (USD)')
        #plt.text(0.8, 200, "MA (30)", fontweight = 'bold', color = 'blue')
        #plt.text(0.8, 195, "MA (14)", fontweight = 'bold', color = 'orange')
        #plt.text(0.8, 190, "MA (5)", fontweight = 'bold', color = 'green')


        # mav calculate Mean average for 5, 14 and 30 days
        #fig.set_xlabel('Cena (USD)')


        #style = 'sas'
        # 'nightclouds'
    #"""
    sns.set_style("darkgrid")
    """

    #------Boxes Plot  for every stock---------------------------
    fig, ax = plt.subplots(2,2)
    i = 0
    nrow = 2
    ncol = 2
    for r in range(nrow):
        for c in range(ncol):
                df1[company[i]].plot.box( ax = ax[r,c])
                plt.tight_layout()
                #ax[r,c].set_xlabel(fontweight = 'bold')
                ax[r,c].set_ylabel('Cena (USD)')
                i = i + 1
    plt.savefig(path + '/Box_data_portfolia.pdf')
    #fig.suptitle('ksdhfkh', fontsize = 12, color = 'black', fontweight = 'bold')

    # Plot histograms of all stocks
    fig, ax = plt.subplots(2,2)
    i = 0
    nrow = 2
    ncol = 2
    for r in range(nrow):
        for c in range(ncol):
                df1[company[i]].plot.hist( ax = ax[r,c])
                plt.tight_layout()
                ax[r,c].set_title(company[i], fontsize = 10, fontweight = 'bold')
                ax[r,c].set_xlabel('Cena (USD)')
                i = i + 1
    #fig.suptitle('ksdhfkh', fontsize = 12, color = 'black', fontweight = 'bold')
    plt.savefig(path + '/histograms_data_portfolia.pdf')
    """

    """
    #Access to monthly data
    df1.reset_index(inplace=True)
    #df1.columns = ['Date', 'TSLA', 'AMZN', 'AAPL', 'GOOGL', 'ADBE', 'CSCO', 'GE']
    df1.columns = ['Date', 'TSLA', 'AMZN', 'GOOGL', 'GE']
    df1['month'] = df1['Date'].dt.strftime('%b')
    #df_swap = df.swaplevel(0,1, axis = 1).sort_index(axis = 1)
    for stock in company:
        #plt.figure()
        fig, ax = plt.subplots()
        #df_stock= df_swap.xs(stock, axis = 1)
        fig_month = sns.boxplot(x='month', y=stock, data = df1, ax=ax)
        #plt.title(f'Struktura měsíčně data - {stock}', weight = 'bold')
        fig_month.set(xlabel = None)
        fig_month.set(ylabel = 'Price (USD)')
        fig_month.get_figure()
        fig.savefig(path + f'/měsíčně data - {stock}.pdf')


    """



    #plt.figure()
    #df1.plot()


    #df_MA1 = df1.rolling(window = 200).mean()
    #df_MA2 = df1.rolling(window = 50).mean()
    #fig, ax = plt.subplots()
    #df_MA1.plot(ax = ax)
    #df_MA2.plot(ax = ax)


    #print(df.info())
    """

    # Log of porcentage change
    cov_matrix =df.pct_change().apply(lambda x: np.log(1 + x)).cov()
    print(cov_matrix)

    # Correlation
    corr_matrix = df.pct_change().apply(lambda x: np.log(1 + x)).corr()
    print(corr_matrix)

    # Randomli weighted portafolio's variance
    w = {'TSLA': 0.25, 'KO': 0.25, 'AAPL': 0.25, 'CAT':0.25}
    port_var =cov_matrix.mul(w, axis = 0).mul(w, axis = 1).sum().sum()
    print(port_var)

    # Yearly returns for individual companies
    ind_er = df.resample('Y').last().pct_change().mean()
    print(ind_er)

    # Portafolio returns
    w = [0.25, 0.25, 0.25, 0.25]
    port_er = (w*ind_er).sum()
    print(port_er)

    # Volatility is given by annual standard deviation. We multiply by 250 becausae
    # there are 250 trading days/years
    ann_sd = df.pct_change().apply(lambda x: np.log(1 + x)).std().apply(lambda x: x*np.sqrt(250))
    print(ann_sd)

    # Creating a table for visualising returns and volatility of assets
    assets = pd.concat([ind_er, ann_sd], axis = 1)
    assets.columns = ['Returns', 'Volatility']
    print(assets)

    p_ret = []  # Define an empty array for portafolio returns
    p_vol = []  # Define an empty array for portafolio volatility
    p_weights = [] # Define an empty array for asset weights

    num_assets = len(df.columns)
    num_portafolios = 10000

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
        ann_sd = sd*np.sqrt(5) # Annual standard deviation = Volatility
        p_vol.append(ann_sd)

    data = {'Returns': p_ret, 'Volatility': p_vol}

    for counter, symbol in enumerate(df.columns.tolist()):
        # Print(counter, symbol)
        data[symbol+' weight'] = [w[counter] for w in p_weights]

    portafolios = pd.DataFrame(data)
    portafolios.head() # Dataframe of the 10000 portafolios created
    # print(portafolios.head())

    # Plot efficient frontier
    portafolios.plot.scatter(x = 'Volatility', y = 'Returns', marker = 'o', s = 10, alpha = 0.3, grid = True, figsize = [10, 10])
    plt.show()

    min_vol_port = portafolios.iloc[portafolios['Volatility'].idxmin()]
    # idxmin() gives us the minimum value in the column specified
    min_vol_port
    print(min_vol_port)

    # Ploting the minimum volatility portafoilo
    # plt.subplots(figsize = [10, 10])
    portafolios.plot.scatter(x = 'Volatility', y = 'Returns', marker = 'o', s = 10, alpha = 0.3, grid = True, figsize = [10, 10])
    #plt.scatter(portafolios['Volatility'], portafolios['Returns'], marker = 'o', s = 10, alpha = 0.3)
    #portafolios['Volatility'], portafolios['Returns'], marker = 'o', s = 10, alpha = 0.3)
    plt.scatter(min_vol_port[1], min_vol_port[0], color = 'r', marker = '*', s = 500)
    plt.show()

    # Finding the optimal portafolio
    rf = 0.01 # risk factor
    optimal_risky_port =portafolios.iloc[((portafolios['Returns']-rf)/portafolios['Volatility']).idxmax()]
    optimal_risky_port
    print(f' weights, {optimal_risky_port}')

    # Ploting optimal portafolio
    # plt.subplots(figsize = (10, 10))
    #plt.scatter(portafolios['Volatility'], portafolios['Returns'], marker = 'o', s = 10, alpha = 0.3)
    portafolios.plot.scatter(x = 'Volatility', y = 'Returns', marker = 'o', s = 10, alpha = 0.3, grid = True, figsize = [10, 10])
    plt.scatter(min_vol_port[1], min_vol_port[0], color = 'r', marker = 'o', s = 500)
    plt.scatter(optimal_risky_port[1], optimal_risky_port[0], color = 'g', marker = 'o', s = 100)

    vector = np.array([0.730748, 0.002006, 0.238988, 0.028257])
    vector = vector*1000000/23.49
    cena = np.array([3469.96, 55.9, 152.52, 203.06])
    units = vector/cena
    print(f'cena, {cena}')
    print(f' money, {vector}')
    print(f'units, {units}')
    """
plt.show()
