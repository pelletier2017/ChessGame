from unittest import TestLoader, TextTestRunner, TestSuite
import test_pieces
import test_board

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