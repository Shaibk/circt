# 2 to 1 32-bit multiplexer using PyCDE

from pycde import generator, dim, Clock, Input, Output, Module, types, System
from pycde.signals import Signal
from pycde.constructs import Mux
from pycde.testing import unittestmodule
from pycde.types import Bits

@unittestmodule()
class MUX2(Module):
  op = Input(Bits(1))
  a = Input(Bits(32))
  b = Input(Bits(32))
  out = Output(Bits(32))

  @generator
  def construct(self):
    self.out = Mux(self.op, self.a, self.b)


system = System([MUX2], name="MUX2", output_directory="output_dir")
system.compile()
