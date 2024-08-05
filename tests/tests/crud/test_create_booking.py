import pytest
import allure

class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("Verify that Create Booking Status and Booking ID Shouldn't be null")
    @allure.description("Create a booking from the payload and Verify the Booking id should not be null")
    def test_create_booking_positive(self):
            pass