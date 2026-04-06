from expression import Expression
from polynome import Polynome
from operations import Multiplication
import math

class Sin(Expression):
    """Expression representant sin(u)."""
    def __init__(self, expression: Expression):
        self.expression = expression
    
    def evaluer(self, x: float) -> float:
        resultat = self.expression.evaluer(x)
        return math.sin(resultat)
    
    def deriver(self) -> Expression:
        return Multiplication(Cos(self.expression), self.expression.deriver())
    
    def __str__(self) -> str:
        return f"sin({self.expression})"


class Cos(Expression):
    """Expression representant cos(u)."""
    def __init__(self, expression: Expression):
        self.expression = expression
    
    def evaluer(self, x: float) -> float:
        resultat = self.expression.evaluer(x)
        return math.cos(resultat)
    
    def deriver(self) -> Expression:
        return Multiplication(-Sin(self.expression), self.expression.deriver())
    
    def __str__(self) -> str:
        return f"cos({self.expression})"


class Exp(Expression):
    """Expression representant exp(u)."""
    def __init__(self, expression: Expression):
        self.expression = expression
    
    def evaluer(self, x: float) -> float:
        resultat = self.expression.evaluer(x)
        return math.exp(resultat)
    
    def deriver(self) -> Expression:
        return Multiplication(Exp(self.expression), self.expression.deriver())
    
    def __str__(self) -> str:
        return f"exp({self.expression})"
