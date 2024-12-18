# Vehicle Rental System


from abc import ABC, abstractmethod


# Abstract Base Class
class Vehicle(ABC):
    """Abstract base class for all vehicles."""

    def __init__(
        self, vehicle_id: str, brand: str, model: str, daily_rate: float
    ):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.daily_rate = daily_rate
        self.is_rented = False

    # Concrete method
    def rent(self) -> None:
        """Marks the vehicle as rented."""
        if not self.is_rented:
            self.is_rented = True
            print(
                f"{self.brand} {self.model} (ID: {self.vehicle_id}) has been rented."
            )
        else:
            print(f"{self.brand} {self.model} is already rented.")

    # Concrete method
    def return_vehicle(self) -> None:
        """Marks the vehicle as available."""
        if self.is_rented:
            self.is_rented = False
            print(
                f"{self.brand} {self.model} (ID: {self.vehicle_id}) has been returned."
            )
        else:
            print(f"{self.brand} {self.model} is already available.")

    # Abstract method
    @abstractmethod
    def calculate_rental_cost(self, days: int) -> float:
        """Calculates the rental cost based on the number of days."""
        pass

    # Abstract method
    @abstractmethod
    def vehicle_type(self) -> str:
        """Returns the type of vehicle."""
        pass


# Concrete Class: Car
class Car(Vehicle):
    def __init__(
        self,
        vehicle_id: str,
        brand: str,
        model: str,
        daily_rate: float,
        seats: int,
    ):
        super().__init__(vehicle_id, brand, model, daily_rate)
        self.seats = seats

    def calculate_rental_cost(self, days: int) -> float:
        return self.daily_rate * days

    def vehicle_type(self) -> str:
        return "Car"

    def __str__(self):
        return f"Car: {self.brand} {self.model}, Seats: {self.seats}"


# Concrete Class: Bike
class Bike(Vehicle):
    def __init__(
        self,
        vehicle_id: str,
        brand: str,
        model: str,
        daily_rate: float,
        engine_capacity: int,
    ):
        super().__init__(vehicle_id, brand, model, daily_rate)
        self.engine_capacity = engine_capacity

    def calculate_rental_cost(self, days: int) -> float:
        # Bikes have a 10% discount for rentals longer than 3 days
        cost = self.daily_rate * days
        if days > 3:
            cost *= 0.9
        return cost

    def vehicle_type(self) -> str:
        return "Bike"

    def __str__(self):
        return f"Bike: {self.brand} {self.model}, Engine: {self.engine_capacity}cc"


# Concrete Class: Truck
class Truck(Vehicle):
    def __init__(
        self,
        vehicle_id: str,
        brand: str,
        model: str,
        daily_rate: float,
        load_capacity: int,
    ):
        super().__init__(vehicle_id, brand, model, daily_rate)
        self.load_capacity = load_capacity

    def calculate_rental_cost(self, days: int) -> float:
        # Trucks have an extra charge of 20% for heavy-duty rentals
        return self.daily_rate * days * 1.2

    def vehicle_type(self) -> str:
        return "Truck"

    def __str__(self):
        return f"Truck: {self.brand} {self.model}, Load Capacity: {self.load_capacity}kg"


# Example Usage
def main():
    # Create vehicle objects
    car = Car("C001", "Toyota", "Camry", 50, 5)
    bike = Bike("B001", "Yamaha", "R15", 30, 150)
    truck = Truck("T001", "Volvo", "FH16", 100, 2000)

    # List of vehicles
    vehicles = [car, bike, truck]

    # Interact with vehicles
    for vehicle in vehicles:
        print(f"Vehicle Type: {vehicle.vehicle_type()}")
        print(vehicle)
        vehicle.rent()
        print(
            f"Rental Cost for 4 days: ${vehicle.calculate_rental_cost(4):.2f}"
        )
        vehicle.return_vehicle()
        print("-" * 50)


if __name__ == "__main__":
    main()
