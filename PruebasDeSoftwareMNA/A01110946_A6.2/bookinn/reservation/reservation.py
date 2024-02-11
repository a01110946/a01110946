"""
Module for managing reservations in the hotel reservation system.

Author: Fernando Maytorena
Last edited: February 08, 2024
"""

import json
import os


class Reservation:
    """Represents a reservation in the hotel reservation system.

    Attributes:
        reservation_id (int): Unique identifier for the reservation.
        customer_id (int): The customer's ID who made the reservation.
        hotel_name (str): The name of the hotel where the reservation is made.
        room_number (int): The room number reserved.
        start_date (str): The start date of the reservation.
        end_date (str): The end date of the reservation.
    """

    def __init__(self, **kwargs):
        """Initializes a Reservation with necessary details."""
        self.reservation_id = kwargs.get('reservation_id')
        self.customer_id = kwargs.get('customer_id')
        self.hotel_name = kwargs.get('hotel_name')
        self.room_number = kwargs.get('room_number')
        self.start_date = kwargs.get('start_date')
        self.end_date = kwargs.get('end_date')

    def save_to_file(self):
        """Saves reservation details to a file."""
        data = vars(self)
        filename = f"reservation_{self.reservation_id}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f)

    @staticmethod
    def cancel_reservation(reservation_id):
        """Cancels a reservation by removing its file."""
        filename = f"reservation_{reservation_id}.json"
        os.remove(filename)

    @classmethod
    def create_reservation(cls, **kwargs):
        """Creates a new reservation and saves it to a file."""
        reservation = cls(**kwargs)
        reservation.save_to_file()
        return reservation


def make_reservation(**kwargs):
    """Factory function to create a Reservation instance."""
    return Reservation(**kwargs)
