from django.db import models

# Create your models here.
class Employee(models.Model):
    # fields of the model
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length = 15)
    last_name = models.CharField(max_length = 15)

    # To see the column name in the select query.
    def __str__(self):
        return str(self.employee_id) + ' ' + self.first_name + '_' + self.last_name