#! /usr/bin/env python

# ======================================================================
# matscipy - Python materials science tools
# https://github.com/libAtoms/matscipy
#
# Copyright (2014) James Kermode, King's College London
#                  Lars Pastewka, Karlsruhe Institute of Technology
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# ======================================================================

import unittest

import numpy as np

import matscipytest
import matscipy.contact_mechanics.Hertz as Hertz

###

class TestHertz(matscipytest.MatSciPyTestCase):

    def test_Hertz_centerline_stress(self):
        z = np.linspace(0.0, 5.0, 101)
        for nu in [ 0.3, 0.5 ]:
            srr1, szz1 = Hertz.centerline_stress(z, nu=nu)
            stt2, srr2, szz2, srz2 = Hertz.stress(np.zeros_like(z), z, nu=nu)

            self.assertTrue(np.max(np.abs(srr1-srr2)) < 1e-6)
            self.assertTrue(np.max(np.abs(srr1-stt2)) < 1e-6)
            self.assertTrue(np.max(np.abs(szz1-szz2)) < 1e-6)


    def test_Hertz_surface_stress(self):
        r = np.linspace(0.0, 5.0, 101)
        for nu in [ 0.3, 0.5 ]:
            pzz1, srr1, stt1 = Hertz.surface_stress(r, nu=nu)
            stt2, srr2, szz2, srz2 = Hertz.stress(r, np.zeros_like(r), nu=nu)

            self.assertTrue(np.max(np.abs(pzz1+szz2)) < 1e-6)
            self.assertTrue(np.max(np.abs(srr1-srr2)) < 1e-6)
            self.assertTrue(np.max(np.abs(stt1-stt2)) < 1e-6)

###

if __name__ == '__main__':
    unittest.main()
