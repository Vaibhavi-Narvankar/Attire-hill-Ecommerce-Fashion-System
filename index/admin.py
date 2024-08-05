from django.contrib import admin
from .models import *
from django.http import HttpResponse
from index.models import ContactForm
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors

def download_pdf(self,request,queryset):
    model_name = self.model.__name__
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename={model_name}.pdf'
    custom_page_width, custom_page_height = 800, 1200  # Custom dimensions in points (1/72 inch)
    custom_pagesize = (custom_page_width, custom_page_height)

    pdf = canvas.Canvas(response,pagesize=custom_pagesize)
    pdf.setTitle('PDF REPORT')

    headers = [field.verbose_name for field in self.model._meta.fields]
    data = [headers]
    
    for obj in queryset:
        data_row = [str(getattr(obj,field.name)) for field in self.model._meta.fields]
        data.append(data_row)

    table = Table(data)
    table.setStyle(TableStyle(
        [
            ('BACKGROUND',(0,0),(-1,0), colors.grey),
            ('GRID',(0,0),(-1,-1),1,colors.black)
        ]

   ))
   
    canvas_width = 600
    canvas_height = 900

    table.wrapOn(pdf, canvas_width,canvas_height)

    table.drawOn(pdf,40,canvas_height-len(data))
    

    pdf.save()
    return response

download_pdf.short_description = "Download Selected items as PDF"


# Register your models here.  added manually


admin.site.register(Product)

@admin.register(Orders)
class ordersinfo(admin.ModelAdmin):
    actions = [download_pdf]
 


@admin.register(SalesReports)
class Salesinfo(admin.ModelAdmin):
    actions = [download_pdf]

# contact form
admin.site.register(ContactForm)
admin.site.register(BilingForm)





