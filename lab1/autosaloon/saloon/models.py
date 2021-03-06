from django.db import models

# Create your models here.

class Position(models.Model):
	name = models.CharField(max_length=50),
	salary = models.IntegerField(default=0),
	duties = models.TextField(max_length=1000),
	requirments = models.TextField(max_length=1000),


class Employee(models.Model):
	name = models.CharField(max_length=150),
	age = models.IntegerField(default=0),
	sex = models.CharField(max_length=10),
	address = models.CharField(max_length=150),
	phone = models.CharField(max_length=20),
	passport = models.CharField(max_length=200),
	position = models.ForeignKey(Position, on_delete=models.CASCADE),


class Manufacturer(models.Model):
	name = models.CharField(max_length=150),
	country = models.CharField(max_length=50),
	address = models.CharField(max_length=150),
	description = models.TextField(max_length=1000),
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE),


class Additional_equipment(models.Model):
	name = models.CharField(max_length=50),
	characteristics = models.TextField(max_length=1000),
	price = models.IntegerField(default=0),


class Body_type(models.Model):
	name = models.CharField(max_length=150),
	description = models.TextField(max_length=1000),


class Car(models.Model):
	mark = models.CharField(max_length=50),
	manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE),
	body_type = models.ForeignKey(Body_type, on_delete=models.CASCADE),
	date = models.DateField(auto_now=True),
	color = models.CharField(max_length=50),
	body_code = models.CharField(max_length=50),
	engin_code = models.CharField(max_length=50),
	characteristics = models.TextField(max_length=1000),
	code1 = models.CharField(max_length=50),
	code2 = models.CharField(max_length=50),
	code3 = models.CharField(max_length=50),
	price = models.IntegerField(default=0),
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE),


class Customer(models.Model):
	name = models.CharField(max_length=150),
	address = models.CharField(max_length=150),
	phone = models.CharField(max_length=20),
	passport = models.CharField(max_length=200),
	car = models.ForeignKey(Car, on_delete=models.CASCADE),
	order_date = models.DateField(auto_now=True),
	sale_date = models.DateField(auto_now=True),
	execution_notes = models.TextField(max_length=1000),
	payment_notes = models.TextField(max_length=1000),
	paied = models.IntegerField(default=0),
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE),

