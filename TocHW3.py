import urllib.request
import json
import sys
import re

if __name__ == '__main__':
    
    url = sys.argv[1]
    block = sys.argv[2]
    road = sys.argv[3]
    year = sys.argv[4]
    
    #fp = open('data.json', 'r')
    #data = json.loads(fp.read())
    #fp.close()
    
    #block = '楊梅市'
    #road = '金山街'
    #year = '103'
    
    month = int(year+'00')
    total_price = 0
    number_of_rec = 0
    data = json.loads(urllib.request.urlopen(url).read().decode('utf-8'))
    
    #url = "http://www.datagarage.io/api/5365dee31bc6e9d9463a0057"
    #data = json.loads(urllib.request.urlopen(url).read().decode("utf-8"))
    #data = json.loads(json_data.read().decode('utf8'))
    
    for record in data:
        if record['鄉鎮市區'] == block:
            if re.search(road, record['土地區段位置或建物區門牌']):
                if int(record['交易年月']) > month:
                    total_price += record['總價元']
                    number_of_rec += 1

    print(int(total_price / number_of_rec))

#print ("\"" + key + "\",\n")
