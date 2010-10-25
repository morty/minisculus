#!/usr/bin/env python

from mark1 import MarkI

class MarkIV(object):
    def __init__(self):
        self.setting = 0

    def get_setting(self):
        return self.setting

    def increment_setting(self, increment_value):
        self.setting += increment_value
