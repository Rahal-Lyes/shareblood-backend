from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid



class TableConfig(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    endpoint = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_("Endpoint"),
        help_text=_("Identifiant unique pour ce tableau (ex: 'projects', 'users')")
    )
    display_name = models.CharField(
        max_length=255,
        verbose_name=_("Display Name"),
        help_text=_("Nom lisible du tableau (ex: 'Liste des projets')")
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Description"),
        help_text=_("Description du tableau pour les utilisateurs")
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Table Configuration")
        verbose_name_plural = _("Table Configurations")

    def __str__(self):
        return self.display_name

class HeaderConfig(models.Model):
    class Meta:
        verbose_name = _("Header Configuration")
        verbose_name_plural = _("Header Configurations")
        unique_together = ('table', 'key')  # anciennement (endpoint, key)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    table = models.ForeignKey(
        TableConfig,
        on_delete=models.CASCADE,
        related_name="headers",
        verbose_name=_("Table"),
        help_text=_("Tableau auquel appartient cette configuration d'en-tête")
    )

    key = models.CharField(
        max_length=255,
        verbose_name=_("Field Key"),
        help_text=_("Clé du champ (ex: 'start_date')")
    )

    display_name = models.CharField(
        max_length=255,
        verbose_name=_("Display Name"),
        help_text=_("Nom d'affichage pour l'en-tête")
    )

    help_text = models.TextField(
        verbose_name=_("Help Text"),
        blank=True,
        null=True,
        help_text=_("Description du champ")
    )

    field_type = models.CharField(
        max_length=50,
        verbose_name=_("Field Type"),
        default="text",
        help_text=_("Type de données (text, date, boolean, etc.)")
    )

    sortable = models.BooleanField(
        default=True,
        verbose_name=_("Sortable"),
        help_text=_("Peut être trié ou non")
    )

    visible = models.BooleanField(
        default=True,
        verbose_name=_("Visible"),
        help_text=_("Visible par défaut dans le tableau")
    )

    width = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_("Width"),
        help_text=_("Largeur de la colonne (ex: '150px')")
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Order"),
        help_text=_("Ordre d'affichage dans le tableau")
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.table.endpoint} - {self.display_name}"

    def to_dict(self):
        return {
            "value": self.key,
            "display_name": self.display_name,
            "help_text": self.help_text,
            "type": self.field_type,
            "sortable": self.sortable,
            "visible": self.visible,
            "width": self.width
        }
