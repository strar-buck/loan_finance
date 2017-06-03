from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import fileinput,io
from loan.models import Document
from loan.forms import DocumentForm
import os
import pandas as pd
import sys,subprocess
from tabula import read_pdf_table

# uploadig pdf and processing it
def upload_pdf(request):
	 # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc_name=str(newdoc.docfile)
            newdoc_df=read_pdf_table(newdoc_name,guess=False)
            print newdoc_df
            newdoc.save()	

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('loan:list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'home.html',
        {'documents': documents, 'form': form}
)

