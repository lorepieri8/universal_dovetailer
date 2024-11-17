
from icecream import ic
from utils import text_from_bits, exit_after


class UniversalDovetailer:
    def __init__(self, early_stop_program_length = None):
        self.early_stop_program_length = early_stop_program_length

    def dovetail(self):
        # Generate and run all possible programs
        program_length = 0

        # Loop over all possible program lengths and allowed runtimes
        while True:
            program_length += 1

            # Early stopping, useful for debugging
            if self.early_stop_program_length is not None:
                if program_length > self.early_stop_program_length:
                    return

            for program in self.program_generator("", program_length):
                
                max_allowed_runtime = program_length # For simplicity we take them equal. We could relate them via an arbitrary monotonically increasing function.
                self.execute_program(program, max_allowed_runtime)

    def program_generator(self, program, max_program_length):
        # Generate all possible programs of length max_program_length

        if len(program) >= max_program_length:
            return
     
        for b in [0, 1]:
            new_program = program + str(b)
            yield new_program
            yield from self.program_generator(new_program, max_program_length)

    def program_exec(self, program):
        exec(program)    
        print('The program execution has finished successfully \n', flush=True)

    def execute_program(self, binary_program, max_running_time):   
        # Execute a binary string by converting it to a ascii program and running it.
        # max_running_time is the maximum allowed runtime for the program in seconds. 
            
        try:
            program = text_from_bits(binary_program)
            ic(binary_program, program)
            exit_after(max_running_time)(self.program_exec)(program)
        except:
            pass # The program is not valid Python code, or it errored out.
            










