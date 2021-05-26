from django.contrib import admin
from .models import (
                CountryBaseInfo,
                CountryAssignment,
                CountryFiles,
                CountyLinkDirectory,
                AnnualCountryLinkDirectory,
                QuarterCountryLinkDirectory,
                MonthCountryLinkDirectory,
                )

admin.site.register(CountryBaseInfo)
admin.site.register(CountryAssignment)
admin.site.register(CountryFiles)
admin.site.register(CountyLinkDirectory)
admin.site.register(AnnualCountryLinkDirectory)
admin.site.register(QuarterCountryLinkDirectory)
admin.site.register(MonthCountryLinkDirectory)