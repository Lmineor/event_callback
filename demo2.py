#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@Time    : 2021/1/29 21:15
@Author  : lex(luohai2233@163.com)
@File    : demo2.py.py
@Software: PyCharm
"""

import time

from flask import Flask

import registry
import events

app = Flask(__name__)


def pull_the_trigger():
    registry_event()


def registry_event():
    registry.subscribe(create_database, 'database', events.CREATE)

    registry.subscribe(create_table_student, 'database', events.AFTER_CREATE)
    registry.subscribe(create_table_class, 'database', events.AFTER_CREATE)
    registry.subscribe(create_table_teacher, 'database', events.AFTER_CREATE)

    registry.subscribe(update_database, 'database', events.UPDATE)
    registry.subscribe(delete_database, 'database', events.DELETE)


def create_database(resource, event, trigger, **kwargs):
    print("*****starting create database*****")
    for i in range(3):
        time.sleep(1)
        print(".")
    print("*****create database finish*****")
    registry.notify('database', events.AFTER_CREATE, 'tigger')


def update_database(resource, event, trigger, **kwargs):
    print("This is update_network")


def delete_database(resource, event, trigger, **kwargs):
    print("This is delete_network")


def create_table_student(resource, event, trigger, **kwargs):
    print("*****starting create student table*****")
    for i in range(3):
        time.sleep(1)
        print(".")
    print("*****create database finish*****")


def create_table_class(resource, event, trigger, **kwargs):
    print("*****starting create class table*****")
    for i in range(3):
        time.sleep(1)
        print(".")
    print("*****create database finish*****")


def create_table_teacher(resource, event, trigger, **kwargs):
    print("*****starting create teacher table*****")
    for i in range(3):
        time.sleep(1)
        print(".")
    print("*****create database finish*****")


@app.route('/')
def hello_world():
    registry_event()
    return 'You pull The trigger!'


@app.route('/fire')
def fire():
    registry.notify('database', events.CREATE, 'tigger')
    return "Fire!!!"


if __name__ == '__main__':
    app.run()
