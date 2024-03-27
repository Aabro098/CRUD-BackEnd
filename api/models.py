from django.db import models

class Note(models.Model):
    title = models.CharField(max_length = 30)
    body = models.TextField()
    created = models.DateField(auto_now_add = True)

    def __str__(self):
        return f"{self.title} (Created: {self.created}, Updated: {self.updated}): body: {self.body[:40]}" 

    class Meta():
        ordering = ['-created'] 