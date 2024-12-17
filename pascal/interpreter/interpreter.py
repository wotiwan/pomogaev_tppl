from .parser import Parser
from .__ast import Number, BinOp, UnaryOp, Block, Assignment, Var


class NodeVisitor:
    def visit(self):
        pass


class Interpreter(NodeVisitor):
    def __init__(self):
        self.parser = Parser()
        self.variables_assigned = {}

    def visit(self, node):
        if isinstance(node, Number):
            return self._visit_number(node)
        elif isinstance(node, BinOp):
            return self._visit_binop(node)
        elif isinstance(node, UnaryOp):
            return self._visit_unary(node)
        elif isinstance(node, Block):
            return self._visit_block(node)
        elif isinstance(node, Assignment):
            return self._visit_assignment(node)
        elif isinstance(node, Var):
            return self._visit_var(node)

    def _visit_var(self, node):
        if node.token.value not in self.variables_assigned:
            raise Exception(f"Variable {node.token.value} is undefined!")
        return self.variables_assigned[node.token.value]

    def _visit_assignment(self, node):
        var_name = node.var.token.value
        value = self.visit(node.exp)
        self.variables_assigned[var_name] = value

    def _visit_block(self, node):
        for i in node.expressions:
            self.visit(i)

    def _visit_unary(self, node):
        match node.op.value:
            case "+":
                return +self.visit(node.expr)
            case "-":
                return -self.visit(node.expr)

    def _visit_number(self, node: Number) -> float:
        return float(node.token.value)

    def _visit_binop(self, node: BinOp):
        match node.op.value:
            case "+":
                return self.visit(node.left) + self.visit(node.right)
            case "-":
                return self.visit(node.left) - self.visit(node.right)
            case "/":
                return self.visit(node.left) / self.visit(node.right)
            case "*":
                return self.visit(node.left) * self.visit(node.right)

    def eval(self, code: str) -> dict:
        self.variables_assigned = {}
        tree = self.parser.eval(code)
        self.visit(tree)
        return self.variables_assigned
