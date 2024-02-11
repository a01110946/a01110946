"""
Module for managing room entities in a hotel reservation system.

Author: Fernando Maytorena
Last edited: February 08, 2024
"""


class Room:
    """Represents a room in a hotel.

    Attributes:
        room_number (int): The room number.
        room_type (str): The type of the room (e.g., single, double, suite).
        is_available (bool): Availability status of the room.
        price (float): Price per night for the room.
    """

    def __init__(self, room_number, room_type, price, is_available=True):
        """Initializes a Room with number, type, price, and availability.
           Initially, all rooms are available.

        Parameters:
            room_number (int): The room number.
            room_type (str): The type of the room.
            price (float): Price per night for the room.
            is_available (bool): Availability status of the room.
        """
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_available = is_available

    def make_reservation(self):
        """Marks the room as reserved (not available)."""
        self.is_available = False

    def cancel_reservation(self):
        """Marks the room as available (cancels reservation)."""
        self.is_available = True

    def update_price(self, new_price):
        """Updates the room's price.

        Parameters:
            new_price (float): The new price of the room.
        """
        self.price = new_price

    @classmethod
    def from_dict(cls, data):
        """Creates a Room instance from a dictionary.

        Parameters:
            data (dict): A dictionary containing room properties.

        Returns:
            Room: An instance of the Room class.
        """
        return cls(
            room_number=data['room_number'],
            room_type=data['room_type'],
            price=data['price'],
            is_available=data.get('is_available', True)  # Default to True if not specified
        )

    def to_dict(self):
        """
        Converts the Room instance into a dictionary representation.

        This method allows the Room object's current state to be represented
        as a dictionary, making it easier to serialize, especially for saving
        the room data in formats like JSON.

        Returns:
            dict: A dictionary containing the room's properties, including
                'room_number', 'room_type', 'price', and 'is_available'.
        """
        return {
            'room_number': self.room_number,
            'room_type': self.room_type,
            'price': self.price,
            'is_available': self.is_available
        }
