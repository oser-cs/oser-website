"""Projects admin configuration."""

from django.contrib import admin

from dynamicforms.views import download_multiple_forms_entries
from dynamicforms.models import Form
from .models import Edition, Participation, Project, EditionForm
from django.contrib.admin import SimpleListFilter
from profiles.models import Student


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Admin panel for projects."""

    list_display = ('__str__', 'logo', 'num_editions', 'last_edition',
                    'total_accepted_participations')

    def num_editions(self, obj: Project) -> int:
        """Return the number of editions."""
        return obj.editions.count()
    num_editions.short_description = "Éditions"

    def last_edition(self, obj: Project) -> int:
        """Return the year of the last edition."""
        return obj.editions.latest().year
    last_edition.short_description = 'Année de la dernière édition'

    def total_accepted_participations(self, obj: Project) -> int:
        """Return total number of accepted participations."""
        return obj.total_participations(state=Participation.STATE_ACCEPTED)
    total_accepted_participations.short_description = 'Participations totales'


class OrganizersInline(admin.TabularInline):
    """Inline for edition organizers."""

    model = Edition.organizers.through
    extra = 0


class SchoolFilter(admin.SimpleListFilter):
    title = 'établissement'
    parameter_name = 'profiles__school'

    def lookups(self, request, model_admin):
        list_of_school = []
        query = Student.objects.values_list(
            "school", flat=True).distinct()
        for school in query:
            list_of_school.append((school, school))
        return list_of_school

    def queryset(self, request, queryset):
        if self.value():
            emails = Student.objects.filter(
                school=self.value()).values_list("user__email", flat=True)
            return queryset.filter(user__email__in=emails)


@ admin.register(Edition)
class EditionAdmin(admin.ModelAdmin):
    """Admin panel for editions."""

    list_display = ('project', 'year',
                    'num_pending', 'num_validated', 'num_accepted',
                    'num_rejected', 'num_cancelled')
    list_filter = ('project', 'year',)
    inlines = (OrganizersInline,)

    def num_pending(self, obj: Edition) -> int:
        """Return number of pending participations."""
        return obj.participations.pending().count()
    num_pending.short_description = 'En attente'

    def num_validated(self, obj: Edition) -> int:
        """Return number of validated participations."""
        return obj.participations.validated().count()
    num_validated.short_description = 'Validés'

    def num_accepted(self, obj: Edition) -> int:
        """Return number of accepted participations."""
        return obj.participations.accepted().count()
    num_accepted.short_description = 'Acceptés'

    def num_rejected(self, obj: Edition) -> int:
        """Return number of rejected participations."""
        return obj.participations.rejected().count()
    num_rejected.short_description = 'Refusés'

    def num_cancelled(self, obj: Edition) -> int:
        """Return number of cancelled participations."""
        return obj.participations.cancelled().count()
    num_cancelled.short_description = 'Annulés'


@ admin.register(EditionForm)
class EditionFormAdmin(admin.ModelAdmin):
    """Admin panel for edition forms."""

    list_display = ('form', 'deadline', 'recipient',)
    list_filter = ('edition', 'deadline',)


@ admin.register(Participation)
class ParticipationAdmin(admin.ModelAdmin):
    """Participation admin panel."""

    list_display = ('user', 'edition', 'submitted', 'state')
    list_filter = (SchoolFilter,
                   'edition', 'submitted', 'state',)
    readonly_fields = ('submitted',)
    search_fields = ('user__first_name', 'user__last_name', 'user__email',)
