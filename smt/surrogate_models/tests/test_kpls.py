"""
Author: Remi Lafage <<remi.lafage@onera.fr>>

This package is distributed under New BSD license.
"""

import unittest
import numpy as np
from smt.surrogate_models import KPLS
from smt.problems import Sphere
from smt.sampling_methods import FullFactorial, LHS


class TestKPLS(unittest.TestCase):
    def test_predict_output(self):
        d, n = (3, 10)
        sx = LHS(
            xlimits=np.repeat(np.atleast_2d([0.0, 1.0]), d, axis=0),
            criterion="m",
            random_state=42,
        )
        x = sx(n)
        sy = LHS(
            xlimits=np.repeat(np.atleast_2d([0.0, 1.0]), 1, axis=0),
            criterion="m",
            random_state=42,
        )
        y = sy(n)

        kriging = KPLS(n_comp=2)
        kriging.set_training_values(x, y)
        kriging.train()

        x_fail_1 = np.asarray([0, 0, 0, 0])
        x_fail_2 = np.asarray([0])

        self.assertRaises(ValueError, lambda: kriging.predict_values(x_fail_1))
        self.assertRaises(ValueError, lambda: kriging.predict_values(x_fail_2))
        var = kriging.predict_variances(x)
        self.assertEqual(y.shape[0], var.shape[0])


if __name__ == "__main__":
    unittest.main()
