
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self._storage = storage 

    def specs(self):
        print(f"{self.brand} {self.model} with {self._storage}GB storage.")

    def call(self, number):
        print(f"Calling {number} from {self.model}...")


class GamingPhone(Smartphone):
    def specs(self):
        print(f"{self.brand} {self.model} is optimized for gaming with {self._storage}GB and a high-refresh display!")

class CameraPhone(Smartphone):
    def specs(self):
        print(f"{self.brand} {self.model} features a pro-grade camera and {self._storage}GB storage.")


phone1 = GamingPhone("Razer", "Blade X", 256)
phone2 = CameraPhone("Pixel", "ProShot", 128)

phone1.specs()
phone1.call("0712345678")

phone2.specs()
phone2.call("0798765432")
