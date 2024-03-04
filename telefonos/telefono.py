from typing import List

class Observer:
    def update(self):
        pass

class Cliente1(Observer):
    def update(self):
        print("Cliente1 actualizado")

class Cliente2(Observer):
    def update(self):
        print("Cliente2 actualizado")

class Cliente3(Observer):
    def update(self):
        print("Cliente3 actualizado")

class IPhone:
    def __init__(self):
        self.observers: List[Observer] = []
        self.producto = None

    def registerObserver(self, observer: Observer):
        self.observers.append(observer)

    def removeObserver(self, observer: Observer):
        self.observers.remove(observer)

    def notifyObservers(self):
        for observer in self.observers:
            observer.update()

    def valuesChanged(self):
        self.notifyObservers()

    def setNewProduct(self, product):
        self.producto = product
        self.valuesChanged()

# Ejemplo de uso
if __name__ == "__main__":
    iphone = IPhone()
    cliente1 = Cliente1()
    cliente2 = Cliente2()
    cliente3 = Cliente3()

    iphone.registerObserver(cliente1)
    iphone.registerObserver(cliente2)
    iphone.registerObserver(cliente3)

    iphone.setNewProduct("Nuevo iPhone lanzado")

