from django.db import models
from datetime import datetime

# constants
THIS_YEAR = datetime.today().year


class AdmissionTest(models.Model):
    name = models.CharField(max_length=100, unique=True)
    acronym = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.name
    

class QuestionMeta(models.Model):
    has_appeared = models.BooleanField(default=False)
    has_passage = models.BooleanField(default=False)


class Appearance(models.Model):
    meta = models.OneToOneField(QuestionMeta, on_delete=models.CASCADE)
    YEAR_CHOICES = [(str(yr), str(yr)) 
                    for yr in range(THIS_YEAR, THIS_YEAR-41, -1)]
    admission_test = models.ForeignKey(AdmissionTest, on_delete=models.CASCADE)
    unit = models.CharField(max_length=10)
    year = models.CharField(max_length=10, choices=YEAR_CHOICES)
    
    def appearance_label_str(self):
        return f'{self.admission_test.acronym} Unit-{{self.unit}} {self.year}'


class Passage(models.Model):
    meta = models.OneToOneField(QuestionMeta, on_delete=models.CASCADE)
    text = models.TextField(default='Passage Text')


class Question(models.Model):
    meta = models.ForeignKey(QuestionMeta, on_delete=models.CASCADE)
    text = models.TextField(default='Question Text')
    
    def get_correct_answer(self):
        for option in self.options.all():
            if option.is_correct: return option


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.TextField(default='Option Text')
    is_correct = models.BooleanField(default=False)


class Explanation(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE)
    text = models.TextField(default='Explanation Text')
