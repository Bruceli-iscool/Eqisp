# create ASTs
class ASTNode:
    def __init__(self, type, value=None, left=None, right=None):
        self.type = type
        self.value = value
        self.left = left
        self.right = right
# Function to parse tokens and assemble AST
def parse(tokens):
    if not tokens:
        return None

    root = ASTNode('expression')
    current_node = root

    for token in tokens:
        # This is the reason for the lexer.
        if token[0] == 'INTEGER':
            current_node.right = ASTNode('integer', value=token[1])
        elif token[0] == 'OPERATOR':
            current_node.left = current_node.right
            current_node.right = ASTNode('operator', value=token[1])
            current_node = current_node.right

    return root
def visualize_ast(node, indent=0):
    if node is None:
        return

    print(" " * indent + str(node.type), node.value)
    visualize_ast(node.left, indent + 2)
    visualize_ast(node.right, indent + 2)

visualize_ast(parse("[('INTEGER', 1), ('OPERATOR', '+')]"))