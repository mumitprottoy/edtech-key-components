from django.contrib import admin
from .models import (
    AdmissionTest,
    QuestionMeta,
    Appearance,
    Passage,
    Question,
    Option,
    Explanation
) 


@admin.register(AdmissionTest)
class AdmissionTestAdmin(admin.ModelAdmin):
    list_display = ('name', 'acronym')


admin.site.register((
    QuestionMeta,
    Appearance,
    Passage,
    Question,
    Option,
    Explanation
) )
