import argparse
from unittest import TestCase, mock
from indexdisplay import IndexDisplay


class TestIndexDisplay(TestCase):
    def setUp(self):
        self.indexdisplay = IndexDisplay()


class TestClass(TestIndexDisplay):
    # @mock.patch("builtins.input", return_value="[1, 2, 3, 1, 5]")
    # def testinputliststring(self, mock_input):
    #     self.indexdisplay.getlist()
    #     self.assertEqual("[1, 2, 3, 1, 5]", self.indexdisplay.inputListString)
    #
    # @mock.patch("builtins.input", return_value="{1: 10, 2: 33}")
    # def testinputdictstring(self, mock_input):
    #     self.indexdisplay.getdict()
    #     self.assertEqual("{1: 10, 2: 33}", self.indexdisplay.inputDictString)

    @mock.patch('argparse.ArgumentParser.parse_args',
                return_value=argparse.Namespace(kwarg1="[1, 2, 3, 1, 5]", kwarg2="{1: 10, 2: 33, 5: 28}"))
    def testprocess(self, mock_args):
        self.indexdisplay.process()
        captured = self.capsys.readouterr()
        print(f"Capture: {captured.out}")
        self.assertEqual([10, 33, 3, 10, 6], captured.out)
