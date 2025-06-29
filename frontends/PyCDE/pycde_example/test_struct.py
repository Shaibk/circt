from pycde import Clock, Output, Input, generator, types, Module, System
from pycde.constructs import Mux

class Buffer(Module):
    clk = Clock()
    master = Input(types.struct({
        "valid": types.int(1),
        "data": types.int(32)
    }))
    out = Output(types.int(32))

    @generator
    def build(self):
        self.out = Mux(self.master.valid, self.master.data.reg().reg(), types.int(32)(0))

system = System([Buffer], name="Buffer", output_directory="output_dir")
system.compile()
