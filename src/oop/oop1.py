# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle():
    # Base class
    pass


class FlightVehicle(Vehicle):
    # Primary subclass
    pass


class GroundVehicle(Vehicle):
    # Primary subclass
    pass


class Airplane(FlightVehicle):
    # Secondary subclass
    pass


class Starship(FlightVehicle):
    # Secondary subclass
    pass


class Car(GroundVehicle):
    # Secondary subclass
    pass


class Motorcycle(GroundVehicle):
    # Secondary subclass
    pass
