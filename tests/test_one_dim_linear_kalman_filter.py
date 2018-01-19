from unittest import TestCase

from Localization import one_dim_linear_kalman_filter as m

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
        self.measured_pos = [0., 1.2, 2.3, 4.1, 3.0, 6.1]
        self.motionref_vel = [1., 1., 2., -1., 3., 3.]
        self.mu = 0.                     # initial value of mu
        self.sig = 10000.                # initial value of sig
        self.measurement_sig = 4.
        self.motion_sig = 2.
        m.kalman_filter(self)
