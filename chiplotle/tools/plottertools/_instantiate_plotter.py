from chiplotle.tools.serialtools import instantiate_serial_from_config_file
from chiplotle.tools.serialtools.virtual_serial_port import VirtualSerialPort
from chiplotle import plotters

def _instantiate_plotter(port, id):
   '''Instantiate a Plotter object with given `id` at port `port`. 
   
   - `port` a ``str`` address or number of serial port. 
      Usually something like '/def/ttyS0' in posix systems or 'COM1' Windowz.
      
      If port == None then instantiate a virtual serial port
      
   - `id` is the string ID of the plotter to be instantiated. e.g., 'DXY-1300'
   '''
   
   if port == None:
      ser = VirtualSerialPort()
      plotter = getattr(plotters, id)(ser)
      
      return plotter
   
   ser = instantiate_serial_from_config_file(port)

   from chiplotle.tools.plottertools import instantiate_plotter_from_id
   from chiplotle.tools.plottertools import interactive_choose_plotter
   plotter = instantiate_plotter_from_id(ser, id)
   if not plotter:
      print "\nChiplotle does not have a software Plotter type that"
      print "matches your hardware plotter %s." % id
      plotter = interactive_choose_plotter(ser)
   print "\nInstantiated plotter %s:" % plotter
   print "\tDrawing area: %s" % plotter.margins.soft
   print "\tBuffer Size: %s" % plotter.buffer_size
   return plotter
