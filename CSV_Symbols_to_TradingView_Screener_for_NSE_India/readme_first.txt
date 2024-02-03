1. This code converts symbols in this format:

EIHOTEL
L&TFH
GSPL
HINDOILEXP

to this

NSE:EIHOTEL,NSE:GSPL,NSE:HINDOILEXP,NSE:L_TFH

or in this format

EIHOTEL, L&TFH, GSPL, HINDOILEXP

to this

NSE:EIHOTEL,NSE:GSPL,NSE:HINDOILEXP,NSE:L_TFH

2. It removes duplicates, replace "&" and "-" to "_", and sort alphabetically to a set of 40 in each line.

3. Also it removes any symbols which are present in the "Additional Surveillance Measure" list from "https://www.nseindia.com/reports/asm"

4. Default inputs are made for NSE listed symbols. This can be modified.

5. You can just copy and paste the symbols to the TradingView screener.

6. If you change the filenames "step_1_paste_csv_symbols.txt" and "step_3_symbols_for_tradingview_screener.txt" you need to change the same in the .py file also.

END