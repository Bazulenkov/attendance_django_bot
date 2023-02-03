from django.contrib import admin

from attendance.models import Attendance, Course, Group, Schedule, Student


admin.site.register(Attendance)
admin.site.register(Course)
admin.site.register(Group)
admin.site.register(Schedule)
admin.site.register(Student)
