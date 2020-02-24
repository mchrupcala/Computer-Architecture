"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        #hold 256 bytes of memory
        self.memory = [0] * 256
        # 8 general-purpose registers
        self.r0, self.r1, self.r2, self.r3, self.r4, self.r5, self.r6, self.r7 = 0, 0, 0, 0, 0, 0, 0
        self.pc = 0

    def ram_read(self, read_address):
        #read the value at the read_address. Not sure if this is right...
        return self.memory[read_address]

    def ram_write(self, write_value, write_address):
        #accept the value to write & address to write it to
        pass

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self, operand_a=None, operand_b=None):
        """Run the CPU."""
        instruction_register = self.memory[self.pc]

        while True:
            if instruction_register == "HLT":
                # return False
                sys.exit(0)
            elif instruction_register == "LDI":
                self.memory[operand_a] = operand_b
                #Might need to skip steps
                self.pc += 1
            elif instruction_register == "PRN":
                print(self.memory[operand_a])
                self.pc += 1
            else:
                print(f"Sorry I couldn't find that command: {instruction_register}")
                sys.exit(0)