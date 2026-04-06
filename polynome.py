from expression import Expression


class Polynome(Expression):
    """Polynome represente par une liste de coefficients [a0, a1, a2, ...]."""
    def __init__(self, coefficients: list[float]):
        self.coefficients = coefficients
    
    def evaluer(self, x: float) -> float:
        resultat = 0
        for i, coefficient in enumerate(self.coefficients):
            resultat += coefficient * x**i
        return resultat

    def deriver(self) -> Expression:
        resultat = []
        for i in range(1, len(self.coefficients)):
             resultat.append(self.coefficients[i] * i)
        return Polynome(resultat)

    def __str__(self)-> str:
        resultat = ""
        for i, coefficient in enumerate(self.coefficients):
            resultat += f"{coefficient}*x^{i}"

            if i == len(self.coefficients)-1:
                pass
            else:
                resultat += " + "
        return resultat
