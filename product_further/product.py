# -*- coding: utf-8 -*-
from json_object import JsonObject


# 产品改进点
class Further(JsonObject):
    def __init__(self, product, further_name, further_type, further_wight, description, compete_time):
        self.product = product
        self.further_name = further_name
        self.further_type = further_type
        self.further_wight = further_wight
        self.description = description
        self.complete_time = compete_time
