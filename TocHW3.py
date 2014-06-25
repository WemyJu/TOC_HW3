# TOC HW3
# TocHW3.py
# Created by Wemy Ju on 25/06/2014.

import urllib.request
import json
import sys
import re

if __name__ == '__main__':
    
    if(len(sys.argv) < 5):
        sys.exit("Error\nusage: python3 <file_name.py> <URL> <block_name> <road_name> <year>")
    else:
        url = sys.argv[1]
        block = sys.argv[2]
        road = sys.argv[3]
        year = sys.argv[4]
    
        month = int(year+'00')
        total_price = 0
        number_of_rec = 0
        data = json.loads(urllib.request.urlopen(url).read().decode('utf-8'))
    
        for record in data:
            if record['鄉鎮市區'] == block:
                if re.search(road, record['土地區段位置或建物區門牌']):
                    if int(record['交易年月']) > month:
                        total_price += record['總價元']
                        number_of_rec += 1

        if(number_of_rec == 0):
            print("0")
        else:
            print(int(total_price / number_of_rec))
