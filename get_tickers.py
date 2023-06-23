"""
import requests
import pandas as pd
from lxml.html import parse
from urllib.request import Request, urlopen

headers = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3)" + " "
    "AppleWebKit/537.36 (KHTML, like Gecko)" + " " + "Chrome/35.0.1916.47" +
    " " + "Safari/537.36"
]

url = 'https://www.stockmonitor.com/sector/healthcare/'

headers_dict = {'User-Agent': headers[0]}
req = Request(url, headers=headers_dict)
webpage = urlopen(req)

tree = parse(webpage)


healthcare_tickers = []
for element in tree.xpath("//tbody/tr/td[@class='text-left']/a"):

    healthcare_tickers.append(element.text)

pd.Series(healthcare_tickers)

print(healthcare_tickers)

['TXG', 'YI', 'ATNF', 'ONEM', 'XXII', 'ME', 'TSVT', 'FDMT', 'LBPS', 'ETNB', 'MASS', 'NMTR', 'AADI', 'ABT', 'ABBV', 'ABCM', 'ABCL', 'ABEO', 'ABMD', 'ABSI', 'ABVC', 'ACHC', 'ACAD', 'ACST', 'AXDX', 'ACCD', 'ARAY', 'ACRX', 'ACER', 'ACHV', 'ACHL', 'ACIU', 'ACRS', 'ACOR', 'ATNM', 'ABOS', 'ACXP', 'AFIB', 'ADAG', 'ADGI', 'ADMP', 'AHCO', 'ADAP', 'ADPT', 'ADCT', 'ADXN', 'ADUS', 'ADIL', 'ACET', 'ADTX', 'ADMA', 'ADXS', 'ADVM', 'AGLE', 'AERI', 'AVTE', 'AIH', 'AEZS', 'AEMD', 'AFMD', 'AGEN', 'AGE', 'A', 'AGRX', 'AGTI', 'AGL', 'AGIO', 'AIKI', 'ALRN', 'AIM', 'AIRS', 'AKTX', 'AKBA', 'KERN', 'AKRO', 'AKUS', 'AKYA', 'AKU', 'ALBO', 'ALC', 'ALDX', 'ALEC', 'ALHC', 'ALGN', 'ALGS', 'ALIM', 'ALKS', 'ALLK', 'ALNA', 'AHPI', 'ALLO', 'ALVR', 'MDRX', 'ALNY', 'ATEC', 'TKNO', 'ALPN', 'CYTO', 'ATHE', 'ALT', 'ALXO', 'ALZN', 'AMRN', 'AMAM', 'AMED', 'AMS', 'AMWL', 'ABC', 'AMGN', 'FOLD', 'AMRX', 'AMN', 'AMPH', 'AMPE', 'AMYT', 'AMLX', 'ANAB', 'AVXL', 'ANEB', 'ANGO', 'ANGN', 'ANIK', 'ANIP', 'ANIX', 'ANNX', 'ANVS', 'ANPC', 'ATRS', 'ANTM', 'APLS', 'APEN', 'AMEH', 'APDN', 'AGTC', 'AMTI', 'APLT', 'APRE', 'APR', 'APVO', 'APTX', 'APM', 'APTO', 'APYX', 'AQST', 'ARAV', 'ABUS', 'ABIO', 'ARCT', 'RCUS', 'ARQT', 'ARDX', 'ARNA', 'ARGX', 'ARDS', 'ARMP', 'ARWR', 'TARA', 'ARTL', 'ARVN', 'ASND', 'ASXC', 'ASLN', 'AWH', 'ASMB', 'ASRT', 'IONM', 'AZN', 'ATXS', 'ATAI', 'ATRA', 'AVIR', 'ATNX', 'ATHX', 'ATHA', 'ATIP', 'ATOS', 'BCEL', 'ATRC', 'ATRI', 'LIFE', 'AUGX', 'AURA', 'AUPH', 'ACB', 'AUTL', 'AVDL', 'AVCO', 'AVTX', 'AVNS', 'AVAH', 'ATXI', 'AVEO', 'CDMO', 'RNA', 'AVGR', 'RCEL', 'AVRO', 'AXLA', 'AXGN', 'AXNX', 'AXSM', 'AYLA', 'AYTU', 'AZTA', 'AZYO', 'BBLN', 'BXRX', 'BHC', 'BAX', 'BEAM', 'BDX', 'BGNE', 'BLPH', 'BLCM', 'BLU', 'BNTC', 'BLI', 'BTTX', 'XAIR', 'BYSI', 'BCYC', 'BCAB', 'BCDA', 'BIOC', 'BCRX', 'BDSI', 'BDSX', 'BFRA', 'BFRI', 'BIIB', 'BHVN', 'BIOL', 'BLFS', 'BLRX', 'BMRN', 'BMEA', 'BMRA', 'PHGE', 'BNGO', 'BVXV', 'BNOX', 'BNTX', 'BPTH', 'BPTS', 'BIO', 'BIO.B', 'BRTX', 'BSGM', 'TECH', 'BEAT', 'BTCY', 'BVS', 'BIVI', 'BTAI', 'BDTX', 'BLUE', 'BJDX', 'BPMC', 'BOLT', 'BBLG', 'BSX', 'BCLI', 'BWAY', 'BCTX', 'BBI', 'BBIO', 'BHG', 'DRUG', 'BMY', 'BKD', 'BTX', 'BRKR', 'BNR', 'BFLY', 'CCCC', 'CABA', 'CLBS', 'CALA', 'CALT', 'CADL', 'CANF', 'CANO', 'CGC', 'CAPR', 'CARA', 'CRDF', 'CAH', 'CRDL', 'CSII', 'CDNA', 'CMAX', 'CRBU', 'CASI', 'SAVA', 'CSTL', 'CSLT', 'CTLT', 'CBIO', 'CPRX', 'YCBD', 'CELC', 'CLDX', 'CLRB', 'CLLS', 'CVM', 'CLSN', 'CELU', 'CYAD', 'CNC', 'CNTA', 'CNTG', 'IPSC', 'CERE', 'CERN', 'CERT', 'CERS', 'CSBR', 'CHNG', 'CRL', 'CHEK', 'CMPI', 'CKPT', 'CEMI', 'CHE', 'CCXI', 'CMMB', 'CMRX', 'CJJD', 'CPHI', 'SXTC', 'KDNY', 'CDXC', 'MPLN', 'CDTX', 'CI', 'CING', 'CTXR', 'CRXT', 'CLPT', 'CLSD', 'CLNN', 'CLVR', 'CLOV', 'CLVS', 'CNSP', 'COCP', 'DNAY', 'CDXS', 'CODX', 'CDAK', 'COGT', 'CGTX', 'CWBR', 'CHRS', 'COLL', 'CLGN', 'CYH', 'CMPS', 'CMPX', 'CGEN', 'CPSI', 'CNCE', 'CCM', 'CFMS', 'CNMD', 'CNTB', 'CNTX', 'CFRX', 'CNVY', 'CRBP', 'CORT', 'CRMD', 'CRTX', 'CRVS', 'CVET', 'CELZ', 'CRNX', 'CRSP', 'CRON', 'CCRN', 'CCEL', 'CRY', 'CTIC', 'CUE', 'HLTH', 'CGEM', 'CPIX', 'CVAC', 'CRIS', 'CUTR', 'CVRX', 'CVS', 'CYBN', 'CYCC', 'CYCN', 'CYTH', 'CBAY', 'CYT', 'CTKB', 'CYTK', 'CTMX', 'CTSO', 'DHR', 'DARE', 'DRIO', 'DVA', 'DXR', 'DAWN', 'DBVT', 'DBTX', 'DCPH', 'DH', 'DCTH', 'DNLI', 'XRAY', 'DRMA', 'DMTK', 'DSGN', 'DXCM', 'DMAC', 'DICE', 'DFFN', 'DCGO', 'DOCS', 'RDY', 'DRRX', 'DYAI', 'DYNT', 'DVAX', 'DYN', 'EGRX', 'EAR', 'EDAP', 'EDSA', 'EWTX', 'EDIT', 'EW', 'EFTR', 'EIGR', 'EKSO', 'ELAN', 'ECOR', 'ELMD', 'ELDN', 'ELEV', 'ELYM', 'LLY', 'ELOX', 'EBS', 'ENTA', 'EHC', 'ENDP', 'NDRA', 'ENLV', 'ENOB', 'ENSC', 'ETTX', 'ENTX', 'TRDA', 'ENVB', 'NVST', 'NVNO', 'ENZ', 'EPZM', 'EQRX', 'EQ', 'ERAS', 'ERYP', 'ESPR', 'EPIX', 'ESTA', 'ETON', 'EVAX', 'EVLO', 'EVFM', 'EVGN', 'EVOK', 'EVH', 'EOLS', 'EVO', 'EXAS', 'XGN', 'EXEL', 'XCUR', 'EXAI', 'EYEN', 'EYPT', 'FATE', 'FEMY', 'FENC', 'FGEN', 'FTRP', 'FNCH', 'FWBI', 'FVE', 'FLGC', 'FLDM', 'FHTX', 'FONR', 'FORA', 'FMTX', 'FBRX', 'FBIO', 'FWP', 'FRLN', 'FREQ', 'FMS', 'HUGE', 'FSTX', 'FULC', 'FLGT', 'FUSN', 'GTHX', 'GANX', 'GLPG', 'GALT', 'GLTO', 'GRTX', 'GLMD', 'GMDA', 'GBS', 'GMTX', 'GBIO', 'GENE', 'GTH', 'GNFT', 'GMAB', 'GNCA', 'GNPX', 'GOVX', 'GERN', 'GHRS', 'GILD', 'DNA', 'GKOS', 'GSK', 'GBT', 'CO', 'GMED', 'GLYC', 'GMVD', 'GDRX', 'GOSS', 'GRCL', 'GRPH', 'GRAY', 'GEG', 'GBNH', 'GLSI', 'GRFS', 'GRTS', 'GRVI', 'GTBP', 'GH', 'GHSI', 'HAE', 'HALO', 'HNGR', 'HRMY', 'HARP', 'HROW', 'HBIO', 'HCA', 'HCWB', 'HCSG', 'HCTI', 'HCAT', 'HQY', 'HSTM', 'HTBX', 'HSDT', 'HSIC', 'HEPA', 'HRTX', 'HSKA', 'HEXO', 'HITI', 'HSTO', 'HOLX', 'FIXX', 'HOOK', 'HZNP', 'HOTH', 'HTGM', 'HUMA', 'HUM', 'HGEN', 'HCM', 'IBIO', 'ICAD', 'ICCM', 'ICLR', 'ICVX', 'ICUI', 'IDYA', 'IDRA', 'IDXX', 'IGMS', 'IKNA', 'ILMN', 'IMAB', 'IMAC', 'IMGO', 'IMRA', 'IMCC', 'IMTX', 'IMMX', 'ICCC', 'IMRX', 'IMUX', 'IBRX', 'IMCR', 'IMGN', 'IMNM', 'IPA', 'IMVT', 'IMRN', 'IMMP', 'IMPL', 'IMV', 'INAB', 'NARI', 'INCY', 'INDP', 'INFI', 'IFRX', 'INFU', 'IKT', 'INBX', 'INM', 'INMD', 'INMB', 'IPHA', 'INNV', 'INVA', 'INGN', 'NOTV', 'INO', 'INZY', 'INSM', 'IINN', 'NSPR', 'INSP', 'TIL', 'PODD', 'ITGR', 'IART', 'IGAP', 'NTLA', 'ICPT', 'INCR', 'IDXG', 'XENT', 'ITCI', 'IIN', 'ISRG', 'IVC', 'IVA', 'NVTA', 'NVIV', 'INVO', 'IOBT', 'IONS', 'IOVA', 'IQV', 'IRMD', 'IRTC', 'IRIX', 'IRWD', 'ISO', 'ISR', 'ISPC', 'ITOS', 'ITRM', 'ISEE', 'JAGX', 'JANX', 'JSPR', 'JAZZ', 'JNJ', 'JNCE', 'JUPW', 'KALA', 'KLDO', 'KALV', 'KMDA', 'KRTX', 'KPTI', 'KZIA', 'KMPH', 'KROS', 'KZR', 'KNSA', 'KNTE', 'KTRA', 'KPRX', 'KRBP', 'KOD', 'PHG', 'KRON', 'KRYS', 'KURA', 'KYMR', 'LH', 'LJPC', 'LABP', 'LCI', 'LTRN', 'LNTH', 'LRMR', 'LVTX', 'LPTX', 'LEGN', 'LMAT', 'LNSR', 'LEXX', 'LXRX', 'LHCG', 'LIAN', 'LFMD', 'LFST', 'LGND', 'LMNL', 'LCTX', 'LPCN', 'LQDA', 'LIVN', 'LIXT', 'LOGC', 'LBPH', 'LGVN', 'LUCD', 'LHDX', 'LMDX', 'LUMO', 'LYEL', 'LYRA', 'MGNX', 'MDGL', 'MGTA', 'MYNZ', 'MNKD', 'MRVI', 'MRNS', 'MRKR', 'MRAI', 'MASI', 'MTNB', 'MXCT', 'MCK', 'MDVL', 'MDNA', 'MNOV', 'MDGS', 'MDWD', 'MD', 'MEDP', 'MDT', 'MEIP', 'MGTX', 'MRK', 'MREO', 'VIVO', 'MMSI', 'MACK', 'MRSN', 'MRUS', 'MESO', 'MTCR', 'MTD', 'MBOT', 'MICR', 'MTP', 'MIST', 'MLSS', 'MDXG', 'MNMD', 'NERV', 'UTRS', 'INKT', 'MRTX', 'MIRO', 'MIRM', 'MRNA', 'MODV', 'MOLN', 'MTEM', 'MBRX', 'MOH', 'MNPR', 'GLUE', 'MORF', 'MOR', 'MOTS', 'MOVE', 'MTBC', 'MBIO', 'MYMD', 'MYO', 'MYOV', 'MYGN', 'NBRV', 'NBTX', 'NSTG', 'NAOV', 'NNVC', 'NNOX', 'NH', 'NTRA', 'NHC', 'NRC', 'NTUS', 'NAUT', 'NAVB', 'NKTR', 'NMRD', 'NEOG', 'NEO', 'NLTX', 'NVCN', 'NEPH', 'NEPT', 'NBSE', 'NRBO', 'NBIX', 'NURO', 'STIM', 'NMTC', 'NPCE', 'NRSN', 'NVRO', 'NFH', 'NXGL', 'NEXI', 'NXTC', 'NXGN', 'BIMI', 'NGM', 'NKTX', 'NLSP', 'NBY', 'NOVN', 'NVS', 'NVAX', 'NVCR', 'NVOS', 'NVO', 'NRXP', 'NCNA', 'NRIX', 'NTRB', 'NUVL', 'NUVA', 'NUVB', 'NUWE', 'NYMX', 'NYXH', 'OSH', 'OBSV', 'OCGN', 'OCUL', 'OCUP', 'ODT', 'OLMA', 'OLK', 'OMGA', 'OMER', 'OMCL', 'OCX', 'TOI', 'ONCY', 'ONTX', 'ONCR', 'ONCS', 'ONCT', 'OTRK', 'OPGN', 'OPNT', 'OPK', 'OPT', 'OPRX', 'OPTN', 'OPCH', 'OGEN', 'ORMP', 'OSUR', 'ORTX', 'OGI', 'ORGO', 'OGN', 'ONVO', 'ORGS', 'ORIC', 'ORPH', 'OCDX', 'OFIX', 'KIDS', 'OSCR', 'OSMT', 'OTIC', 'OTLK', 'OM', 'OVID', 'OMI', 'OWLT', 'OYST', 'PIII', 'PACB', 'PCRX', 'PRFX', 'PTN', 'PALI', 'PBLA', 'FNA', 'PRTK', 'KTTA', 'PASG', 'PDCO', 'PAVM', 'PDSB', 'PEAR', 'PEN', 'PKI', 'PRGO', 'PSNL', 'PETQ', 'PETS', 'PTPI', 'PETV', 'PFE', 'PMCB', 'PHVS', 'PHAS', 'PHAT', 'PAHC', 'PHIO', 'PHR', 'PIRS', 'PLRX', 'PSTI', 'PSTV', 'PLXP', 'PMVP', 'PNT', 'PTE', 'PYPD', 'PRTG', 'PSTX', 'PRAX', 'PGEN', 'PRPO', 'DTIL', 'POAI', 'PRLD', 'PINC', 'PBH', 'PRVA', 'PROC', 'PRCT', 'PCSA', 'PDEX', 'PROF', 'PROG', 'PGNY', 'RXDX', 'PRPH', 'PRQR', 'PTIX', 'PTGX', 'PLX', 'PRTA', 'PRVB', 'PMD', 'PTCT', 'PULM', 'LUNG', 'PLSE', 'PBYI', 'PRTC', 'PPBT', 'PYXS', 'QGEN', 'QLI', 'QLGN', 'QTRX', 'QSI', 'DGX', 'QDEL', 'QIPT', 'QNRX', 'QTNT', 'RCM', 'RDUS', 'RDNT', 'RFL', 'RAIN', 'RLYB', 'RMED', 'RANI', 'RPID', 'RAPT', 'RETA', 'REPH', 'RXRX', 'RDHL', 'RGC', 'REGN', 'RGNX', 'RHE', 'RGLS', 'RLAY', 'RLMD', 'RNLX', 'RPHM', 'RCOR', 'RNXT', 'RPTX', 'RGEN', 'REPL', 'KRMD', 'RSLS', 'RMD', 'RVP', 'RVNC', 'RVPH', 'RVMD', 'RWLK', 'RZLT', 'RYTM', 'RIGL', 'RAD', 'RCKT', 'RMTI', 'ROIV', 'RPRX', 'RUBY', 'RXST', 'SABS', 'SAGE', 'SLRX', 'SANA', 'SMTI', 'SGMO', 'SNY', 'SRPT', 'STSA', 'SVRA', 'SRRK', 'SDGR', 'SNCE', 'SCPS', 'SCPH', 'WORX', 'SCYX', 'SPNE', 'SGEN', 'EYES', 'SEEL', 'SEER', 'SELB', 'SEM', 'SLS', 'SMFR', 'SMLR', 'SNSE', 'SENS', 'SRTS', 'SQL', 'SERA', 'MCRB', 'SESN', 'SHCR', 'STTK', 'SISI', 'SWAV', 'SIBN', 'SIEN', 'SRRA', 'SIGA', 'SGHT', 'SGTX', 'SGFY', 'SLN', 'SILK', 'SBTX', 'SLP', 'OMIC', 'SVA', 'SINT', 'SIOX', 'SLHG', 'SDC', 'SNN', 'TLMD', 'SLNO', 'SLGL', 'SLDB', 'SNGX', 'SLGC', 'SONX', 'SNDA', 'SONN', 'SNOA', 'SOPH', 'SPHS', 'SRNE', 'SHC', 'SY', 'SPPI', 'SPRO', 'SPOK', 'SWTX', 'SPRB', 'SQZ', 'STAA', 'STRR', 'STAB', 'MITO', 'STXS', 'STE', 'STVN', 'STOK', 'SSKN', 'STRM', 'SYK', 'SMMT', 'SNDL', 'SSY', 'SUPN', 'SURF', 'SRGA', 'SGRY', 'SRDX', 'SRZN', 'STRO', 'SNPX', 'SNDX', 'SYNH', 'SYBX', 'SYN', 'SYRS', 'TTOO', 'TRHC', 'TCMD', 'TAK', 'TALS', 'TLIS', 'TALK', 'TNDM', 'TNGX', 'TARO', 'TARS', 'TSHA', 'TCRR', 'TELA', 'TDOC', 'TFX', 'TPST', 'TENX', 'TNYA', 'THC', 'TERN', 'TEVA', 'TFFP', 'TGTX', 'COO', 'ENSG', 'JYNT', 'TXMD', 'THTX', 'TBPH', 'TMO', 'THMO', 'THRX', 'TLRY', 'TMBR', 'TMDI', 'TTNP', 'TVTY', 'TLSA', 'TNXP', 'TCON', 'RNAZ', 'TMDX', 'TVTX', 'TMCI', 'TRVN', 'TRVI', 'TCDA', 'TRIB', 'GTS', 'MEDS', 'TCRX', 'TPTX', 'TWST', 'TYME', 'TYRA', 'UFPT', 'RARE', 'UNCY', 'QURE', 'UNH', 'UTHR', 'UBX', 'UHS', 'UPC', 'UPH', 'URGN', 'USPH', 'UTMD', 'VCNX', 'VACC', 'VLNS', 'VLON', 'VALN', 'VNDA', 'VAPO', 'VREX', 'VBLT', 'VXRT', 'PCVX', 'VAXX', 'VBIV', 'VECT', 'VEEV', 'VTYX', 'VERO', 'VCYT', 'VSTM', 'VERA', 'VCEL', 'VRNA', 'VRCA', 'VRTX', 'VERU', 'VERV', 'VTRS', 'RBOT', 'VMD', 'VRAY', 'VKTX', 'VINC', 'VIRX', 'VIR', 'VRDN', 'VIRI', 'VRPX', 'VTGN', 'VIVE', 'VVOS', 'VNRX', 'VOR', 'VYGR', 'VTVT', 'VYNT', 'VYNE', 'WBA', 'WRBY', 'WAT', 'WVE', 'HOWL', 'WST', 'WINT', 'XFOR', 'XBIT', 'XNCR', 'XBIO', 'XENE', 'XERS', 'XLO', 'XOMA', 'XRTX', 'XTNT', 'XTLB', 'YMAB', 'YMTX', 'ZLAB', 'ZEAL', 'ZNTL', 'ZCMD', 'ZBH', 'ZIOP', 'ZIVO', 'ZTS', 'ZGNX', 'ZOM', 'ZSAN', 'ZYME', 'ZYNE', 'ZYXI', 'PNTG']
"""
#=========================other task=============================

#"""
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as pdr
import yfinance as yf


start_date = '2015/01/01'
end_date = '2021/11/07'

""" ================START DATA TEST==============
Financial_services = ['PYPL','JPM','TGT']
Consumer_defensive = ['PG','PYPL','TGT']

Technology = ['JPM']

Consumer_cyclical = ['JPM']

Healthcare = ['JPM']

Comunication_services = ['JPM']

Industrials = ['JPM']
"""
# ================FINISH DATA TEST==============
#"""
Financial_services = ['JPM', 'PYPL', 'AXP', 'BRK-B', 'PNC', 'COF',	'MMC',\
'FRC', 'TROW', 'MTB', 'WTW', 'CB', 'NDAQ', 'AON', 'CME', 'TRV',	'AJG', 'AMP',\
'LPLA',	'AIZ',	'RE','RNR','KNSL','MORN','AMG','PRI','PIPR', 'ERIE','VRTS',\
'CRVL',	'ANAT',	'ESGR',	'WRLD',	'DHIL',	'NWLI',	'HVRRF','FBAK',	'ITIC',	'DBOEF',\
'NACB',	'ALIZF', 'CNND', 'SVCTF','HALFF','MURGF','KLIB', 'EXSR']#'V'

Consumer_defensive = ['PG','TGT','PEP',	'DG','EL','CLX','STZ','HSY','CASY',	\
'HELE',	'DEO','SAFM','LANC','JJSF',	'DIT','PDRDF','CABJF','STZ-B','REMYF']

Technology = ['AAPL',	'MSFT',	'NVDA',	'AMAT',	'QCOM',	'CRM',	'TXN',	'ZM',\
	'CRWD',	'COIN',	'TEAM',	'SNOW',	'ADI',	'TEL',	'BILL',	'WDAY',	'ZS',	\
    'ADSK',	'NXPI',	'OKTA',	'XLNX',	'CDNS',	'TER',	'FTNT',	'SWKS',	'RNG',	\
    'KEYS',	'PAYC',	'MSI',	'SEDG',	'CDW',	'SNPS',	'BR',	'ANSS',	\
    'AZPN',	'JKHY',	'FLT',	'IT',	'MNDY',	'CNXC',	'OLED',	'WEX',	\
    'CCMP',	'MKSI',	'NICE',	'COHR',	'GLOB',	'PCTY',	'SYNA',	'IPGP',	'SITM',	\
    'FFIV',	'SLAB',	'ROG',	'UI',	'NOVT',	'LFUS',	'CACI',	'MLAB',	'SOTGY',\
    'IIVIP', 'CAPMF','TYOYY','NGRRF','FJTSF','SLOIF', 'ESKEF','NCSYF','LSRCF']#'VRSN','AMBA'

Consumer_cyclical = ['CVNA',	'ABNB',	'MCD',	'LOW',	'ETSY',	'APTV',	'MAR',\
	'LULU',	'W',	'EXPE',	'BURL',	'WHR',	'TSCO',	'FIVE',	'MTN',	'MHK',	\
    'LAD',	'WING',	'AAP',	'VAC',	'DECK',	'RACE',	'MUSA',	'LEA',	'TM',	\
    'ABG',	'DDS',	'CHH',	'GPI',	'LVMUY',	'CHDN',	'MED',	'HESAY',	\
    'CVCO',	'WINA',	'SZKMY',	'LNNGY',	'APTV-PA',	'PDYPF',	'VLKPF',\
    	'MGDDF',	'ADDDF',	'VLKAF',	'HDUGF',	'OLCLF',	'CHDRY',\
        	'SHMDF']

Healthcare = ['MRNA',	'JNJ',	'DHR',	'AMGN',	'LLY',	'BNTX',	'ISRG',	'ZTS',\
	'VRTX',	'BIIB',	'SYK',	'BDX',	'PKI',	'VEEV',	'CI',	'IQV',	'HCA',	\
    'PODD',	'LH',	'RGEN',	'ICLR',	'MCK',	'SWAV',	'RMD',	'STE',	'INSP',	\
    'MASI',	'TFX',	'ABMD',	'UTHR',	'MEDP',	'PEN',	'WAT',	'OMCL',	'MOH',	\
    'BGNE',	'ICUI',	'ARGX',	'HSKA',	'GNNDY',	'CZMWY',	'ZRSEF',	\
    'GNMSF',	'ESLOF',	'DSRLF',	'CZMWF',	'CMXHF',	'MKGAF',	\
    'CLPBF']

Comunication_services = ['FB',	'DIS',	'SE',	'ROKU',	'TTWO',	'TWLO',	'BIDU',\
	'SPOT',	'NXST',	'LBRDK',	'MSGS',	'NAPRF']

Industrials = ['BA',	'CAT',	'HON',	'ETN',	'UNP',	'TT',	'MMM',	'WM',\
	'GPN',	'UPS',	'LHX',	'ADP',	'ODFL',	'VRSK',	'FDX',	'NSC',	'GD',\
    	'ITW',	'GNRC',	'JBHT',	'CMI',	'SWK',	'PH',	'EFX',	'DOV',	\
        'MIDD',	'ROK',	'HEI',	'URI',	'CAR',	'HUBB',	'IEX',	'SNA',	\
        'AVY',	'SAIA',	'BLD',	'RRX',	'HII',	'LSTR',	'HRI',	'SITE',	\
        'LII',	'AYI',	'CFXA',	'CSL',	'ALGT',	'WSO',	'NDSN',	'WTS',	\
        'FCN',	'ROLL',	'VMI',	'UNF',	'KAI',	'ASR',	'FERG',	'ALG',	\
        'ESLT',	'SBGSF',	'TLPFY',	'ASHTY',	'DSDVF',	'UZAPF',	\
        'HPGLY',	'ANNSF',	'FANUF',	'WSO-B',	'DKILF',	'EENEY',	\
        'SMAWF',	'HLAGF',	'SCPJ',	'SPXSF',	'SHLAF',	'ACXIF',	\
        'KRDXF',	'MTUAF',	'PUODY']

#"""

sectors = [Financial_services, Consumer_defensive, Technology, \
Consumer_cyclical, Healthcare, Comunication_services, Industrials]


for sector in sectors:
    df1 = pdr.get_data_yahoo(sector, start = start_date, end = end_date)
    #print(df1.head())
    dfZ = pd.DataFrame()
    #dfZ = []
    summary = pd.DataFrame()
    for company in sector:
        #company = Healthy_sector[i]
        try:
            df = yf.Ticker(company)
            dfb = df.balance_sheet.iloc[:,0]
            dff = df.financials.iloc[:,0]

            current_assets = dfb.T['Total Current Assets']
            #print(f'Current assets = {current_assets}')
            current_liabilities = dfb.T['Total Current Liabilities']
            #print(f'Current liabilities = {current_liabilities}')
            working_capital = current_assets-current_liabilities
            #print(f'Working capital = {working_capital}')

            #working_capital.plot()
            total_assets = dfb.T['Total Assets']
            #print(f'Total assets = {total_assets}')
            X_1 = working_capital/total_assets
            #print(f'X_1 = {X_1}')
            #X_1.plot()
            try:
                retained_earnings = dfb.T['Retained Earnings']
                #print(f'Retained earnings = {retained_earnings}')
            except:
                retained_earnings = dfb.T['Earnings Surplus']
            X_2 = retained_earnings/total_assets
            #print(f'X_2 = {X_2}')
            #X_2.plot()

            EBIT = dff.T['Ebit']
            #print(f'EBIT = {EBIT}')
            X_3 = EBIT/total_assets
            #print(f'X_3 = {X_3}')

            market_value_equity=df.info['marketCap']
            #print(f'Market value equity = {market_value_equity}')

            try:
                book_value_of_total_debt = dfb.T['Total Liab']
                #print(f'Book value of total debt = {book_value_of_total_debt}')
                X_4 = market_value_equity/book_value_of_total_debt
            except:
                X_4 = 0

            #print(f'X_4 = {X_4}')
            #X_4.plot()

            sales = dff.T['Total Revenue']
            #print(f'Sales = {sales}')

            X_5 = sales/total_assets
            #print(f'X_5 = {X_5}')
            #X_5.plot()

            Z = 1.2*X_1 + 1.4*X_2 + 3.3*X_3 + 0.6*X_4 + 1.0*X_5
            #Z = 0.012*X_1 + 0.014*X_2 + 0.033*X_3 + 0.006*X_4 + 0.999*X_5

            #index = ['Current assets', 'Current liabilities', 'Working capital',\
            #'Total assets', 'X_1', 'Retained earnings', 'X_2', 'EBIT', 'X_3', \
            #'Market value equity', 'Book value of total debt', 'X_4', 'Sales',\
            #'X_5', 'Z']

            #values = [f'{current_assets}', f'{current_liabilities}', f'{working_capital}',\
            #f'{total_assets}', f'{X_1}', f'{retained_earnings}', f'{X_2}', f'{EBIT}', f'{X_3}', \
            #f'{market_value_equity}', f'{book_value_of_total_debt}', f'{X_4}', f'{sales}'\
            #f'{X_5}', f'{Z}']

            values ={'Current assets':[current_assets], 'Current liabilities': [current_liabilities], 'Working capital':[working_capital],\
            'Total assets':[total_assets], 'X_1':[X_1], 'Retained earnings':[retained_earnings], 'X_2':[X_2], 'EBIT':[EBIT], 'X_3':[X_3], \
            'Market value equity':[market_value_equity], 'Book value of total debt':[book_value_of_total_debt], 'X_4':[X_4], 'Sales':[sales],\
            'X_5':[X_5], 'Z':[Z]}

            #values = [[current_assets], [current_liabilities], [working_capital],\
            #[total_assets], [X_1], [retained_earnings], [X_2], [EBIT], [X_3], \
            #[market_value_equity], [book_value_of_total_debt], [X_4], [sales]\
            #[X_5], [Z]]

            recap = pd.DataFrame(values, index = [company])
            #summary.columns = [company]
            summary = pd.concat([summary, recap])
            print(summary.T)
            #sector_name = [Financial_services, Consumer_defensive, Technology, \
            #Consumer_cyclical, Healthcare, Comunication_services, Industrials]
            Z = pd.Series(Z, index = [company])
            #i = i+1
            #print(Z.info)
            #dfZ = np.append(dfZ,Z)
            #Z = pd.DataFrame({[company], Z})

            #print(f'Z = {Z}')

            dfZ = pd.concat([dfZ, Z.to_frame()])
            #dfZ = dfZ.append(Z)
        except:
            pass
        # we van vreate a loop for nanes here: CCC =[1 2 3 ], then i = CCC[0] one vector with names
    #print(f'dfZ_{sector}')


    print(f'Summary of Z Score values')
    print(dfZ)
    #dfZ.plot.barh(legend = False)

    #print(dfZ.info())
    dfZ = dfZ.sort_values(by = [0])
    #print(dfZ)
    dfZD = dfZ.sort_values(by = [0], ascending = False)

    data_summary = pd.merge(dfZD[0:4], summary, left_index = True, right_index = True)
    data_summary.drop(data_summary.columns[[0]], axis = 1, inplace = True)
    print('Summary of the 4 best stocks, according Z Score')
    print(data_summary.T)
    #print(summary[dfZD[0:4].T.columns])
    dfZ.plot.barh(legend = False)
    plt.xlabel('Z Score')
    #dfZ.sort_values([0], ascending = False).plot.barh(legend = False)

    #try:
    #    dfZ.sort_values(dfZ[0], ascending = False).plot.barh(legend = False)
    #except:
    #    dfZ.plot.barh(legend = False)
plt.show()
