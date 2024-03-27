# Note that this implementation is for x64. ARM users refer to the compilerARM.py file
class CodeGenerator:
    def __init__(self):
        self.asm = []

    def generate_code(self, ast):
        self.asm.append(".intel_syntax noprefix")
        self.asm.append(".text")
        self.asm.append(".global _start")
        self.asm.append("_start:")
        self.traverse_ast(ast)
        self.asm.append("    mov rdi, rax")  # Move the result to rdi (convention for exit syscall)
        self.asm.append("    mov rax, 60")  # System call number for exit
        self.asm.append("    syscall")      # Invoke exit syscall

    def traverse_ast(self, node):
        if node.type == 'expression':
            self.traverse_ast(node.left)
            self.asm.append("    push rax")  # Push the left operand onto the stack
            self.traverse_ast(node.right)
            self.asm.append("    pop rbx")   # Pop the left operand from the stack to rbx
        elif node.type == 'integer':
            self.asm.append(f"    mov rax, {node.value}")  # Move the integer value to rax
        elif node.type == 'operator':
            self.asm.append("    pop rdi")   # Pop the right operand from the stack to rdi
            self.asm.append("    add rax, rdi" if node.value == '+' else
                             "    sub rax, rdi" if node.value == '-' else
                             "    imul rax, rdi" if node.value == '*' else
                             "    cqo\n    idiv rdi") 
