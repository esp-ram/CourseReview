from django.db import models
import numpy as np
import datetime


class Dept(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Mat(models.Model):
    name = models.CharField(max_length = 150)
    dep = models.ForeignKey(Dept, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length = 100)
    mat = models.ForeignKey(Mat, on_delete=models.CASCADE)

    def average_recs(self):
        try:
            total = 0
            upp = 0
            for i in self.coursereview_set.all():
                total += 1
                upp += i.recom
            avg = upp/total
            return avg*100
        except:
            return -1

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class CourseReview(models.Model):
    RECOM_CHOICES = (
        (1, 'SI'),
        (0, 'NO'),
    )

    CUATR_CHOICES = (
        (1, '1C'),
        (2, '2C'),
    )

    YEAR_CHOICES = ((r,r) for r in range(2010, datetime.date.today().year+1))

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    comment = models.CharField(max_length = 1000)
    year = models.IntegerField(('year'), choices = YEAR_CHOICES, default=datetime.datetime.now().year)
    cuatr = models.IntegerField(choices = CUATR_CHOICES)
    recom = models.IntegerField(choices = RECOM_CHOICES)
    flag = models.IntegerField(default = 0)



class AdminMessage(models.Model):
    mensaje = models.CharField(max_length=1000)
    date = models.DateTimeField('date published')
