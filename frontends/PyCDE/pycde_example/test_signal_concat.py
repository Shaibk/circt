# 8-bit concatenation
from pycde import Module, Input, Output, types, generator,System
from pycde.signals import BitsSignal

class Signal_concat(Module):
    a = Input(types.int(4))
    b = Input(types.int(4))
    out = Output(types.int(8))

    @generator
    def build(self):
        self.out = BitsSignal.concat([self.a, self.b])  # 8-bit concatenation
system = System([Signal_concat], name="Signal_concat", output_directory="output_dir")
system.compile()
