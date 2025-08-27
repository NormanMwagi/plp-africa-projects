class Smartphone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def make_call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}...")

    def send_message(self, number, message):
        print(f"Sending message to {number} from {self.brand} {self.model}: {message}")

    def __str__(self):
        return f"{self.brand} {self.model}"

class Samsung(Smartphone): # inheritance
    def __init__(self, model):
        super().__init__("Samsung", model)
        self.__mobilebanking = "MPESA" # private attribute

    def use_mobile_banking(self):
        print(f"Using mobile banking {self.__mobilebanking} on {self}.")
    def get_mobile_banking_service(self):
        return self.__mobilebanking
    def use_whatsapp(self): # polymorphism
        print(f"Using WhatsApp (Android version) on {self}.") 

class Iphone(Smartphone):
    def __init__(self, model):
        super().__init__("Apple", model)

    def use_apple_pay(self):
        print(f"Using Apple Pay on {self}.")

    def use_whatsapp(self):  # polymorphism
        print(f"Using WhatsApp (iOS version) on {self}.")


# Create objects
samsung_phone = Samsung("Galaxy S21")
iphone_phone = Iphone("iPhone 13 Pro")

# Demonstration
samsung_phone.make_call("+254792037392")
samsung_phone.send_message("+254792037392", "Hello from my Samsung!")
samsung_phone.use_mobile_banking()
iphone_phone.use_apple_pay()
iphone_phone.send_message("+254792037392", "Hello from my iPhone!")
iphone_phone.make_call("+254792037392")

# Polymorphism in action
phones = [samsung_phone, iphone_phone]
for phone in phones:
    phone.use_whatsapp()


