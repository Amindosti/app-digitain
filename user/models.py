from django.db import models
from django.contrib.auth.models import AbstractUser


POSITION_CHOICES =( 
    ("DEALER", "DEALER"), 
    ("PITBOSS", "PITBOSS"), 
    ("FLOOR_MANAGER", "FLOOR_MANAGER"), 
    ("SHUFFLER", "SHUFFLER"), 
    ("TEAM_MANAGER", "TEAM_MANAGER"), 
)

SHIFT_CHOICES = {
    "FIX": [
        ("MORNING", "Morning"),
        ("MIDDLE", "Middle"),
        ("NIGHT", "Night")
    ],
    "NORMAL": [
        ("ANNA", "Anna"),
        ("BILLY", "Billy"),
        ("CICI", "Cici"),
        ("DIDI", "Didi"),
        ("EDI", "Edi")
    ]
}

WORKING_LINE_CHOICES =(
    ("NETWORK", "NETWORK"),
    ("DEDICATED", "DEDICATED"),
    ("TOTO", "TOTO"),
    ("RUSSIAN", 'RUSSIAN'),
    ("BACCARAT", "BACCARAT"),
)

class User(AbstractUser):
    
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=20, choices=POSITION_CHOICES, default="DEALER", blank=False, help_text="your working position")
    online = models.BooleanField(default=False)
    shift_type = models.CharField(max_length=20 ,choices=SHIFT_CHOICES, default="NORMAL", blank=False)
    #shift_working = models.CharField(max_length=20,choices=SHIFT_CHOICES, blank=False)
    address = models.CharField(max_length=25, blank=False)
    line = models.CharField(max_length=20, choices=WORKING_LINE_CHOICES, default="NETWORK", blank=False)


def __str__(self):
    return self.name