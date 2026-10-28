from django.db import models

class Student(models.Model):
    addresses = [
        ('KhanYounis', 'Khan Younis'),
        ('Gaza', 'Gaza'),
        ('Rafah', 'Rafah'),
        ('DeirBalah', 'DeirBalah'),
        ('Jabalia', 'Jabalia')
    ]
    std_name = models.CharField(max_length=100)
    std_id = models.CharField(max_length=9, unique=True)
    age = models.PositiveIntegerField()
    date_of_birth = models.DateField()
    address = models.CharField(max_length=30, choices=addresses)
    salary = models.DecimalField(decimal_places=2, max_digits=8)
    photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.std_name

    class Meta:
        ordering = ['std_id']
