from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import CertificateAuthority, Company, Task, Skill, Certificate, Category, Profession, Job, UserStory, Introduction, Expertise, User, Project, Resume

class CertificateAuthorityAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

class CompanyAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

class TaskAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

class SkillAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

class CertificateAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

class CategoryAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

class ProfessionAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

class JobAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

class UserStoryAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

class IntroductionAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

class ExpertiseAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

class UserAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

class ProjectAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

class ResumeAdmin(ImportExportMixin, admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(CertificateAuthority, CertificateAuthorityAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Profession, ProfessionAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(UserStory, UserStoryAdmin)
admin.site.register(Introduction, IntroductionAdmin)
admin.site.register(Expertise, ExpertiseAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Resume, ResumeAdmin)