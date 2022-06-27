import re
from django import views
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .forms import ExcelForm
from .injection import (post_database, post_db_schema, post_db_service,
                        post_db_table, post_team)
from .models import ExcelModel


class UploadView(generic.TemplateView):
    model = ExcelModel
    template_name ='templates/inj.html'

    def get(self, request):
        form = ExcelForm
        return render(request, 'index.html', {'form': form})


    def injection(self,request, pk):
        file = get_object_or_404(ExcelModel, pk=pk)
        post_team(file)
        post_db_service(file)
        post_database(file)
        post_db_schema(file)
        post_db_table(file)
        return render(request, 'inj.html')


    def post(self, request,pk):
        if request.method == 'POST':
            form = ExcelForm(request.POST, request.FILES)
            if form.is_valid():
                upload = request.FILES['file']
                fss = FileSystemStorage('media/docs')
                fss.save(upload.name, upload)
                if ExcelModel.objects.filter(file = request.file).exists:
                    file = get_object_or_404(ExcelModel, pk=pk)
                    self.injection(request, file.pk)
            return render(request, 'ty.html')
        return render(request, 'index.html')


    
