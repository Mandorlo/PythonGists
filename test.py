import unittest, os

loader = unittest.TestLoader()
tests = loader.discover('./test')
testRunner = unittest.runner.TextTestRunner()
testRunner.run(tests)