from unittest import TestLoader, TextTestRunner, TestSuite
import sys

import test_pieces
import test_board
import test_player

"""
Import this file to run all tests
"""

loader = TestLoader()
suite = TestSuite((
    loader.loadTestsFromModule(test_pieces),
    loader.loadTestsFromModule(test_board),
    loader.loadTestsFromModule(test_player)
    ))
runner = TextTestRunner(verbosity=2)

if not runner.run(suite).wasSuccessful():
    sys.exit(1)