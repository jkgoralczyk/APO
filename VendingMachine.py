import time

class Product:
    def __init__(self, number, name, price, quantity):
        self.number = number
        self.name = name
        self.price = price
        self.quantity = quantity

    def buyProduct(self):
        if self.quantity == 0:
            print('\nBrak ' + self.name + '!\nPoczekaj na uzupełnienie!')
            time.sleep(5)
            self.quantity += 5
            print('\nUzupełniono :)\n')
        self.quantity -= 1

class VendingMachine:
    def __init__(self):
        self.amount = 0
        self.items = []

    def addProduct(self, item):
        self.items.append(item)

    def showProducts(self):
        print('\n'+'|{:<10}|{:<10}|{:<10}|{:<10}'.format('Numer:','Nazwa:','Cena:','Ilosc:')+'\n-----------------------------------------')
        for item in self.items:
            print('|{:<10}|{:<10}|{:<10}|{:<10}'.format(item.number, item.name, item.price, item.quantity))

    def buyProduct(self, item):
            self.amount -= item.price
            item.buyProduct()
            print('\nWydano: ' + item.name + '\nReszta: ' + str(self.amount))
            self.amount = 0

    def containsProduct(self, wanted):
        get = False
        for item in self.items:
            if item.number == int(wanted):
                get = True
                break
        return get

    def getProduct(self, wanted):
        get = None
        for item in self.items:
            if item.number == int(wanted):
                get = item
                break
        return get

    def insertCash(self, item):
        price = item.price
        print()
        while self.amount < price:
                self.amount = self.amount + float(input('Wrzuć ' + str(price - self.amount) + ' : '))

    def payCard(self):
            print("\nZbliz kartę!")
            time.sleep(5)
            input("Podaj pin: ")
            print("\nPlatnosc zaakceptowana!")

    def choosePayment(self, number, item):
        if number == 1:
            VendingMachine.payCard(self)
        else: VendingMachine.insertCash(self, item)

def main():

    vend = VendingMachine()
    vend.addProduct(Product(12, 'Cola', 1.5, 5))
    vend.addProduct(Product(23, 'Kitkat', 1.75, 10))
    vend.addProduct(Product(34, 'Mleko', 2.0, 2))
    vend.addProduct(Product(45, 'Kawa', 2.50, 5))
    vend.addProduct(Product(56, 'Chipsy', 3.15, 5))
    vend.addProduct(Product(67, 'Obiad', 29.99, 1))

    while(1):
        vend.showProducts()
        selected = input('\nPodaj numer produktu: ')
        if vend.containsProduct(selected):
            item = vend.getProduct(selected)
            vend.choosePayment(int(input("\n( 1.Karta  2.Gotówka )\nWybierz rodzaj platnosci: ")),item)
            vend.buyProduct(item)
            print('\nDziekujemy za zakupy!\n')
        else:
            print('Nie ma takiego produktu. Podaj inny numer.')
            continue

main()