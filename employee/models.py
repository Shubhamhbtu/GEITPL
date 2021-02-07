from django.db import models
from django.utils.translation import gettext_lazy as _


PROJECT_MANAGER = "ProjectManager"
BACKEND_DEVELOPER = "BackendDeveloper"
FRONTEND_DEVELOPER = "FrontendDeveloper"
DESIGNER = "Designer"

Designation = (
    (PROJECT_MANAGER, _('ProjectManager')),
    (BACKEND_DEVELOPER, _('BackendDeveloper')),
    (FRONTEND_DEVELOPER, _('FrontendDeveloper')),
    (DESIGNER, _('Designer')),
)


class Project(models.Model):
    name = models.CharField(_('Project_Name'), max_length=30)
    start_date = models.DateField(_('Start_Date'))
    end_date = models.DateField(_("End_date"))

    def __str__(self):
        return self.name

    @property
    def duration(self):
        duration = (self.end_date - self.start_date).days
        return duration


class Employee(models.Model):
    full_name = models.CharField(_('FullName'), max_length=50)
    address = models.CharField(_('Address'), max_length=100)
    designation = models.CharField(_('Designation'), max_length=30,
                                   choices=Designation,
                                   default=BACKEND_DEVELOPER,
                                   null=True,
                                   blank=True,
                                   db_index=True)
    supervisor = models.ForeignKey('self', null=True,
                                   blank=True,
                                   related_name='employee',
                                   on_delete=models.CASCADE)
    project = models.ManyToManyField(Project, null=True, blank=True,
                                     related_name='employee_project')

    def __str__(self):
        return "{}".format(self.full_name,)

