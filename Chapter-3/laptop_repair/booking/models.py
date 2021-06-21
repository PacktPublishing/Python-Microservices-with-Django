from django.db import models

# Create your models here.

# declare a new model with a name "Orderbook"
class Orderbook(models.Model):
    # fields of the model
    first_name = models.CharField(max_length = 15)
    last_name = models.CharField(max_length = 15)
    laptop_desc = models.CharField(max_length = 30)
    booking_date = models.CharField(max_length = 10)
    booking_time = models.CharField(max_length = 10)
    contact_number = models.IntegerField()
    address = models.CharField(max_length = 50)
    accessory = models.CharField(max_length = 20)
    additional_comment = models.CharField(max_length = 100)
    booking_id = models.CharField(max_length = 10)

    # To see the column name in the select query.
    def __str__(self):
        return self.first_name + ' ' + self.last_name + '_' + self.laptop_desc + '_' + self.booking_date + '_' + self.booking_time + '_' + str(self.contact_number) + '_' + self.address + '_' + self.accessory  + '_' + self.additional_comment + '_' + self.booking_id