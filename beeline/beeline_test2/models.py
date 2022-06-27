from django.core.files.storage import FileSystemStorage
from django.db import models

# fs = FileSystemStorage(location='/media')

class ExcelModel(models.Model):
    file = models.FileField(upload_to='')


# посмотреть конфиг из видоса или репы
config = {'conn':'hive'}
class Service(models.Model):
    name = models.CharField(max_length=128, default="Hive-example")
    connection = {'config':config}
    serviceType = models.CharField(max_length=128, default="Hive")


class Database(models.Model):
    name = models.CharField(max_length=128,default="DB_TEST")
    service = models.ForeignKey(Service,on_delete=models.CASCADE)


class Schema(models.Model):
    name = models.CharField(max_length=128, default="default.domain_ess_nfs_dm")
    database = models.ForeignKey(Database, on_delete=models.CASCADE)


class ap_ap_invoices_all(models.Model):
    columns = ["Description", "Service", "Field", "Table Name"]
    Description = models.CharField(max_length=128,default='Table description')
    Service = models.ForeignKey(Service, on_delete=models.CASCADE)
    Field = models.CharField(max_length=128)
    Table_Name = models.CharField(max_length=128)

    