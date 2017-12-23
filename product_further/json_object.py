# -*- coding: utf-8 -*-
import json


# json对象，继承后方便json序列化及反序列化
class JsonObject(object):

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)