from typing import Tuple


class LALGCodeInterpreter:
    """A MEPA interpreter.

    The MEPA interpreter is a stack-based interpreter for the Linguagem Pascal Simplificada.
    See the documentation for more information.
    @see https://www.ic.unicamp.br/~tomasz/ilp/ilp.pdf
    """

    def __init__(self, code: list[str]):
        """Initializes the MEPA interpreter."""
        self.code = code
        self.instruction_pointer = 0
        self.stack: list[int] = []

    def __post_init__(self):
        """Initializes the MEPA interpreter."""
        self.instruction_pointer = 0
        self.stack = []

    def fetch_instruction(self) -> Tuple[str, int]:
        """Fetches the current instruction and its operand (if any)."""
        parts = self.code[self.instruction_pointer].split()
        instruction = parts[0]
        operand = int(parts[1]) if len(parts) > 1 else 0
        return instruction, operand

    def run(self):
        """Executes the MEPA code."""
        while True:
            instruction, operand = self.fetch_instruction()
            has_next_instruction = self.process_instruction(instruction, operand)
            if not has_next_instruction:
                break
            self.instruction_pointer += 1

    def process_instruction(self, instruction: str, operand: int) -> bool:
        """Processes a single instruction."""
        operations = {
            "INPP": self.init_program,
            "AMEM": self.allocate_memory,
            "CRCT": self.load_constant,
            "CRVL": self.load_value,
            "ARMZ": self.store_value,
            "SOMA": self.add_values,
            "SUBT": self.subtract_values,
            "MULT": self.multiply_values,
            "DIVI": self.divide_values,
            "MODI": self.modulus_operation,
            "INVR": self.invert_value,
            "CONJ": self.logical_and,
            "DISJ": self.logical_or,
            "NEGA": self.logical_not,
            "CMME": self.compare_less,
            "CMMA": self.compare_greater,
            "CMIG": self.compare_equal,
            "CMDG": self.compare_not_equal,
            "CMEG": self.compare_less_equal,
            "CMAG": self.compare_greater_equal,
            "DSVS": self.unconditional_jump,
            "DSVF": self.conditional_jump,
            "LEIT": self.read_integer,
            "LECH": self.read_character,
            "IMPR": self.print_integer,
            "IMPC": self.print_character,
            "IMPE": self.print_newline,
            "DMEM": self.deallocate_memory,
            "NADA": self.no_operation,
            "PARA": self.end_program,
        }

        operation = operations.get(instruction)
        if operation is None:
            self.abort(f"Unknown command: {instruction}")
            return False

        return operation(operand)

    def init_program(self, operand: int) -> bool:
        """Initializes the program."""
        self.instruction_pointer = 0
        self.stack = []
        return True

    def load_constant(self, operand: int) -> bool:
        """Loads a constant."""
        self.stack.append(operand)
        return True

    def load_value(self, operand: int) -> bool:
        """Loads a value from the stack."""
        # TODO: Check if should start backwards
        loaded_value = self.stack[operand]
        self.stack.append(loaded_value)
        return True

    def store_value(self, operand: int) -> bool:
        """Stores a value in memory."""
        self.stack[operand] = self.stack.pop()
        return True

    def add_values(self, operand: int) -> bool:
        """Adds values."""
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a + b)
        return True

    def subtract_values(self, operand: int) -> bool:
        """Subtracts values."""
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a - b)
        return True

    def multiply_values(self, operand: int) -> bool:
        """Multiplies values."""
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a * b)
        return True

    def divide_values(self, operand: int) -> bool:
        """Divides values."""
        b = self.stack.pop()
        a = self.stack.pop()
        if b == 0:
            self.abort(f"Division by zero: {a} / {b}")
            return False
        self.stack.append(a // b)
        return True

    def modulus_operation(self, operand: int) -> bool:
        """Performs a modulus operation."""
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a % b)
        return True

    def invert_value(self, operand: int) -> bool:
        """Inverts a value."""
        value = self.stack.pop()
        assert value is not None
        self.stack.append(-value)
        return True

    def logical_and(self, operand: int) -> bool:
        """Performs a logical and."""
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a and b)
        return True

    def logical_or(self, operand: int) -> bool:
        """Performs a logical or."""
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a or b)
        return True

    def logical_not(self, operand: int) -> bool:
        """Performs a logical not."""
        # TODO: Check if this is correct. If not, return to not self.stack.pop()
        value = self.stack.pop()
        assert value is not None
        self.stack.append(1 - value)
        return True

    def compare_less(self, operand: int) -> bool:
        """Compares values."""
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a < b)
        return True

    def compare_greater(self, operand: int) -> bool:
        """Compares values."""
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a > b)
        return True

    def compare_equal(self, operand: int) -> bool:
        """Compares values."""
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a == b)
        return True

    def compare_not_equal(self, operand: int) -> bool:
        """Compares values."""
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a != b)
        return True

    def compare_less_equal(self, operand: int) -> bool:
        """Compares values."""
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a <= b)
        return True

    def compare_greater_equal(self, operand: int) -> bool:
        """Compares values."""
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a >= b)
        return True

    def unconditional_jump(self, operand: int) -> bool:
        """Performs an unconditional jump."""
        # TODO: Check if should really be -1
        self.instruction_pointer = operand - 1
        return True

    def conditional_jump(self, operand: int) -> bool:
        """Performs a conditional jump."""
        if not self.stack.pop():
            self.instruction_pointer = operand - 1
        return True

    def read_integer(self, operand: int) -> bool:
        """Reads an integer."""
        self.stack.append(int(input("Enter an integer: ")))
        return True

    def read_character(self, operand: int) -> bool:
        """Reads a character."""
        self.stack.append(ord(input("Enter a character: ")[0]))
        return True

    def print_integer(self, operand: int) -> bool:
        """Prints an integer."""
        print(self.stack.pop())
        return True

    def print_character(self, operand: int) -> bool:
        """Prints a character."""
        character_ord = self.stack.pop()
        assert character_ord is not None
        print(chr(character_ord), end="")
        return True

    def print_newline(self, operand: int) -> bool:
        """Prints a newline."""
        # TODO: Check if this is correct
        print(self.stack.pop())
        return True

    def allocate_memory(self, operand: int) -> bool:
        """Allocates memory."""
        for _ in range(operand):
            self.stack.append(0)
        return True

    def deallocate_memory(self, operand: int) -> bool:
        """Deallocates memory."""
        for _ in range(operand):
            self.stack.pop()
        return True

    def no_operation(self, operand: int) -> bool:
        """Does nothing."""
        return True

    def end_program(self, operand: int) -> bool:
        """Ends the program."""
        return False

    def abort(self, message: str) -> bool:
        """Aborts the program."""
        print(f"Error: {message}. Aborting.")
        print(f"Stack: {self.stack}")
        return False
