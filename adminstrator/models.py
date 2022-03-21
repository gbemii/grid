from django.db import models

# Create your models here.


class Admin_info(models.Model):
	firstname =models.CharField(max_length=225)
	surname= models.CharField(max_length=255)
	email= models.CharField(max_length=255)
	phone_number= models.CharField(max_length=2555)
	date_of_birth= models.CharField(max_length=255)
	address_line1= models.CharField(max_length=255)
	address_line2= models.CharField(max_length=255)
	language = models.CharField(max_length=255)
	Password= models.CharField(max_length=222)
	state=models.CharField(max_length=20)
	city=models.CharField(max_length=20)
	nationality=models.CharField(max_length=20)
	document_upload= models.CharField(max_length=2222)
	telegram_username=models.CharField(max_length=222)

	def __str__(self):
		return self.firstname




# class Account(models.Model):
# 	user_id =models.CharField(max_length=225)
# 	available_funds= models.CharField(max_length=222)
# 	invested_funds= models.CharField(max_length=222)
# 	account_balance= models.CharField(max_length=222)
# 	total_profit= models.CharField(max_length=222)
# 	open_postions= models.CharField(max_length=222)



# 	def __str__(self):
# 		return self.user_id


class Farm(models.Model):
	farm_id =models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
	farm_name= models.CharField(max_length=222)
	monthly_interest= models.IntegerField()
	terms= models.IntegerField()
	roi= models.IntegerField()
	apy= models.IntegerField()
	farm_description= models.CharField(max_length=222)



	def __str__(self):
		return self.farm_name

# class Transactions(models.Model):
# 	transaction_id =models.CharField(max_length=225)
# 	user_id=models.CharField(max_length=222)
# 	transaction_type= models.CharField(max_length=222)
# 	amount= models.CharField(max_length=222)
# 	date= models.CharField(max_length=222)
	


# 	def __str__(self):
# 		return self.transaction_id

# class Kyc_user_info(models.Model):
# 	firstname =models.CharField(max_length=225)
# 	surname= models.CharField(max_length=255)
# 	email= models.CharField(max_length=255)
# 	phone_number= models.CharField(max_length=2555)
# 	date_of_birth= models.CharField(max_length=255)
# 	address_line1= models.CharField(max_length=255)
# 	address_line2= models.CharField(max_length=255)
# 	language = models.CharField(max_length=255)
# 	Password= models.CharField(max_length=222)
# 	state=models.CharField(max_length=20)
# 	city=models.CharField(max_length=20)
# 	nationality=models.CharField(max_length=20)
# 	document_upload= models.CharField(max_length=2222)
# 	telegram_username=models.CharField(max_length=222)

# 	def __str__(self):
# 		return self.firstname
