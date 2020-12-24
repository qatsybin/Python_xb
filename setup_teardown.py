#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest


def setup_module():
    print('整个模块setup_teadowen,开始前执行一次')


def teardown_module():
    print('整个模块setup_teadowen，结束后执行一次')


def setup_function():
    print('\n+++执行类外的用例开始+++')


def teardown_function():
    print('\n+++执行类外的用例结束+++')


def test_three():
    print('执行testthree')


def test_four():
    print('执行testfour')


class TestClass:

    def setup_class(self):
        print('setupclass所有用例执行前')

    def teardown_class(self):
        print('teardown所有用例执行后')

    def setup_method(self):
        print('setupmethod，用例开始前执行')

    def teardown_method(self):
        print('teardown，用例结束后执行')

    def test_one(self):
        print('执行testone用例')

    def test_two(self):
        print('执行testtwo')
