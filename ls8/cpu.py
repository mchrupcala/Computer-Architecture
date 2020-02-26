"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        #hold 256 bytes of memory
        self.ram = [0] * 256
        # 8 general-purpose registers
        self.r0, self.r1, self.r2, self.r3, self.r4, self.r5, self.r6, self.r7 = 0, 0, 0, 0, 0, 0, 0, 0
        self.pc = 0
        self.reg = self.ram[self.pc]

    def ram_read(self, read_address):
        #read the value at the read_address. Not sure if this is right...
        return self.ram[read_address]

    def ram_write(self, write_value, write_address):
        #accept the value to write & address to write it to
        pass

    def load(self, program):
        """Load a program into memory."""
        # print("Program is: ", program)
        address = 0

        # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        elif op == "MUL":
            # print(self.ram[reg_a], self.ram[reg_b])
            print(reg_a, reg_b)
            reg_a *= reg_b
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

    def run(self):
    # , operand_a=None, operand_b=None
        """Run the CPU."""
        print(self.ram)
        while True:
            operand_a = self.ram_read(self.pc+1)
            operand_b = self.ram_read(self.pc+2)
            self.reg = self.ram[self.pc]

            if self.reg == 0b00000001:
                # return False
                sys.exit(0)
                #LDI
            elif self.reg == 0b10000010:
                self.ram[operand_a] = operand_b
                print('LDI while at ', self.reg)
                self.pc += 3
                #PRN
            elif self.reg == 0b01000111:
                print("Printing: ", self.ram[operand_a])
                self.pc += 2
            elif self.reg == 0b10100010:
                print(f"Multiplying at ", self.reg)
                self.alu("MUL", operand_a, operand_b)
                self.pc += 3
            else:
                print(f"Sorry I couldn't find that command: {self.reg}, {self.pc}")
                sys.exit(0)