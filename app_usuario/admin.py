from django.contrib import admin
from .models import MyUser

def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = "Marcar os selecionados como garantidos do desconto"

@admin.register(MyUser)
class AdminMyUser(admin.ModelAdmin):
    list_display = ('upper_case_name','view_birtday', 'whatsapp', 'email',)
    list_filter = ('birtday','city',('is_staff', admin.BooleanFieldListFilter),)
    search_fields = ['name','birtday','phone']
    actions = [make_published]
    def upper_case_name(self, obj):
        return ("%s" % (obj.name)).upper()

    upper_case_name.short_description = 'Name'

    def view_birtday(self, obj):
        return obj.birtday

    view_birtday.empty_value_display = 'desconhecido'