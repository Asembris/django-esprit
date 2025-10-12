from django.contrib import admin
from django.utils import dates

# Register your models here.
from .models import Conference,Submission
#admin.site.register(Conference)
admin.site.register(Submission)

#admin.site.title="gestion de conférences 25/26"
#admin.site.header="gestion conférences"
#admin.site.index_title="django app conference"


class SubmissionInline(admin.StackedInline):
    model=Submission
    extra=1
    readonly_fields=("submission_date",)





@admin.register(Conference)
class AdminConferenceModel(admin.ModelAdmin):
    list_display=('name','theme','start_date','end_date','duration')
    ordering=("start_date",)
    search_fields=('name',) 
    fieldsets=(
        ("informations generales",{
            "fields":('name','theme','description')
        }),
        ("logistiques info",{
            "fields":("location","start_date","end_date")
        }),
    )
    def duration(self,objet):
        if objet.start_date and objet.end_date:
            return (objet.end_date-objet.start_date).days
        return 'rien a afficher'
    duration.short_description="duree en jours"
    inline=[SubmissionInline]

        
