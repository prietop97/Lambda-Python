"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0
        self.fl = 0b00000000

    def load(self,program):
        """Load a program into memory."""

        address = 0

        with open(program) as f:
            for direction in f:
                trimmed = direction.split("#")[0].strip()
                if trimmed:
                    self.ram[address] = int(trimmed,2)
                    address += 1

    def equals(self,reg_a,reg_b):
        if reg_a ^ reg_b:
            return False
        else:
            return True
        

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            carry = 0b00000000
            addition = 0b00000000
            num_1 = reg_a
            num_2 = reg_b
            first = True
            while carry or first:
                first = False
                carry = num_1 & num_2
                addition = num_1 ^ num_2
                num_1 = carry << 1
                num_2 = addition
            return addition
        elif op == "SUB":
            carry = 0b00000000
            sub = 0b00000000
            num_1 = reg_a
            num_2 = reg_b
            first = True
            while carry or first:
                first = False
                carry = num_1 & num_2
                sub = num_1 ^ num_2
                num_1 = carry >> 1
                num_2 = sub
            return sub
        elif op == "MULT":
            final = 0
            for i in range(reg_b):
                final += self.alu("ADD",reg_a,reg_a)
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
        SP = 7

        while running:
            print(self.alu("SUB",0b00000011,0b10000000))
            if IR == 0b00000001:
                print("Quitting")

                self.pc = 0
                running = False

            elif IR == 0b10000010: ##LDI
                self.reg[self.ram_read(self.pc + 1)] = self.ram_read(self.pc + 2)
                self.pc += 3
                IR = self.ram_read(self.pc)
            
            elif IR == 0b01000111: ##PRINT
                print(self.reg[self.ram_read(self.pc + 1)])
                self.pc += 2
                IR = self.ram_read(self.pc)

            elif IR == 0b10100010: ##MULT
                self.reg[self.ram_read(self.pc + 1)] = self.reg[self.ram_read(self.pc + 2)] * self.reg[self.ram_read(self.pc + 1)]
                self.pc += 3
                IR = self.ram_read(self.pc)
            elif IR == 0b01000101: ##PUSH
                SP -= 1
                self.reg[SP] = self.reg[self.ram_read(self.pc + 1)]
                self.pc += 2
                IR = self.ram_read(self.pc)
            elif IR == 0b01000110: ##POP
                self.reg[self.ram_read(self.pc + 1)] = self.reg[SP]
                SP += 1
                self.pc += 2
                IR = self.ram_read(self.pc)
            elif IR == 0b01010000: ##CALL
                next_pc = self.pc + 2
                SP -= 1
                self.reg[SP] = next_pc
                self.pc = self.reg[self.ram_read(self.pc + 1)]
                IR = self.ram_read(self.pc)
            elif IR == 0b00010001: ##RET
                self.pc = self.reg[SP]
                SP += 1
                IR = self.ram_read(self.pc)
            elif IR == 0b10100000: ##ADD
                
                self.reg[self.ram_read(self.pc + 1)] = self.alu("ADD",)self.reg[self.ram_read(self.pc + 2)]
                self.pc += 3
                IR = self.ram_read(self.pc)
            elif IR == 0b10100000: ##CMP
                same = 0b00000001
                less = 0b00000100
                more = 0b00000010



                self.pc += 3
                IR = self.ram_read(self.pc)
            else:
                print(f"QUITTING DUE TO ERROR ON CALL {IR}")
                self.pc = 0
                running = False

            

        
