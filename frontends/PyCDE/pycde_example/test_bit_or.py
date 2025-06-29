#Instantiate a module that performs bitwise OR operation on two 32-bit integers
from pycde import Input, Output, Module, System
from pycde import generator
from pycde.types import Bits


class OrInts(Module):
  a = Input(Bits(32))
  b = Input(Bits(32))
  c = Output(Bits(32))

  @generator
  def construct(self):
    self.c = self.a | self.b

#Top module
class Top_OrInts(Module):
  a = Input(Bits(32))
  b = Input(Bits(32))
  c = Output(Bits(32))

  @generator
  def construct(self):

    add_ints = OrInts(a=self.a, b=self.b)
    self.c = add_ints.c


system = System([Top_OrInts], name="Top_OrInts", output_directory="output_dir")
system.compile()
