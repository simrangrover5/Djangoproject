from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.
class AddUser(models.Model):
	FirstName = models.CharField(max_length=100)
	LastName = models.CharField(max_length=100)
	Email = models.EmailField(max_length=100,unique=True)
	Password = models.CharField(max_length=30)

	def __str__(self):
		return f"{self.Email}"


class Uimage(models.Model):
	Sender = models.ForeignKey(to=AddUser,on_delete=models.CASCADE,null=True,related_name="sender")
	Receiver = models.ForeignKey(to=AddUser,on_delete=models.CASCADE,related_name="receiver")
	Description = models.TextField()
	Pic = models.ImageField(upload_to="static/images") 

	def __str__(self):
		return f"{self.Receiver}"

class Ufiles(models.Model):
	Sender1 = models.ForeignKey(to=AddUser,on_delete=models.CASCADE,null=True,related_name="sender1")
	Receiver1 = models.ForeignKey(to=AddUser,on_delete=models.CASCADE,related_name="receiver1")
	Description1 = models.TextField()
	File = models.FileField(validators=[FileExtensionValidator('pdf')])

	def __str__(self):
		return f"{self.Receiver1}"
