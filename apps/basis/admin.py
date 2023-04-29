from django.contrib import admin


class ModelAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_max_show_all = 100
    date_hierarchy = 'addtime'
    
    def get_list_display_links(self, request, list_display) -> set:
        return set(list_display).difference(self.list_editable)
