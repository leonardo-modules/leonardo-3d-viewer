# -#- coding: utf-8 -#-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from leonardo.module.web.models import Widget
from leonardo.module.web.widgets.forms import WidgetUpdateForm
from constance.forms import JsonField
from leonardo.module.media.fields import FileField


class ModelForm(WidgetUpdateForm):

    file = FileField()
    extra = JsonField(required=False)


class ModelViewerWidget(Widget):

    feincms_item_editor_form = ModelForm

    file = models.ForeignKey("media.File", verbose_name=_(
        "3d model"), related_name="%(app_label)s_%(class)s_related")

    image = models.ForeignKey("media.File", verbose_name=_(
        "Image"),
        help_text="fallback for browsers which does not support webgl",
        related_name="%(app_label)s_%(class)s_image_related",
        blank=True, null=True)

    shadows = models.BooleanField(verbose_name=_('Shadows?'), default=True)
    antialias = models.BooleanField(verbose_name=_('Antialias?'), default=True)

    animation_speed = models.CharField(
        max_length=255, verbose_name=_("animation speed"), default='0.0005')

    background_color = models.CharField(
        max_length=255, verbose_name=_("background color"), default='0xffffff')

    color = models.CharField(
        max_length=255, verbose_name=_("color"), default='0xfdd017',
        help_text=_("color for model"))

    model_ambient = models.CharField(
        max_length=255, verbose_name=_("model ambient"), default='0xFBB917',
        help_text=_("abient factor for model"))

    position = models.CharField(
        max_length=255, verbose_name=_("position"), default='0, -0.25, 0.6',
        help_text=_("position x,y,z"))

    rotation = models.CharField(
        max_length=255, verbose_name=_("rotation"),
        default='0, - Math.PI / 2, 0',
        help_text=_("rotation x,y,z"))

    scale = models.CharField(
        max_length=255, verbose_name=_("scale"), default='1',
        help_text=_("scale of model"))

    camera_position = models.CharField(
        max_length=255, verbose_name=_("camera position"),
        default='3, 0.5, 3',
        help_text=_("camera position x,y,z"))

    ambient_light = models.CharField(
        max_length=255, verbose_name=_("ambient color"), default='0x736F6E',
        help_text=_("abient light color"))

    extra = models.TextField(verbose_name=_("extra"), blank=True)

    @property
    def get_scale(self):
        return float(self.scale)

    @property
    def speed(self):
        return float(self.animation_speed)

    class Meta:
        abstract = True
        verbose_name = _("3d model")
        verbose_name_plural = _('3d models')
