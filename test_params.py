#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest


def add_function(a, b):
    return a + b


# ids格式ids=[" "," "," "]
@pytest.mark.parametrize("a,b,exp", [(23, 45, 68), (-1, -2, -3), (1000, 2000, 3000)], ids=["int", "minus", "bigint"])
def test_add(a, b, exp):
    assert a + b == exp
