from django.db import models

class Topic(models.Model):
    # Topic that the user wants to discuss about
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Reply(models.Model):
    # Reply to a specific topic
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'replies'

    def __str__(self):
        return f"{self.text}"