import json

f1 = open('sublist.txt')
idList = []
for i in f1.readlines():
    idList.append(i.rstrip('\n'))
f1.close()

f2 = open('channel.txt', encoding='utf-8')
nameList = []
for i in f2.readlines():
    nameList.append(i.rstrip('\n'))
f2.close()

jsonOutList = []
for i in range(0, len(idList)):
    jsonOutList.append({'snippet' : {'channelTitle' : nameList[i], 'resourceId' : {'channelId' : idList[i]}}})

with open('output.json', 'w', encoding='utf-8') as output:
    json.dump(jsonOutList, output, ensure_ascii=False, indent=2)
