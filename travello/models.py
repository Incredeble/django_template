from django.db import models

# Create your models here.
class Destination:
    id:int
    name:str
    price:str
    img:str
    desc:str
    offer:bool