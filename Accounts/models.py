from django.db import models
from django.contrib.auth.models import AbstractUser, User

# # Create your models here.

class User(AbstractUser):
	is_admin = models.BooleanField(default=False)
	is_client = models.BooleanField(default=False)
	blocked=models.BooleanField(default=False)
	phone_number= models.CharField(blank=True, max_length=2555)
	date_of_birth= models.CharField(blank=True, max_length=255)
	address_line1= models.CharField(blank=True, max_length=255)
	address_line2= models.CharField(blank=True, max_length=255)
	state=models.CharField(blank=True, max_length=20)
	city=models.CharField(blank=True, max_length=20)
	nationality=models.CharField(blank=True, max_length=20)
	# document_upload= models.FileField(upload_to='uploads', blank=True)
	telegram_username=models.CharField(blank=True, max_length=222)
	
	def __str__(self):
		return str(self.id)


# ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
# ('password', models.CharField(max_length=128, verbose_name='password')),
# ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
#   ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
#   ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
#   ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
#   ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
#    ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
#      ( 'is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
#   ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
#   ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
#    ('is_admin', models.BooleanField(default=False)),
#    ('is_user', models.BooleanField(default=False)),
#    ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
#   ('user_permissions', models



	