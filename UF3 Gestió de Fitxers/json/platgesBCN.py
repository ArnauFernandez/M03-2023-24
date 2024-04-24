import json
f=open('opendatabcn_NP-NASIA_Platges-js.json','w',encoding='utf-8')
json.dump(f)
f=open('opendatabcn_NP-NASIA_Platges-js.json','r',encoding='utf-8')
file=json.load(f)
print(json.dumps(f, indent=0))
f.close()