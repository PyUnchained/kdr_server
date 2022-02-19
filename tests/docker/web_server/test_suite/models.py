from django.db import models

class TestModel(models.Model):
    char_field = models.CharField(max_length=120)
    integer_field = models.InterField()
    float_field = models.FloatField()
    boolean_field = models.BooleanField(default=False)
    date_time_field = models.DateTimeField(auto_now_add=True)
    date_field = models.DateField(auto_now_add=True)
    fk_field = models.ForeignKey('sample_django_app.FKTestModel', models.SET_NULL,
        null = True, blank = True)
    m2m_field = models.ManyToManyField('sample_django_app.M2MTestModel')

class M2MTestModel(models.Model):
    char_field = models.CharField(max_length=120)

class FKTestModel(models.Model):
    char_field = models.CharField(max_length=120)