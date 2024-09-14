from django.contrib import admin
from .models import Person, Volunteer, Contact, Cause, Donate, work, Donations, Event, EventImage
# Register your models here.
admin.site.register(Person)
admin.site.register(Volunteer)
admin.site.register(Contact)
admin.site.register(Cause)
admin.site.register(Donate)
admin.site.register(work)
admin.site.register(Donations)



class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 1  # Number of extra fields for images

class EventAdmin(admin.ModelAdmin):
    inlines = [EventImageInline]

admin.site.register(Event, EventAdmin)

