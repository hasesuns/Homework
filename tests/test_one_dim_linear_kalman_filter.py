from unittest import TestCase

# Add to path if you need
import sys
sys.path.append("./Localization/kalman_filter/")

from Localization.kalman_filter import one_dim_linear_kalman_filter as m

class Test(TestCase):

    def test_update(self):
        mean1 = 2.
        mean2 = 4.
        var1 = 4.
        var2 = 4.
        expected = [3., 2.]
        actual = m.update(mean1, var1, mean2, var2)
        self.assertEqual(expected, actual)

    def test_predict(self):
        mean1 = 1.3
        mean2 = 2.5
        var1 = 1.9
        var2 = 1.4
        expected = [3.8, 3.3]
        actual = m.predict(mean1, var1, mean2, var2)
        self.assertEqual(expected, actual)

    def test_main(self):
        m.main()
