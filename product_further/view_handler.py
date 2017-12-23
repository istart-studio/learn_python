# -*- coding: utf-8 -*-
import os
import webbrowser


# 打开视图
def open_view(data):
    # 读取模版
    document = open("template/info_graphic.html", "r")
    content = document.read();
    # content = "{json_data}";
    content = content.format(json_data=data)
    # 生成本地cache文件
    output_file = open('view/view.html', 'w')

    # 写入输出文件内容
    output_file.write(content)
    output_file.close()

    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    # open in a new tab, if possible
    webbrowser.open('file://' + url, new=2)
