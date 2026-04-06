from expression import Expression
from polynome import Polynome

class Addition(Expression):
    """Expression representant u + v."""
    def __init__(self, expressions: list[Expression]):
        self.expressions = expressions

    def evaluer(self, x: float) -> float:
        resultat = 0
        for expression in self.expressions: 
            resultat += expression.evaluer(x)
        return resultat
    
    def deriver(self) -> Expression:
        resultat = []
        for expression in self.expressions:
            resultat.append(expression.deriver())
        return Addition(resultat)

    def __str__(self) -> str:
        resultat = []
        for expression in self.expressions:
            resultat.append(str(expression))
        return " + ".join(resultat)

class Multiplication(Expression):
    """Expression representant u * v."""
    def __init__(self, expression1: Expression, expression2: Expression):
        self.expression1 = expression1
        self.expression2 = expression2

    def evaluer(self, x: float) -> float:
        resultat = 1
        resultat *= self.expression1.evaluer(x)
        resultat *= self.expression2.evaluer(x)
        return resultat

    def deriver(self) -> Expression:
        return Addition([
            Multiplication(self.expression1.deriver(), self.expression2),
            Multiplication(self.expression1, self.expression2.deriver())
        ])

    def __str__(self) -> str:
        return f"({self.expression1} * {self.expression2})"
