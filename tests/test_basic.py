# -*- coding: utf-8 -*-

from .context import ontoma

import unittest

print(ontoma.EFO_URL)
class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        assert True


if __name__ == '__main__':
    unittest.main()