from django.db import models
from django.contrib.postgres.fields import ArrayField
from location_field.models.plain import PlainLocationField
from users.models import ExtendedUser,CreationTimeStamp


class Customer(CreationTimeStamp):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(CreationTimeStamp):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    location = models.CharField(max_length=300, blank=True)
    no_of_data_collectors = models.PositiveSmallIntegerField(default=0)
    budget = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return self.name

class Survey(CreationTimeStamp):
    STATUS_CHOICES = (
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="ACTIVE")
    data_collectors = models.ManyToManyField(ExtendedUser)

    def __str__(self):
        return self.name

class Question(CreationTimeStamp):
    QUESTION_TYPES = (
        ('CHOICE', 'Choice'),
        ('OPEN', 'Open'),
        ('MEDIA', 'Media'),
    )

    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    has_multiple_answers = models.BooleanField(default=False)
    is_dependent = models.BooleanField(default=False)
    dependent_question = models.JSONField(null=True)
    is_required = models.BooleanField(default=True)
    type = models.CharField(choices=QUESTION_TYPES, max_length=30)
    options = ArrayField(models.CharField(max_length=300, blank=True), null=True)
    audio_url = models.URLField(null=True)
    image_url = models.URLField(null=True)
    video_url = models.URLField(null=True)

    def __str__(self):
        return self.title

class QuestionAnswer(CreationTimeStamp):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    responses = ArrayField(models.CharField(max_length=300, blank=True))
    location = PlainLocationField(based_fields=['city'], zoom=7, blank=True)

    def __str__(self):
        return f"Answer for {self.question} is ({self.responses})"

    class Meta:
        ordering = ['-created_at']

        