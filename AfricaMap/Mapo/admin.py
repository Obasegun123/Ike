from django.contrib import admin

from .models import Currency,City,Country,Ethnic,Tourist,CommonReligion,LandMark,Timezone,Demonyms,LanguageName,Culture,CapitalName

# Register your models here.
# class PostImageAdmin(admin.StackedInline):
#     model = Country
# @admin.register(Currency)
# class PostAdmin(admin.ModelAdmin):
#     inlines = [PostImageAdmin]

#     class Meta:
#        model = Currency

admin.site.register([Currency,City,Country,Ethnic,Tourist,CommonReligion,LandMark,Timezone,Demonyms,LanguageName,Culture,CapitalName])
