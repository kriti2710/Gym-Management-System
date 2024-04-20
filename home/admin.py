from django.contrib import admin
from home.models import Registration, Gallery, SubPlan, SubPlanFeature
# Register your models here.
admin.site.register(Registration)
admin.site.register(Gallery)

class SubPlanAdmin(admin.ModelAdmin):
    list_editable=('highligth_status',)
    list_display=('title', 'price', 'highlight_status')
admin.site.register(SubPlan)

class SubPlanFeatureAdmin(admin.ModelAdmin):
    list_display=('title', 'subplan')
admin.site.register(SubPlanFeature)


