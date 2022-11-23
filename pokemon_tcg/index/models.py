from django.db import models
import os
import random
import string


def get_random_string():
    # With combination of lower and upper case
    length = 25
    result_str = ''.join(random.choice(string.ascii_letters)
                         for i in range(length))
    return result_str


class Collection(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(
        max_length=128, blank=True, default="My_Collection")
    createDate = models.DateTimeField(auto_now=True)
    buyValue = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, default=0.00)
    listValue = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, default=0.00)
    sellValue = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, default=0.00)

    class Meta:
        db_table = 'collection'


class PokeCard(models.Model):
    franchises = (
        ('Pokemon', 'Pokemon'),
        ('YuGiOh', 'YuGiOh'),
        ('Magic', 'Magic'),
    )

    conditions = (
        ('None', None),
        ('MT', 'Mint'),
        ('NM', 'Near Mint'),
        ('LP', 'Lightly Played'),
        ('MP', 'Moderately Played'),
        ('HP', 'Heavily Played'),
        ('DM', 'Damaged'),

    )

    tcgseries = (
        ('00', None),
        ('BS', 'BASE'),
        ('JG', 'JUNGLE'),
        ('FS', 'FOSSIL'),
        ('PRO', 'PROMO'),
        ('BS2', 'BASE2'),
        ('TR', 'TEAMROCKET'),
        ('GYM', 'GYM_CHALLENGE_OR_HEROES'),
        ('GO', 'POKEMON_GO'),
        ('NEO', 'NEO-REVELATION/GENESIS/DISCOVERY/DESTINY'),
        ('LEG', 'LEGENDARY_COLLECTION'),
        ('AQU', 'AQUAPOLIS'),
        ('SKY', 'SKYRIDGE'),

    )

    id = models.BigAutoField(primary_key=True)
    collection = models.ForeignKey(
        Collection, on_delete=models.CASCADE, verbose_name="collection")
    franchise = models.CharField(
        max_length=32, choices=franchises, default="Pokemon", blank=True)
    condition = models.CharField(
        max_length=32, choices=conditions, default=None, blank=True)
    pokeName = models.CharField(max_length=128, default=None, blank=True)
    firstEdition = models.BooleanField(default=False, blank=True)
    shadowless = models.BooleanField(default=False, blank=True)
    series = models.CharField(
        max_length=128, default=None, choices=tcgseries, blank=True)

    createDate = models.DateTimeField(auto_now=True)
    purchaseDate = models.DateField(blank=True, default=None)

    buyPrice = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, default=0.00)
    listPrice = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, default=0.00)
    sellPrice = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, default=0.00)

    front = models.ImageField(
        upload_to="collection/" + str(collection) + "/" + str(id) + "/")
    back = models.ImageField(
        upload_to="collection/" + str(collection) + "/" + str(id) + "/")

    notes = models.TextField(max_length=2048, default=None, blank=True)

    class Meta:
        db_table = 'PokeCard'

# class Person(models.Model):
#    first_name = models.CharField(max_length=30)
#    last_name = models.CharField(max_length=30)
#    class Meta:
#       db_table = 'Person'
#
#
# class Musician(models.Model):
#    SHIRT_SIZES = (
#        ('S', 'Small'),
#        ('M', 'Medium'),
#        ('L', 'Large'),
#    )
#    id = models.BigAutoField(primary_key=True)
#    first_name = models.CharField(max_length=50)
#    person = models.ForeignKey(
#        Person,
#        on_delete=models.CASCADE,
#        verbose_name="the related person",
#    )
#    MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE')
#    medal = models.CharField(
#        blank=True, choices=MedalType.choices, max_length=10)
#    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
#    credit = models.DecimalField(max_digits=6, decimal_places=2)
