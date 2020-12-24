#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest


def add_function(a, b):
    return a + b


@pytest.mark.parametrize("a", [0, 3])
@pytest.mark.parametrize("b", [2, 4])
def test_foo(a, b):
    print("测试参数堆叠组合：a->%s,b->%s" % (a, b))
