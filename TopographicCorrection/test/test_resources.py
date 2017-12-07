# coding=utf-8
"""Resources test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'forests2020@gmail.com'
__date__ = '2017-10-31'
__copyright__ = 'Copyright 2017, forests2020'

import unittest

from PyQt4.QtGui import QIcon



class TopographicCorrectionDialogTest(unittest.TestCase):
    """Test rerources work."""

    def setUp(self):
        """Runs before each test."""
        pass

    def tearDown(self):
        """Runs after each test."""
        pass

    def test_icon_png(self):
        """Test we can click OK."""
        path = ':/plugins/TopographicCorrection/icon.png'
        icon = QIcon(path)
        self.assertFalse(icon.isNull())

if __name__ == "__main__":
    suite = unittest.makeSuite(TopographicCorrectionResourcesTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)



