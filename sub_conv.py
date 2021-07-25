# -*- coding: utf-8 -*-

import json
import csv

file = 'sub.csv'
with open(file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    channelId, channelName = [], []
    for row in reader:
        channelId.append(row[reader.fieldnames[0]])
        channelName.append(row[reader.fieldnames[2]])

jsonOutList = []
for i in range(0, len(channelId)):
    jsonOutList.append(
        {'snippet': {'channelTitle': channelName[i],
                     'resourceId': {'channelId': channelId[i]}}})

with open('output.json', 'w', encoding='utf-8') as output:
    json.dump(jsonOutList, output, ensure_ascii=False, indent=2)

print('Converted %d subscription list to output.json' % len(channelId))
