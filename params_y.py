#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest
import yaml


def get_data():
    with open("./data_y.yml") as f:
        datas = yaml.safe_load(f)
        myids = yaml.safe_load(f)
        print(datas)
        add_datas = datas["datas"]
        add_ids = datas["myids"]
        return [add_datas, add_ids]


def add_function(a, b):
    return a + b


@pytest.mark.parametrize("a,b,exp", get_data()[0], ids=get_data()[1])
def test_add(a, b, exp):
    assert a + b == exp
