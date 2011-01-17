## TODO: delete. deprecated in favor of _HPGLCompound
#from chiplotle.hpgl.abstract.hpgl import _HPGL
#from chiplotle.geometry.vector import Vector
#from chiplotle.hpgl.commands import PA, PU, SP
#from chiplotle.hpgl.compound.pen import Pen
#import types
#
#class _CompoundHPGL(_HPGL):
#   
#   _scalable = ['xy']
#
#   def __init__(self, xy, pen=None):
#      self.pen = pen
#      self.xy = xy
#
#   ## PUBLIC ATTRIBUTES ##
#
#   @apply
#   def xy( ):
#      def fget(self):
#         return self._coords
#      def fset(self, arg):
#         self._coords = Vector(arg)
#      return property(**locals())
#
#   @apply
#   def x( ):
#      def fget(self):
#         return self._coords.x
#      def fset(self, arg):
#         self.xy = Vector(arg, self.y)
#      return property(**locals())
#
#   @apply
#   def y( ):
#      def fget(self):
#         return self._coords.y
#      def fset(self, arg):
#         self.xy = Vector(self.x, arg)
#      return property(**locals())
#
#   @property
#   def format(self):
#      result = ''
#      for c in self._subcommands:
#         result += c.format
#      return result
#
#   @apply
#   def pen( ):
#      def fget(self):
#         return self._pen
#      def fset(self, pen):
#         if isinstance(pen, int):
#            self._pen = Pen(pen)
#         elif isinstance(pen, (Pen, types.NoneType)):
#            self._pen = pen
#         else:
#            raise TypeError('pen must be a Pen( ) instance, int or None.')
#      return property(**locals( ))
#
#
#   ## PRIVATE ATTRIBUTES ##
#
#   ### TODO should _subcommands return a Generator rather than a list?
#   @property
#   def _subcommands(self):
#      result = [ ]
#      if self.pen:
#         result.append(self.pen)
#      result.extend([PU( ), PA(self.xy)])
#      return result
#
#
#   ## OVERRIDES ##
#   
#   def __repr__(self):
#      return self.__class__.__name__ + "( )"
