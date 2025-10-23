from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_title = 'Conference Management 25/26'
admin.site.site_header = 'Conference Management 25/26'
admin.site.index_title = 'Conference Management 25/26'     


@admin.action(description="Mark as payed")
def marked_as_payed(modeladmin, request, queryset):
    queryset.update(payed=True)

@admin.action(description="Mark as accepted")
def mark_as_accepted(modeladmin, request, queryset):
     queryset.update(status="accepted")

""""admin.site.register(CONFERENCE)"""
@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('submission_id', 'title', 'status', 'payed', 'created_at', 'updated_at')
    search_fields = ('title', 'status', 'payed')
    list_filter = ('status', 'payed')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')
    fieldsetes = {
        "Information general": {
            "fields": ("title", "abstract", "keywords")
        },
        "document": {
            "fields": ("paper", "user", "conference")
        },
        "Status": {
            "fields": ("status", "payed")
        }
    }

        
    def save(self, *args, **kwargs):
        if not self.Submission_id:
            newid = generate_submission_id()
            while Submission.objects.filter(Submission_id=newid).exists():
                newid = generate_submission_id()
            self.Submission_id = newid
        super().save(*args, **kwargs)   
    actions = [marked_as_payed,mark_as_accepted]



class SubmissionInline(admin.StackedInline):
    model = Submission
    extra = 1
    readonly_fields =("submission_date",)

@admin.register(Conference)
class CONFERENCEpersonalization(admin.ModelAdmin):
    list_display = ('name', 'description', 'theme', 'location', 'start_date', 'end_date', 'created_at', 'updated_at','duration')
    ordering = ('start_date', 'end_date')
    list_filter = ('name','theme')
    search_fields = ('name', 'theme')
    date_hierarchy = 'start_date'
    fieldsets = (
        ("information general",{
            "fields":('conference_id','name','theme','description')
        }),
        ("logistic info",{
            "fields":('location','start_date','end_date')
        }),
    )
    readonly_fields = ('conference_id',)
    def duration(self, obj):
        if obj.start_date and obj.end_date:
            return (obj.end_date - obj.start_date).days
        return "RAS"
    duration.short_description = "Duration (days)"
    inlines = [SubmissionInline]