from two_d_point import *
from rectangle import *
from quadrilateral import *
from square import *


class ShapeSorter:
    @staticmethod
    def sort(quadrilateral: List[Quadrilateral]) -> List[Quadrilateral]:
        quadrilateral.sort(key=Quadrilateral.smallest_x)
        return quadrilateral
    # return sort(quadrilateral, key=Quadrilateral.smallest_x)
