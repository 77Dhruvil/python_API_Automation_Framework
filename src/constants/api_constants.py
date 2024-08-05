#APIConstants - Class which contain all the endpoints
#Keep the URLs

class APIConstants(object):
    def base_url(self):
        return "https://restful-booker.herokuapp.com"
    
    def url_Create_booking(self):
        return "https://restful-booker.herokuapp.com/booking"

    def url_Create_Token(self):
        return "https://restful-booker.herokuapp.com/auth"

    #Update , PUT , PATCH , Delete - BookingID
    
    def url_patch_put_Delete(booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)
    

