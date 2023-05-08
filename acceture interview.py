# sort the list according to severety
alerts = [{"id":1, "severity":3, "message":"CPU high"}, {"id":2, "severity":1, "message":"App in crashloop"}, {"id":3, "severity":1, "message":"App in pending stage"}]

sort_severety=[]
def sort_by_severity(alert):
    for i in alert:
        print(alerts[1]["severity"])
        
        print(i)
        
print(sort_by_severity(alerts))
    # alert.

    
import json,operator
products = '''\
[{"id":1, "severity":3, "message":"CPU high"}, {"id":2, "severity":1, "message":"App in crashloop"}, {"id":3, "severity":1, "message":"App in pending stage"}]
'''
# Array of JSON Objects
# products = '''\
# [{"name": "HDD", "brand": "Samsung", "price": 100},
#             {"name": "Monitor", "brand": "Dell", "price": 120},
#             {"name": "Mouse", "brand": "Logitech", "price": 10}]
# '''
print(type(products))
data = json.loads(products)
data.sort(key=operator.itemgetter('severity'))
print(json.dumps(data, indent=2))
