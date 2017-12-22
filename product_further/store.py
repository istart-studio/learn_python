# -*- coding: utf-8 -*-
import product


# 读取数据
def read():
    document = open("furthers.data", "r")
    data = document.readlines()
    return data


class FurthersStore:

    def __init__(self):
        pass

    def list_furthers(self):
        data_collection = read()
        object_list = []
        for data in data_collection:
            data = data.strip()
            print("data:" + data)
            # 不能为空字符
            if data:
                columns = data.split(',')
                print(columns)
                object_list.append(product.Further(columns[0], columns[1], columns[2], columns[3], columns[4]))

        return object_list
