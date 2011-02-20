from chiplotle.geometry.shapes.shape import _Shape
from chiplotle.tools.geometrytools.get_line_intersection \
   import get_line_intersection

def get_shape_intersections(shape1, shape2):
   '''Returns a generator of all intersecting points found in the 
   given shapes.'''

   if not isinstance(shape1, _Shape) or not isinstance(shape2, _Shape):
      raise TypeError

   for i in range(len(shape1)-1):
      for j in range(len(shape2)-1):
         intersection = get_line_intersection(
            line(s1[i], s1[i+1]), 
            line(s2[j], s2[j+1]))
         if intersection:
            yield intersection


## demo
if __name__ == '__main__':
   from chiplotle import *
   from chiplotle.hpgl.decorators.pen import PenDecorator
   from random import randint

   s1 = bezier_path([randint(0, 200) for  i in range(12)], 1, 14)
   s2 = bezier_path([randint(0, 200) for  i in range(12)], 1, 14)
   PenDecorator(Pen(4))(s1)
   PenDecorator(Pen(2))(s2)

   intersections = get_shape_intersections(s1, s2)
   marks = [ ]
   for i in intersections:
      c = circle(2)
      offset(c, i)
      marks.append(c)

   io.view(Group(marks + [s1, s2]))
