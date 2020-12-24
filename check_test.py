#!/usr/bin/env python
# -*- coding:utf-8 -*-
def inc(x):
    return x + 1


def check_answer():
    print('这是我的第1条测试用例')
    assert inc(3) == 4


def test_answer1():
    print('这是我的第2条测试用例')
    assert inc(3) == 4