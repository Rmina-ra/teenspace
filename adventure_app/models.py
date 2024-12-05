from django.db import models
from pytils.translit import slugify
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# мои добавления
from django.contrib.auth.models import User

class Category(models.Model):
    image = models.ImageField(blank=True, upload_to='image')
    name = models.CharField("Название категории", max_length=255)
    slug = models.SlugField(unique=True, editable=False, blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
class Vakanсy(models.Model):
    name = models.CharField("Название компании", max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Выберите категорию")
    author = models.CharField("Работодатель", max_length=255)
    cost = models.CharField("Зарплата", max_length=150)
    phone = models.CharField("Номер телефона", max_length=17)
    course = models.URLField("Ссылка на курсы", max_length=500)

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('parent', 'Родитель'),
        ('child', 'Ребенок'),
        ('employer', 'Работодатель'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='customuser_groups',
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='customuser_permissions',
        blank=True
    )

class ChildProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='child_profile')
    parent = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='children', limit_choices_to={'role': 'parent'})
    school_name = models.CharField(max_length=100)
    grade = models.IntegerField()

# мои добавления
class Task(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'В процессе'),
        ('completed', 'Завершена'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='owned_tasks', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, related_name='assigned_tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title    