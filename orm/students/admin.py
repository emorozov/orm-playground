from django.contrib import admin

from orm.students.models import Status, Cohort, Student, ActivityLog


admin.site.register(Status)
admin.site.register(Cohort)
admin.site.register(Student)
admin.site.register(ActivityLog)
