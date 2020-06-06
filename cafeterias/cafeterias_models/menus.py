from django.db import models

import users


class Day(models.Model):
    name = models.CharField(
        max_length=10, 
        choices= (
            ('MON', 'Monday'),
            ('TUE', 'Tuesday'),
            ('WED', 'Wednesday'),
            ('THU', 'Thursday'),
            ('FRI', 'Friday'),
            ('SAT', 'Saturday') ), 
        default='Monday', 
        unique=True )
    
    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField( max_length=100 )
    description = models.CharField( max_length=250 )
    price = models.DecimalField( max_digits=6, decimal_places=2, default=0.00 )
    quantity = models.PositiveIntegerField(default=1)
    vendor = models.ForeignKey(
        'users.User', 
        on_delete=models.CASCADE, 
        limit_choices_to={'is_vendor':True},
    )
    time_created = models.DateTimeField(auto_now=True)
    scheduled_days = models.ManyToManyField('Day', related_name='reoccurs')
    is_reoccurring = models.BooleanField(default=False)
    reoccurring_frequency = models.PositiveIntegerField(default=1)
    
    class Meta:
        ordering = [ 'name' ]
        
    def __str__(self):
        return f"{self.name} ({self.quantity} / NGN {self.price})"
    
    def save(self, *args, **kwargs):
        if int(self.reoccurring_frequency) > 1:
            self.is_reoccurring = True
        else: 
            self.is_reoccurring = False
        super().save(*args, **kwargs)

