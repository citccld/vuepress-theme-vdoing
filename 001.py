# -*-coding: utf-8 -*-
# @Time    : 2023/5/27 22:15
# @Author  : devops
# @desc    :
from jinja2 import Template

# 定义表格的标题和数据
headers = ['Name', 'Age', 'Country']
data = [
    ['John Doe', '30', 'USA'],
    ['Jane Smith', '25', 'Canada'],
    ['Tom Johnson', '35', 'UK']
]

# 读取模板文件
with open('template.html', 'r') as file:
    template_content = file.read()

# 创建模板对象
template = Template(template_content)

# 填充占位符并生成HTML
html = template.render(headers=headers, data=data)

# 将HTML代码保存到文件
with open('table.html', 'w') as file:
    file.write(html)
