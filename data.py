import urllib
import os
import shutil
import datautil
import datautil.tabular
from datautil.tabular.xls import XlsReader

cache = datautil.Cache('cache')

def market_quote_report():
    url = 'https://uk.zopa.com/ZopaWeb/ashx/MarketQuoteReport.ashx'
    fp = cache.retrieve(url)
    shutil.copy(fp, 'data/market_quote_report.csv')

class RiskInfo:

    def retrieve(self):
        url = 'https://uk.zopa.com/ZopaWeb/public/downloads/risk_info_to_lenders.zip'
        # it changes monthly so overwrite
        fp = cache.retrieve(url,
                #overwrite=True
                )
        import zipfile
        zf = zipfile.ZipFile(fp)
        # only one file in there (xls)
        fn = zf.namelist()[0]
        fileobj = zf.open(fn)
        outfn = fn.lower().replace(' ', '_')
        dest = os.path.join('data', outfn)
        outfileobj = open(dest, 'w')
        outfileobj.write(fileobj.read())

    def clean_from_excel(self):
        reader = XlsReader()
        # unfortunately the following fails
        # File ".../lib/python2.6/site-packages/xlrd/compdoc.py",
        # line 70, in _build_family_tree
        # _build_family_tree(dirlist, parent_DID, dirlist[child_DID].left_DID)
        # IndexError: list index out of range
        #
        # tabdata = reader.read(open(dest), sheet_index=1)
        out = datautil.tabular.TabularData()
        out.headers = [
            'period',
            'market',
            'lifetime_bad_debt_rate',
            'total_value_of_loans',
            'defaults_and_arrears',
            'defaults'
            ]
        for inrow in tabdata.data[12:47]:
            if not inrow[0]:
                continue
            outrow = ['All Time', inrow[0], inrow[1]] + inrow[3:5]
            out.data.append(outrow)
        writer = datautil.tabular.csv.CsvWriter()
        outfo = open(os.path.join('data', 'risk_info.csv'))
        writer.write(out, outfo)

market_quote_report()
risk_info = RiskInfo()
risk_info.retrieve()
# risk_info.clean()

