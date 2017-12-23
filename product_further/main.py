# -*- coding: utf-8 -*-
import json
import store
import view_handler

objectList = store.FurthersStore().list_furthers();

# 集合json字符串
json_string = json.dumps([ob.__dict__ for ob in objectList], ensure_ascii=False)
print("json_data :" + json_string)

# 循环打印
# for further in objectList:
#    print(further.to_json())

# 打开界面
view_handler.open_view(json_string);
