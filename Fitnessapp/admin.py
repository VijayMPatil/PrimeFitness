from django.contrib import admin
from .models import Contact,Enrollment,Trainer,MembershipPlan,Attendance,Gallery

# Register your models here.
admin.site.register(Contact)
admin.site.register(MembershipPlan)
admin.site.register(Trainer)
admin.site.register(Enrollment)
admin.site.register(Attendance)
admin.site.register(Gallery)