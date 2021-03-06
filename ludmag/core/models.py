from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from smart_selects.db_fields import ChainedManyToManyField

from django import forms

# Curso : Kinder-Primaria-Secundaria-COMIPEMS
class Curso(models.Model):
    name = models.CharField(max_length=11)
    def __str__(self):
        return "%s" % self.name

#Plan : Basico-Avanzado-Premium-None
class Plan(models.Model):
    name = models.CharField(max_length=20)
    curso= models.ForeignKey(Curso, on_delete=models.CASCADE)
    def __str__(self):
        return "%s" % self.name
#Grado : 1ero-2do-3ro-4to .. .. Semanal-Fin de Semana
class Grado(models.Model):
    name = models.CharField(max_length=30)
    curso= models.ForeignKey(Curso, on_delete=models.CASCADE)
    def __str__(self):
        return "%s" % self.name

class ClientePotencial(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length = 254) 
    phone = models.CharField(max_length=17)
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    grado = ChainedForeignKey(
        "Grado",
        chained_field="curso",
        chained_model_field="curso",
        show_all=False,
        auto_choose=True,
    )
 
    plan = ChainedForeignKey(
        "Plan",
        chained_field="curso",
        chained_model_field="curso",
        show_all=False,
        auto_choose=True,
    )
    
  
    def __str__(self):
        return "%s" % self.name

def image_upload_location(instance,filename):
    teacher_name = instance.name
    path = str("teachers/".format(teacher_name,filename))
    print(path)
    return path
    


class ProfesorResume(models.Model):
    name = models.CharField(max_length=100,verbose_name = "Nombre")
    paternal_surname= models.CharField(max_length=100,verbose_name = "Apellido Paterno")
    maternal_surname= models.CharField(max_length=100,verbose_name = "Apellido Materno")
    description = models.CharField(max_length=100,verbose_name = "Rol")
    urlImage = models.ImageField(upload_to='teachers/',verbose_name = "Foto de Perfil")
    phrase = models.CharField(max_length=254)
    def __str__(self):
        return "%s" % self.name

   
class Paragraph(models.Model):
    profesor = models.ForeignKey(ProfesorResume, on_delete=models.CASCADE)
    description= models.TextField()

    