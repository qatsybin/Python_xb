#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest
import yaml

from pythoncode.calculator import Calculator


def get_datax():
    with open("./data.yml") as f:
        datax = yaml.safe_load(f)
        print(datax)
        # 加法
        calc_add = datax["datas_add"]
        ids_add = datax["myids_add"]
        # 减法
        calc_sub = datax["datas_sub"]
        ids_sub = datax["myids_sub"]
        # 乘法
        calc_mul = datax["datas_mul"]
        ids_mul = datax["myids_mul"]
        # 除法
        calc_div = datax["datas_div"]
        ids_div = datax["myids_div"]
        return [calc_add, ids_add, calc_sub, ids_mul, calc_mul, ids_mul, calc_div, ids_div]


class TestCalc:

    def setup_method(self):
        print("\n开始计算")

    def teardown_method(self):
        print("\n结束计算")

    def setup_class(self):
        # 实例化类,生成类的对象
        self.calc = Calculator()

    #  使用参数化
    @pytest.mark.parametrize("a,b,expect", get_datax()[0], ids=get_datax()[1])
    # 测试add函数
    def test_add(self, a, b, expect):
        # 调用add函数,返回的结果保存在result里面
        result = self.calc.add(a, b)
        # 判断result结果是否等于期望的值
        assert result == expect
        #  使用参数化

    @pytest.mark.parametrize("a,b,expect", get_datax()[2], ids=get_datax()[3])
    # 测试sub函数
    def test_sub(self, a, b, expect):
        # 调用sub函数,返回的结果保存在result里面
        result = self.calc.sub(a, b)
        # 判断result结果是否等于期望的值
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", get_datax()[4], ids=get_datax()[5])
    # 测试sub函数
    def test_mul(self, a, b, expect):
        # 调用mul函数,返回的结果保存在result里面
        result = self.calc.mul(a, b)
        # 判断result结果是否等于期望的值
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", get_datax()[6], ids=get_datax()[7])
    # 测试sub函数
    def test_div(self, a, b, expect):
        # 调用div函数,返回的结果保存在result里面
        result = self.calc.div(a, b)
        # 判断result结果是否等于期望的值
        assert result == expect