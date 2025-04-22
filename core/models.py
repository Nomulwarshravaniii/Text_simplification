from django.db import models

class SimplificationCount(models.Model):
    total_simplifications = models.IntegerField(default=0)

    def __str__(self):
        return f"Total Simplifications: {self.total_simplifications}"

class ModelSelectionCount(models.Model):
    MODEL_CHOICES = [
        ('model1', 'Gloss Model'),
        ('model2', 'Overlapping Model'),
        ('model3', 'OpenAI ChatGPT'),
    ]
    model_name = models.CharField(max_length=10, choices=MODEL_CHOICES, unique=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.model_name} - {self.count}"
