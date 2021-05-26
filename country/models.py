from django.db import models
from employees.models import User


# Create your models here.
class CountryBaseInfo(models.Model):
    SECTION = (
        ("1", "SECTION A"),
        ("2", "SECTION B"),
        ("3", "SECTION C"),
    )

    class Meta:
        verbose_name_plural = 'CountryBaseInfo(s)'

    country_code = models.CharField(max_length=2, primary_key=True, unique=True)
    country_name = models.CharField(max_length=70)
    country_section = models.CharField(max_length=1, choices=SECTION, default="1")

    def __str__(self):
        return str(self.country_code)


class CountryAssignment(models.Model):
    class Meta:
        verbose_name_plural = 'CountryAssignment(s)'

    country_code = models.OneToOneField(CountryBaseInfo, on_delete=models.CASCADE)
    country_actual = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='actual')
    country_shadow1 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='shadow1')
    country_shadow2 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='shadow2')
    country_shadow3 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='shadow3')

    def __str__(self):
        return str(self.country_code)


class CountryFiles(models.Model):
    class Meta:
        verbose_name_plural = 'CountryFiles'

    FILE_TYPE = (
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
        ("D", "D"),
        ("E", "E"),
        ("F", "F"),
    )

    country_code = models.ForeignKey(CountryBaseInfo, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=1, choices=FILE_TYPE, default="A")

    def __str__(self):
        name = (str(self.country_code) + '-' + str(self.file_type))
        return (str(name))


class CountyLinkDirectory(models.Model):
    class Meta:
        verbose_name_plural = 'CountyLinkDirectory(s)'
        ordering = ['-country_code']

    FREQUENCY = (
        ("1", "ANNUALLY"),
        ("2", "QUARTERLY"),
        ("3", "MONTHLY"),
        ("4", "WEEKLY"),
    )

    country_code = models.ForeignKey(CountryBaseInfo, on_delete=models.CASCADE)
    file_type = models.ForeignKey(CountryFiles, on_delete=models.CASCADE)
    remarks = models.CharField(max_length=100)
    isMarco = models.BooleanField(default=False)
    column_update = models.CharField(max_length=100, blank=True, null=True)
    topic = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    def __str__(self):
        return str(self.country_code) + "-" + str(self.id)


class AnnualCountryLinkDirectory(CountyLinkDirectory):
    class Meta:
        verbose_name = "Annual Country LinkDirectory"
        verbose_name_plural = 'Annual Country LinkDirectory'

    year_1 = models.DateField(blank=True, null=True)
    year_2 = models.DateField(blank=True, null=True)
    year_3 = models.DateField(blank=True, null=True)
    year_4 = models.DateField(blank=True, null=True)
    year_5 = models.DateField(blank=True, null=True)
    year_6 = models.DateField(blank=True, null=True)
    year_7 = models.DateField(blank=True, null=True)
    year_8 = models.DateField(blank=True, null=True)
    year_9 = models.DateField(blank=True, null=True)


class QuarterCountryLinkDirectory(CountyLinkDirectory):
    class Meta:
        verbose_name = "Quarter Country LinkDirectory"
        verbose_name_plural = 'Quarter Country LinkDirectory'

    quarter_1 = models.DateField(blank=True, null=True)
    quarter_2 = models.DateField(blank=True, null=True)
    quarter_3 = models.DateField(blank=True, null=True)
    quarter_4 = models.DateField(blank=True, null=True)
    quarter_5 = models.DateField(blank=True, null=True)
    quarter_6 = models.DateField(blank=True, null=True)
    quarter_7 = models.DateField(blank=True, null=True)
    quarter_8 = models.DateField(blank=True, null=True)
    quarter_9 = models.DateField(blank=True, null=True)
    quarter_10 = models.DateField(blank=True, null=True)
    quarter_11 = models.DateField(blank=True, null=True)
    quarter_12 = models.DateField(blank=True, null=True)
    quarter_13 = models.DateField(blank=True, null=True)
    quarter_14 = models.DateField(blank=True, null=True)


class MonthCountryLinkDirectory(CountyLinkDirectory):
    class Meta:
        verbose_name = "Month Country LinkDirectory"
        verbose_name_plural = 'Month Country LinkDirectory'

    month_1 = models.DateField(blank=True, null=True)
    month_2 = models.DateField(blank=True, null=True)
    month_3 = models.DateField(blank=True, null=True)
    month_4 = models.DateField(blank=True, null=True)
    month_5 = models.DateField(blank=True, null=True)
    month_6 = models.DateField(blank=True, null=True)
    month_7 = models.DateField(blank=True, null=True)
    month_8 = models.DateField(blank=True, null=True)
    month_9 = models.DateField(blank=True, null=True)
    month_10 = models.DateField(blank=True, null=True)
    month_11 = models.DateField(blank=True, null=True)
    month_12 = models.DateField(blank=True, null=True)
    month_13 = models.DateField(blank=True, null=True)
    month_14 = models.DateField(blank=True, null=True)
    month_15 = models.DateField(blank=True, null=True)
    month_16 = models.DateField(blank=True, null=True)
    month_17 = models.DateField(blank=True, null=True)
    month_18 = models.DateField(blank=True, null=True)
    month_19 = models.DateField(blank=True, null=True)
    month_20 = models.DateField(blank=True, null=True)
    month_21 = models.DateField(blank=True, null=True)
    month_22 = models.DateField(blank=True, null=True)
    month_23 = models.DateField(blank=True, null=True)
    month_24 = models.DateField(blank=True, null=True)

