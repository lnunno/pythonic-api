"""
A multi-dimensional ``Vector`` class
"""

from array import array
import math
import numbers
import repr


class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __len__(self):
        return len(self._components)

    def __iter__(self):
        return iter(self._components)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __eq__(self, other):
        return (len(self) == len(other) and
                all(a == b for a, b in zip(self, other)))

    def __str__(self):
        return str(tuple(self))

    def __repr__(self):
        components = repr.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    def __mul__(self, scalar):
        if isinstance(scalar, numbers.Real):
            return Vector(n * scalar for n in self)
        else:
            return NotImplemented

    def __rmul__(self, scalar):
        return self * scalar

    # exercise solutions below...

    def __add__(self, v):
        if isinstance(v, numbers.Real):
            return NotImplemented
        elif len(v) != len(self):
            raise ValueError('Mismatched lengths for add.')
        else:
            return Vector(a+b for a,b in zip(self, v))

    def __radd__(self, v):
        return self + v

    def __neg__(self):
        c_neg = [-a for a in self._components]
        return Vector(c_neg)
