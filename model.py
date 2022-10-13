# -*- coding: utf-8 -*-
# ! /usr/bin/python
# @Time : 
# @Author :
from app import db


"""
字段类	说明
db.Integer	整型
db.String (size)	字符串，size 为最大长度，比如 db.String(20)
db.Text	长文本
db.DateTime	时间日期，Python datetime 对象
db.Float	浮点数
db.Boolean	布尔值"""


class User(db.Model):  # 表名将会是 user（自动生成，小写处理）
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(20))  # 名字


class Movie(db.Model):  # 表名将会是 movie
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(60))  # 电影标题
    year = db.Column(db.String(4))  # 电影年份
