from django.contrib.staticfiles.templatetags.staticfiles import static
from django.template.loader import render_to_string
from django.template.defaultfilters import date, pluralize, urlize
from django.conf import settings

from jingo import register
from jinja2 import Markup


static = register.function(static)
register.filter(date)
register.filter(pluralize)
register.filter(urlize)


@register.function
def field_with_attrs(bfield, **kwargs):
    """Allows templates to dynamically add html attributes to bound
    fields from django forms.

    Taken from bedrock.
    """
    bfield.field.widget.attrs.update(kwargs)
    return bfield


@register.function
def field_errors(field):
    """Return string with rendered template with field errors."""
    return Markup(render_to_string('form-error.html', {'field': field}))


@register.function
def get_full_url(path):
    return '{0}{1}'.format(settings.SITE_URL, path)
