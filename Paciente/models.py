from django.db import models

class MedicalApointment(models.Model):
    id = models.AutoField(primary_key=True)
    cui = models.ForeignKey('Paciente', on_delete=models.DO_NOTHING)
    doctor = models.ForeignKey('Doctor', on_delete=models.DO_NOTHING)
    date = models.DateField()
    hour = models.TimeField()
    reason = models.CharField(max_length=200)
    observations = models.TextField()
    prescription = models.TextField()
    status = models.CharField(max_length=20, default='Pendiente', choices=[('Pendiente', 'Pendiente'), ('Atendido', 'Atendido')])

    class Meta:
        verbose_name = ""
        verbose_name_plural = "s"
        constraints = [
            models.UniqueConstraint(fields=['cui', 'doctor', 'date', 'hour'], name='unique_cui_doctor_date_hour')
        ]
    
    def __str__(self):
        return f"{self.cui} - {self.doctor} - {self.date} - {self.hour} - {self.reason} - {self.status}"
                              

class Doctor(models.Model):
    cui = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    country = models.CharField(max_length=50)

    class Meta:
        verbose_name = ""
        verbose_name_plural = "s"
        constraints = [
            models.UniqueConstraint(fields=['cui', 'name'], name='unique_cui_name_doctor')
        ]

    def __str__(self):
        return self.name


# Create your models here.
class Paciente(models.Model):
    cui = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    

    class Meta:
        verbose_name = ""
        verbose_name_plural = "s"
        constraints = [
            models.UniqueConstraint(fields=['cui', 'name'], name='unique_cui_name_patient')
        ]

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})