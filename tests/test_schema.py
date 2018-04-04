# -*- coding: utf-8 -*-
"""The unit testing module for :obj:`Schema` querieng methods.

"""
import sys, os
sys.path.insert(0, os.path.abspath('../'))

from unittest import TestCase
from omdata.design import inspect

test_schema_file = "docs/omsurvey.schema"
params = ['fields-top', 'fields-all', 'fields-required', 'questions']

class TestConsole(TestCase):

    def test_getting_top_fields(self):
        args = ['inspect', params[0], '-s', test_schema_file]
        inspect(args)
    def test_getting_all_fields(self):
        args = ['inspect', params[1], '-s', test_schema_file]
        inspect(args)
    def test_getting_required_fields(self):
        args = ['inspect', params[2], '-s', test_schema_file]
        inspect(args)

    def test_getting_survey_question_nos(self):
        args = ['inspect', params[3], '-s', test_schema_file]
        inspect(args)
