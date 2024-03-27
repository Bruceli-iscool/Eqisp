
import Lexer, parse
# change according to architecture
from compilerARM import CodeGenerator

def main(input_file, output_file):
    # Initialize lexer, parser, and code generator

    code_generator = CodeGenerator()

    # Read equations from the input file
    with open(input_file, 'r') as f:
        equations = f.readlines()

    # Process each equation
    assembly_code = []
    for equation in equations:
        # Tokenize the equation
        tokens = Lexer.tokenize(equation)
        # Parse tokens into AST
        ast = parse.parse(tokens)
        # Generate assembly code from AST
        code_generator.generate_code(ast)
        assembly_code.append(code_generator.asm)

    # Write assembly code to the output file
    with open(output_file, 'w') as f:
        for asm in assembly_code:
            f.write('\n'.join(asm))
            f.write('\n\n')

if __name__ == "__main__":
    # loop
    while True:
        userinput = input("> ")
        input_file, output_file = userinput.split(' -o ')
        main(input_file, output_file)
        # use ^X to exit