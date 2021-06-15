from django.contrib import admin

from .models import Mat, Dept, CourseReview, Course, AdminMessage


class RecomAdmin(admin.ModelAdmin):
    model = CourseReview
    list_display = ('course', 'recom', 'comment','flag')
    list_filter = ['flag']
    # search_fields = ['comment']


admin.site.register(Mat)
admin.site.register(Dept)
admin.site.register(Course)
admin.site.register(CourseReview,RecomAdmin)
admin.site.register(AdminMessage)
