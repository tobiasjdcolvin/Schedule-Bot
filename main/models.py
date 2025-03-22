from django.db import models

class UserInfo(models.Model):
    assignment_name = models.CharField(max_length=250)
    due_date = models.DateTimeField()

'''
# this table will only have one field for the image urls
class ImageData(models.Model):
    # this field (column) will contain text containing image URLs
    url = models.CharField(max_length=250)
'''