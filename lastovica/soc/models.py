from django.db import models

# Create your models here.
class Ucitel(models.Model):
    meno = models.CharField(max_length=16)
    priezvisko = models.CharField(max_length=32)
    email = models.EmailField(max_length=254)
    heslo = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Učiteľ"
        verbose_name_plural = "Učitelia"
        ordering = ["priezvisko"]

    def __str__(self) -> str:
        return f"{self.meno} {self.priezvisko}"

class Trieda(models.Model):
    nazov = models.CharField(max_length=7)

    class Meta:
        verbose_name = "Trieda"
        verbose_name_plural = "Triedy"
        ordering = ["nazov"]
    
    def __str__(self) -> str:
        return f"{self.nazov}"


class Student(models.Model):
    meno = models.CharField(max_length=16)
    priezvisko = models.CharField(max_length=32)
    trieda = models.ForeignKey(Trieda, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    heslo = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Študent"
        verbose_name_plural = "Študenti"
        ordering = ["priezvisko"]

    def __str__(self) -> str:
        return f"{self.meno} {self.priezvisko}"

class Odbor(models.Model):
    nazov = models.CharField(max_length=64)

    class Meta:
        verbose_name = "Odbor"
        verbose_name_plural = "Odbory"
        ordering = ["nazov"]

    def __str__(self) -> str:
        return f"{self.nazov}"

class Dostupnost(models.Model):
    nazov = models.CharField(max_length=32)

    class Meta:
        verbose_name = "Dostupnosť"
        verbose_name_plural = "Dostupnosti"
        ordering = ["nazov"]

    def __str__(self) -> str:
        return f"{self.nazov}"

class Tema(models.Model):
    nazov = models.CharField(max_length=64)
    popis = models.TextField()
    konzultant = models.ForeignKey(Ucitel, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, blank=True, null=True, on_delete=models.CASCADE)
    odbor = models.ForeignKey(Odbor, on_delete=models.CASCADE)
    dostupnost = models.ForeignKey(Dostupnost, on_delete=models.CASCADE)
    pocet_konzultacii = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Téma"
        verbose_name_plural = "Témy"
        ordering = ["-dostupnost"]

    def __str__(self) -> str:
        return f"{self.nazov}"
