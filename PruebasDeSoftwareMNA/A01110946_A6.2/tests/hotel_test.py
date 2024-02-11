"""
Unit tests for the Hotel class.

This module contains tests that verify the functionality of the Hotel class,
ensuring that all methods behave as expected under various conditions.
"""

import unittest
import os
from bookinn.hotel.hotel import Hotel
from bookinn.hotel.room import Room


class TestHotel(unittest.TestCase):
    """Test cases for the Hotel class.

    This class implements unit tests for the Hotel class, covering initial setup,
    room management, and information display functionalities.
    """
    def setUp(self):
        self.hotel = Hotel("Test Hotel", "Test Location")
        test_room = Room(room_number=101, room_type="single", price=100.00, is_available=True)
        self.hotel.rooms.append(test_room)

    def test_create_hotel(self):
        """Test creating a hotel correctly initializes its attributes."""
        name = "New Hotel"
        location = "New Location"
        hotel = Hotel.create_hotel(name, location)
        self.assertEqual(hotel.name, name, "Hotel name should match the provided name.")
        self.assertEqual(hotel.location, location, "Hotel location should match the provided location.")
        # Cleanup created hotel data file to avoid side effects
        os.remove(hotel.filename)

    def test_delete_hotel(self):
        """Test deleting a hotel removes its data file."""
        hotel = Hotel.create_hotel("Temporary Hotel", "Temporary Location")
        # Ensure the file exists before deletion
        self.assertTrue(os.path.exists(hotel.filename), "Hotel data file should exist before deletion.")
        Hotel.delete_hotel(hotel)
        # Verify the file no longer exists
        self.assertFalse(os.path.exists(hotel.filename), "Hotel data file should be deleted.")

    def test_display_information(self):
        """Test displaying hotel information"""
        expected_output = "Hotel Name: Test Hotel, Location: Test Location"
        self.assertEqual(self.hotel.display_information(), expected_output)

    def test_modify_information(self):
        """Test modifying hotel information updates the hotel attributes."""
        new_name = "Updated Test Hotel"
        new_location = "Updated Test Location"
        self.hotel.modify_information(new_name=new_name, new_location=new_location)

        # Verify that the hotel's information has been updated
        self.assertEqual(self.hotel.name, new_name, "Hotel name should be updated.")
        self.assertEqual(self.hotel.location, new_location, "Hotel location should be updated.")

    def test_reserve_room(self):
        """Test reserving a room changes its availability."""

        room_number = 101  # Define the room number as a variable

        # Attempt to reserve a room
        result = self.hotel.reserve_room("reservation_id", "customer_id", room_number, "2023-01-01", "2023-01-05")

        # Assert: Check the room is now reserved (not available)
        self.assertTrue(result, "Room reservation should succeed")
        reserved_room = next((r for r in self.hotel.rooms if r.room_number == room_number), None)
        self.assertIsNotNone(reserved_room, "Reserved room should exist in hotel")
        self.assertFalse(reserved_room.is_available, "Room should be marked as not available after reservation")

    def test_cancel_reservation(self):
        """Test canceling a reservation marks the room as available again."""
        # Setup: Create a hotel, add a room, and make a reservation
        hotel = Hotel("Hotel for Reservation", "Reservation Location")
        room_number = 101
        hotel.rooms.append(Room(room_number, "double", 150))
        reservation_id = "res101"
        hotel.reserve_room(reservation_id, "cust101", room_number, "2023-01-01", "2023-01-05")

        # Act: Cancel the reservation
        hotel.cancel_reservation(reservation_id)

        # Assert: The room is available again
        room = next((room for room in hotel.rooms if room.room_number == room_number), None)
        self.assertIsNotNone(room, "The room should exist.")
        self.assertTrue(room.is_available, "The room should be available after canceling the reservation.")


if __name__ == '__main__':
    unittest.main()
