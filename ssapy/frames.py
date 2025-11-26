# frames.py
import numpy as np
from astropy.time import Time

def teme_to_gcrf(t):
    try:
        from poliastro.frames import TEME
        from astropy.coordinates import GCRS, CartesianRepresentation
        if not isinstance(t, Time):
            t = Time(t, format="gps").utc
        basis = np.eye(3)
        cols = []
        for i in range(3):
            rep = CartesianRepresentation(*basis[i])
            vec = TEME(rep, obstime=t).transform_to(GCRS(obstime=t)).cartesian.xyz.value
            cols.append(vec)
        return np.array(cols, dtype=float).T
    except Exception:
        # Fallback: identity, meaning you are effectively staying in TEME
        # Consider logging a warning here
        return np.eye(3)