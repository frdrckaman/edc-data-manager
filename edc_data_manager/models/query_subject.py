from edc_registration.models import RegisteredSubject


class QuerySubject(RegisteredSubject):
    class Meta:
        proxy = True
        default_permissions = ("view",)
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"
