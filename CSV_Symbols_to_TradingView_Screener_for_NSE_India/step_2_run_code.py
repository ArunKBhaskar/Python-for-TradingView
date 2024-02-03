import requests
import pandas as pd

class NSE:
    
    surveillance_categories = ['longterm', 'shortterm']
    
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome''/90.0.4430.212 Safari/537.36'
        }
        self.session = requests.Session()
        self.session.get("http://nseindia.com", headers=self.headers)
    
    def additional_surveillance_measure(self, categories):
        url = "https://www.nseindia.com/api/reportASM"
        data = self.session.get(url=url, headers=self.headers).json()
        surveillance_symbols = set()
        for category in categories:
            category_data = data.get(category, {}).get("data", [])
            surveillance_symbols.update(row['symbol'] for row in category_data)
        return surveillance_symbols

# Usage
nse = NSE()
surveillance_symbols = nse.additional_surveillance_measure(NSE.surveillance_categories)

# Define a function to process a line
def process_line(line, surveillance_symbols):
    line = line.strip().replace('-', '_').replace('&', '_')
    parts = [part.strip() for part in line.split(',')]
    filtered_parts = [f"NSE:{part}" for part in parts if part not in surveillance_symbols]
    return ','.join(filtered_parts)

# Open both the source file and the new file
with open("step_1_paste_csv_symbols.txt", "r") as source_file, open("step_3_symbols_for_tradingview_screener.txt", "w") as new_file:
    batch_size = 40
    processed_lines = set()
    for line in source_file:
        processed_line = process_line(line, surveillance_symbols)
        if processed_line:
            processed_lines.add(processed_line)
        if len(processed_lines) >= batch_size:
            new_file.write(','.join(sorted(processed_lines)) + '\n')
            processed_lines.clear()
    if processed_lines:
        new_file.write(','.join(sorted(processed_lines)) + '\n')