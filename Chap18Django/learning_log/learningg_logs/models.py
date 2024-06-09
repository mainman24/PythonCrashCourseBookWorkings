from django.db import models

# Create your models here.


class Topic(models.Model):

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Entry(models.Model):
    # many to one relationship between entry and topic
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)
    text = models.TextField()  # no char limit
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[0:50] + '...'
