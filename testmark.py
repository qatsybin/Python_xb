#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest


class TestDemo:

    @pytest.mark.smoke
    def test_one(self):
        assert 1 == 2

    @pytest.mark.demo
    def test_two(self):
        assert 1 == 1
