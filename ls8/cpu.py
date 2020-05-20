"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0 

    def load(self,program):
        """Load a program into memory."""

        address = 0

        with open(program) as f:
            for direction in f:
                trimmed = direction.split("#")[0].strip()
                if trimmed:
                    self.ram[address] = int(trimmed,2)
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
    
    def ram_read(self,address):
        return self.ram[address]

    def ram_write(self,address,value):
        self.ram[address] = value


    def run(self):
        """Run the CPU."""
        running = True
        IR = self.ram_read(self.pc)

        while running:
            if IR == 0b00000001:
                print("Quitting")
                self.pc = 0
                running = False

            elif IR == 0b10000010:
                self.reg[self.ram_read(self.pc + 1)] = self.ram_read(self.pc + 2)
                self.pc += 3
                IR = self.ram_read(self.pc)
            
            elif IR == 0b01000111:
                print(self.reg[self.ram_read(self.pc + 1)])
                self.pc += 2
                IR = self.ram_read(self.pc)

            elif IR == 0b10100010:
                print("HEY")
                ammount = self.reg[self.ram_read(self.pc + 2)] // 2
                new = self.reg[self.ram_read(self.pc + 1)] << ammount
                print(self.reg[self.ram_read(self.pc + 1)])
                print(self.reg[self.ram_read(self.pc + 2)])
                print(new)
                self.reg[self.ram_read(self.pc + 1,)] = new
                self.pc += 3
                IR = self.ram_read(self.pc)

            else:
                print("QUITTING DUE TO ERROR")
                self.pc = 0
                running = False

            

        
