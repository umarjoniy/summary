from django.contrib import admin
from .models import *


class AdminPerson(admin.ModelAdmin):
    list_display = ('name', 'email', 'website', 'phone')


class AdminEducation(admin.ModelAdmin):
    list_display = ('title', 'name', 'period')


class AdminExperience(admin.ModelAdmin):
    list_display = ('title', 'name', 'period')


class AdminSkills(admin.ModelAdmin):
    list_display = ('name','num', 'is_main', 'lwnum', 'lmnum')


class AdminAwards(admin.ModelAdmin):
    list_display = ('title', 'name', 'period')


class AdminPosts(admin.ModelAdmin):
    list_display = ('author', 'title', 'category', 'created_at', 'is_published')


class AdminComments(admin.ModelAdmin):
    list_display = ('article', 'name', 'email', 'website')


class AdminContact(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'is_solved')


admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Partners)
admin.site.register(Person, AdminPerson)
admin.site.register(Education, AdminEducation)
admin.site.register(Experience, AdminExperience)
admin.site.register(Skills, AdminSkills)
admin.site.register(Awards, AdminAwards)
admin.site.register(Services)
admin.site.register(Projects)
admin.site.register(Another)
admin.site.register(Posts, AdminPosts)
admin.site.register(Comments, AdminComments)
admin.site.register(Contact, AdminContact)
admin.site.register(ServicesText)
