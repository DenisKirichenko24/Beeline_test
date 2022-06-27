import re
from django import views
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.views import generic

from .forms import ExcelForm
from .injection import (post_database, post_db_schema, post_db_service,
                        post_db_table, post_team)
from .models import ExcelModel


class UploadView(generic.TemplateView):
    model = ExcelModel


    def get(self, request):
        form = ExcelForm
        return render(request, 'index.html', {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = ExcelForm(request.POST, request.FILES)
            if form.is_valid():
                upload = request.FILES['file']
                fss = FileSystemStorage('media/docs')
                fss.save(upload.name, upload)
                post_team()
                post_db_service()
                post_database()
                post_db_schema()
                post_db_table()
            return render(request, 'ty.html')
        return render(request, 'index.html')


    
