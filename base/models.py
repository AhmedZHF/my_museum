
from django.db import models
from django.contrib.auth.models import User
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

CHOICES =(
    ("Tunis","TUNIS"),
    ("Monastir","MONASTIR"),
    ("Gabes","GABES"),
    ("Medenin","MEDENIN"),
    ("Sousse","SOUSSE"),
    ("Binzert","BINZERT"),
    ("Sfax","SFAX"),
    ("Tozeur","TOZEUR"),
    ("Tataouine","TATAOUINE"),
    ("Mahdia","MAHDIA"),
    ("Kairouan","KAIROUAN"),
    ("BenArous","BENAROUS"),
    ("Gafsa","GAFSA"),
    ("Jandouba","JANDOUBA"),
    ("El kef","ELKEF"),
    ("Ariana","ARIANA"),
    ("Kasserine","KASERINE"),
    ("SidiBouzid","SIDIBOUZID"),
    ("beja","BEJA"),
    ("Zagouen","ZAGOUEN"),
    ("seliana","SELIANA"),
    ("kebili","KEBILI"),
    ("Manouba","MANOUBA"),
    ("Nabeul","NABEUL")
)

class Museum(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    location=models.CharField(null=True, max_length=20, choices=CHOICES)
    image= models.ImageField(null=True, upload_to="images/")
    lien=models.URLField(max_length=200,null=True)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name




class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Museum, on_delete=models.CASCADE)

    body = models.TextField(null=True)
    rate = models.TextField(null=True)
    image= models.ImageField( null=True, blank=True,upload_to="images/")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body
