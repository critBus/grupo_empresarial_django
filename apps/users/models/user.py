from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def save(self, *args, **kwargs):
        if not self.pk:  # Only set staff=True for new users
            self.is_staff = True
        super().save(*args, **kwargs)
