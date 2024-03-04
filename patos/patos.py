from abc import ABC, abstractmethod

# ----------INTERFAZ------------------
class FlyBehavior(ABC):
    @abstractmethod
    def fly(self, pato):
        pass

# CLASES CONCRETAS DE LA CLASE FlyBehavior

# CLASE CONCRETA 1 FLYWITHWINGS
class FlyWithWings(FlyBehavior):
    def fly(self, pato):
        print("Este pato", pato, "si vuela")

# --------------------------------

# CLASE CONCRETA 2 FLYNOWAY
class FlyNoWay(FlyBehavior):
    def fly(self, pato):
        print("Este pato", pato, "no vuela")

# -------------------------

# CLASE CONCRETA 3 FLYWITHBALLON
class FlyWithBallon(FlyBehavior):
    def fly(self, pato):
        print("Este pato", pato, "vuela con globos")

# ------------------------------

# ------------FIN DE CLASES CONCRETAS----------------

# -------------INTERFAZ-----------------------------
class QuackBehavior(ABC):
    @abstractmethod
    def cuack(self, pato):
        pass

# CLASES CONCRETAS DE LA CLASE QUACKBEHAVIOR

# CLASE CONCRETA 1 QUACK
class Quack(QuackBehavior):
    def cuack(self, pato):
        print("Este pato", pato, "si grazna")

# -----------------------

# CLASE CONCRETA 2 SQUEAK
class Squeak(QuackBehavior):
    def cuack(self, pato):
        print("Este pato", pato, "solo chilla")

# -----------------------

# CLASE CONCRETA 3 MUTEQUACK
class MuteQuack(QuackBehavior):
    def cuack(self, pato):
        print("Este pato", pato, "no hace ruido")

# --------------------------

# FIN DE CLASES CONCRETAS DE QUACK BEHAVIOR

# ---------------CLASE ABSTRACTA--------------

class Duck:
    def __init__(self):
        self.fb = None
        self.qb = None

    def display(self, pato):
        pass

    def setQuackBehavior(self, q):
        self.qb = q

    def setFlyBehavior(self, f):
        self.fb = f

    def perfomQuack(self, pato):
        if self.qb:
            self.qb.cuack(pato)

    def performfly(self, pato):
        if self.fb:
            self.fb.fly(pato)

    def swim(self):
        print("Nadando")

    def showDuck(self):
        self.display("Pato")

# CLASES CONCRETAS DE CLASE DUCK

# CLASE CONCRETA 1 MALLARDDUCK
class MallarDuck(Duck):
    def display(self, pato):
        print("Este es un pato", pato, "llamado pato real")

# ----------------------------

# CLASE CONCRETA 2 RUBBERTDUCK
class RubbertDuck(Duck):
    def display(self, pato):
        print("Este es un pato", pato, "o sea de hule")

# ----------------------------

# CLASE CONCRETA 3 DECOYDUCK
class DecoyDuck(Duck):
    def display(self, pato):
        print("Este es y pato", pato, "de decoracion")

# --------------------------

# CLASE CONCRETA 4 READHEADDUCK
class ReadHeadDuck:
    def display(self, pato):
        print("Este es un pato", pato, "de cabeza roja")

# -----------------------------

# FIN DE CLASES CONCRETAS DE CLASE DUCK

# ---------FIN DE CLASE ABSTRACTA--------------

if __name__ == "__main__":
    # VARIABLES DE LAS CLASES CONCRETAS DE QUACKBEHAVIOR
    Q = Quack()
    patoS = Squeak()
    patoMQ = MuteQuack()
    patoMQ2 = MuteQuack()

    # VARIABLES DE LAS CLASES CONCRETAS DE FLYBEHAVIOR
    Q1 = FlyWithWings()
    patoFN = FlyNoWay()
    patoFB = FlyWithBallon()
    patoFB2 = FlyWithBallon()

    # VARIABLES DE LAS CLASES CONCRETAS DE DUCK
    MD = MallarDuck()
    RB = RubbertDuck()
    DD = DecoyDuck()
    RH = ReadHeadDuck()

    pato = Duck()

    # ----PATO CABEZA ROJA----
    print("//----------------------------//")
    pato.setQuackBehavior(Q)
    pato.perfomQuack("Red")

    pato.setFlyBehavior(Q1)
    pato.performfly("Red")

    print("//----------------------------//")
    print()

    # ----PATO MALLARD----
    print("//----------------------------//")
    pato.setQuackBehavior(patoS)
    pato.perfomQuack("Mallard")

    pato.setFlyBehavior(patoFN)
    pato.performfly("Mallard")
    print("//----------------------------//")
    print()

    # ----PATO DE HULE----
    print("//----------------------------//")
    pato.setQuackBehavior(patoMQ)
    pato.perfomQuack("Rubber")

    pato.setFlyBehavior(patoFB)
    pato.performfly("Rubber")
    print("//----------------------------//")
    print()

    # ----PATO DE MADERA----
    print("//----------------------------//")
    pato.setQuackBehavior(patoMQ2)
    pato.perfomQuack("Decoy")

    pato.setFlyBehavior(patoFB2)
    pato.performfly("Decoy")
    print("//----------------------------//")
    print()
