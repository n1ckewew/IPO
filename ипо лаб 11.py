class Scanner:
    def __init__(self, manufacturer, model, resolution, color_depth, interface_type, price):
        self.manufacturer = manufacturer
        self.model = model
        self.resolution = resolution
        self.color_depth = color_depth
        self.interface_type = interface_type
        self.price = price
    def set_resolution(self, resolution):
        """установить разрешение сканера"""
        self.resolution = resolution

    def set_price(self, price):
        """установить цену сканера"""
        self.price = price

    def get_manufacturer(self):
        """получить производителя сканера"""
        return self.manufacturer

    def get_price(self):
        """получить цену сканера"""
        return self.price
help(Scanner)
Scanner1 = Scanner("Canon", "Canoscan 9000F Mark II", 9600, 48, "USB", 199.99)
Scanner2 = Scanner("Epson", "Perfection V600", 6400, 48, "USB", 229.99)
Scanner3 = Scanner("HP", "Scanjet G4050", 4800, 96, "USB", 149.99)
Scanner4 = Scanner("Fujitsu", "fi-7160", 600, 24, "USB", 1199.99)
Scanner5 = Scanner("Brother", "ADS-2800W", 600, 30, "Ethernet", 399.99)
