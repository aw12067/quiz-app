from django.db import models

class Poll(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=30,default='')
    option_two = models.CharField(max_length=30,default='')
    option_three = models.CharField(max_length=30,default='')     
    option_four = models.CharField(max_length=30,default='')    
    correct_option = models.CharField(max_length=30)
    answer = models.CharField(max_length=30,default='')

    def total(self):
        return self.question

