# The Arm implementation
# x64 users look at compiler.py
class CodeGenerator:
    def __init__(self):
        self.asm = []

    def generate_code(self, ast):
        self.asm.append(".text")
        self.asm.append(".global _main")
        self.asm.append("_main:")
        self.asm.append("    mov x29, sp")  # Set up the frame pointer
        self.traverse_ast(ast)
        self.asm.append("    mov x0, x1")  # Move the result to x0 (convention for exit syscall)
        self.asm.append("    mov x8, 93")  # System call number for exit
        self.asm.append("    svc #0")      # Invoke exit syscall

    def traverse_ast(self, node):
        if node.type == 'expression':
            self.traverse_ast(node.left)
            self.asm.append("    str x0, [sp, #-8]!")  # Push the left operand onto the stack
            self.traverse_ast(node.right)
            self.asm.append("    ldr x1, [sp], #8")    # Pop the left operand from the stack to x1
        elif node.type == 'integer':
            self.asm.append(f"    mov x0, #{node.value}")  # Move the integer value to x0
        elif node.type == 'operator':
            self.asm.append("    ldr x1, [sp]")   # Load the right operand from the stack to x1
            self.asm.append("    add x0, x1, x0" if node.value == '+' else
                             "    sub x0, x1, x0" if node.value == '-' else
                             "    mul x0, x1, x0" if node.value == '*' else
                             "    sdiv x0, x1, x0")  # Divide x1 by x0 (signed division)