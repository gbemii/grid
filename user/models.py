from django.db import models

# Create your models here.


class Personal_info(models.Model):
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
	blocked=models.CharField(max_length=222)

	def __str__(self):
		return self.firstname



class Investment_scheme(models.Model):
	name_of_scheme= models.CharField(max_length=222)
	user_id= models.CharField(max_length=222)
	order_id= models.CharField(max_length=222)
	capital_invested= models.IntegerField()
	investment_status= models.CharField(max_length=222)
	monthly_profit= models.CharField(max_length=222)
	net_profit= models.CharField(max_length=222)
	total_return= models.CharField(max_length=222)
	profit_earned= models.CharField(max_length=222)
	term_of_scheme= models.CharField(max_length=222)
	term_begins= models.CharField(max_length=222)
	term_ends= models.CharField(max_length=222)
	order_date= models.CharField(max_length=222)
	approved_date= models.CharField(max_length=222)
	payment_method= models.CharField(max_length=222)
	payment_status= models.CharField(max_length=222)
	conversion_fee= models.CharField(max_length=222)
	approval=models.CharField(max_length=222)


	def __str__(self):
		return self.name_of_scheme


class Account(models.Model):
	user_id =models.CharField(max_length=225)
	available_funds= models.CharField(max_length=222)
	invested_funds= models.CharField(max_length=222)
	account_balance= models.IntegerField()
	total_profit= models.CharField(max_length=222)
	open_postions= models.CharField(max_length=222)



	def __str__(self):
		return self.user_id


class Transactions(models.Model):
	transaction_id =models.CharField(max_length=225)
	user_id=models.CharField(max_length=222)
	transaction_type= models.CharField(max_length=222)
	amount= models.IntegerField()
	date= models.CharField(max_length=222)
	approval=models.CharField(max_length=222)


	def __str__(self):
		return self.transaction_id

class Kyc_user_info(models.Model):
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



# class Farms(models.Model):
# 	farm_id =models.CharField(max_length=225)
# 	farm_name= models.CharField(max_length=222)
# 	monthly_interest= models.CharField(max_length=222)
# 	terms= models.CharField(max_length=222)
# 	roi= models.CharField(max_length=222)
# 	apy= models.CharField(max_length=222)
# 	farm_description= models.CharField(max_length=222)



# 	def __str__(self):
# 		return self.farm_id

