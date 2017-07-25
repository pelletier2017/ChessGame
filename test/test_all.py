from unittest import TestLoader, TextTestRunner, TestSuite

from test import test_pieces
from test import test_board

"""
Import this file to run all tests
"""

loader = TestLoader()
suite = TestSuite((
    loader.loadTestsFromModule(test_pieces),
    loader.loadTestsFromModule(test_board)
    ))
runner = TextTestRunner(verbosity=2)
runner.run(suite)
