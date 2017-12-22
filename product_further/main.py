# -*- coding: utf-8 -*-
import store
import json


objectList = store.FurthersStore().list_furthers();

# 集合json字符串
json_string = json.dumps([ob.__dict__ for ob in objectList])
print(json_string)

for further in objectList:
    print(further.to_json())

