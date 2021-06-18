from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=60)
    imgpath = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Branch(models.Model):
    latitude = models.CharField(max_length=60)
    longtitude = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    branch_course = models.ForeignKey('Course', related_name='branches', null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Branches'

    def __str__(self):
        return self.address


class Contact(models.Model):
    CONTACT_CHOICES = (
        ("1", "PHONE"),
        ("2", "FACEBOOK"), 
        ("3", "EMAIL"),   
    )
    type = models.CharField(
        max_length = 20,
        choices = CONTACT_CHOICES,
        default = '1'
        )
    value = models.CharField(max_length = 60)
    contact_course = models.ForeignKey('Course',related_name='contacts', null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.value

    

class Course(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=60)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    logo = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.name


