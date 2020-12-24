#!/usr/bin/env python
# -*- coding:utf-8 -*-
import yaml


def step1():
    print('\nstep1:打开浏览器')


def step2():
    print('step2:输入Python')


def step3():
    print('step3:点击搜索查看结果')


def step(path):
    with open(path) as f:
        step = yaml.safe_load(f)

    if "step1" in step:
        step1()
    if "step2" in step:
        step2()
    if "step3" in step:
        step3()


def test_foo1():
    step("./step_y.yml")
