"""
Module for managing hotel data in the reservation system.

Author: Fernando Maytorena
Last edited: February 08, 2024
"""

import json
import os
from bookinn.hotel.room import Room
from bookinn.reservation.reservation import make_reservation


class Hotel:
    """Represents a hotel within the reservation system, with persistence."""

    def __init__(self, name, location):
        """Initializes a Hotel object with a name and location."""
        self.name = name
        self.location = location
        self.rooms = []  # Could be a list of Room objects
        self.filename = f"{name}_data.json"

    def save_to_file(self):
        """Saves hotel data to a file."""
        data = {
            'name': self.name,
            'location': self.location,
            'rooms': [room.to_dict() for room in self.rooms]
        }
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f)

    def load_from_file(self):
        """Loads hotel data from a file."""
        with open(self.filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.name = data['name']
        self.location = data['location']
        # Assume a from_dict class method for Room to reconstruct room objects
        self.rooms = [Room.from_dict(room_data) for room_data in data['rooms']]  # pylint: disable=no-member

    @staticmethod
    def create_hotel(name, location):
        """Creates a new hotel and saves it to a file."""
        hotel = Hotel(name, location)
        hotel.save_to_file()
        return hotel

    @staticmethod
    def delete_hotel(hotel):
        """Deletes hotel data file."""
        os.remove(hotel.filename)

    def display_information(self):
        """Returns hotel information as a string."""
        return f"Hotel Name: {self.name}, Location: {self.location}"

    def modify_information(self, new_name=None, new_location=None):
        """Modifies hotel information and updates the file."""
        if new_name:
            self.name = new_name
        if new_location:
            self.location = new_location
        self.save_to_file()

    def reserve_room(self, reservation_id, customer_id, room_number,  # pylint: disable=too-many-arguments
                     start_date, end_date):
        """Reserve a room if available."""
        room = next((room for room in self.rooms if room.room_number == room_number and room.is_available), None)
        if room:
            room.make_reservation()
            reservation = make_reservation(
                reservation_id=reservation_id,
                customer_id=customer_id,
                hotel_name=self.name,
                room_number=room_number,
                start_date=start_date,
                end_date=end_date
            )
            reservation.save_to_file()
            self.save_to_file()
            return True
        return False

    def cancel_reservation(self, reservation_id):
        """Cancel a room reservation."""
        # This assumes reservation data includes the room number and can be matched to a room in this hotel
        try:
            with open(f"reservation_{reservation_id}.json", 'r', encoding='utf-8') as f:
                data = json.load(f)
            room_number = data['room_number']
            room = next((room for room in self.rooms if room.room_number == room_number), None)
            if room:
                room.cancel_reservation()
                os.remove(f"reservation_{reservation_id}.json")
                self.save_to_file()
                return True
        except FileNotFoundError:
            pass
        return False
