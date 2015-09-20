""" Functional tests for method deprecation. """
# pylint: disable=missing-docstring
import html.parser
import unittest
import distutils
import xml.etree.ElementTree

html.parser.unescape('a')   # [deprecated-method]


class MyTest(unittest.TestCase):
    def test(self):
        self.assert_(True)  # [deprecated-method]

REG = distutils.command.register.register('a')
REG.check_metadata()        # [deprecated-method]

xml.etree.ElementTree.Element('tag').getchildren()  # [deprecated-method]