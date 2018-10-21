#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. currentmodule:: test_env
.. moduleauthor:: Pat Daburu <pat@daburu.net>

This is the test module for the project's `env` module.
"""
import unittest
import arcpy
from djio_arcpy.env import Environment


class TestEnvironment(unittest.TestCase):
    """
    Test the `Environment` class.
    """

    def test_setValue_setValueInCtx_valueIsRestored(self):
        """
        Arrange:  Set a value on `arcpy.env`.
        Act:  Create a new `Environment` context and change the value.
        Assert:  After the context exits, the original value is restored.
        """
        arcpy.env.overwriteOutput = True
        with Environment():
            arcpy.env.overwriteOutput = False
            self.assertFalse(arcpy.env.overwriteOutput)
        self.assertTrue(arcpy.env.overwriteOutput)


if __name__ == '__main__':
    unittest.main()
