from django.db import models

# Create your models here.
  
# declare a new model with a name "Accessorieslist"
class Accessorieslist(models.Model):
    # fields of the model
    accessories_list = models.CharField(max_length = 30)

    # To see the column name in the select query.
    def __str__(self):
        return self.accessories_list