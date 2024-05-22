import sys
import numpy as np
import freestream
import json

with open('params.json', 'r') as jsonf: params = json.load(jsonf)

ic = np.loadtxt('sd.dat')

fs = freestream.FreeStreamer(ic, params['trento']['grid_max'], params['freestream']['tau_freestream'])

for fmt, f, arglist in [('ed', fs.energy_density, [()]),
                        ('u{}', fs.flow_velocity, [(1,), (2,)]),
                        ('pi{}{}', fs.shear_tensor, [(1, 1), (1, 2), (2, 2)])]:
    for a in arglist:
        X = f(*a)
        np.savetxt(fmt.format(*a) + '.dat', X)

