#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author:Linany
from flask import Flask

# 引入蓝图
from apps.web_recorder_page import web_recorder

# Flask 核心对象
app = Flask(__name__)

# 蓝图绑定
app.register_blueprint(web_recorder)

# 服务启动
if __name__ == '__main__':
    app.run("127.0.0.1", 233, debug=True)
