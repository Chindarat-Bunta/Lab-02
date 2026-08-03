from django.db import models
from django.urls import reverse

# Create your models here.
# st_id, fname, lname


class Students(models.Model):

    st_id = models.CharField(max_length=12, unique=True)
    fname = models.CharField(max_length=100, blank=False)
    lname = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.fname + " " + self.lname

    def get_absolute_url(self):
        return reverse("Student_detail", kwargs={"pk": self.pk})

