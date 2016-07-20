from calaccess_raw import get_model_list
from bakery.views import BuildableListView
from calaccess_raw.models import RawDataVersion
from calaccess_raw.annotations.filing_forms import all_filing_forms


class AbstractSitemapClass(BuildableListView):
    def render_to_response(self, context):
        return super(AbstractSitemapClass, self).render_to_response(
            context,
            content_type='text/xml'
        )


class OtherSitemapView(AbstractSitemapClass):
    build_path = "other-sitemap.xml"
    template_name = "calaccess_website/other-sitemap.xml"
    queryset = [
        {"url": "/"},
        {"url": "/forms/"},
        {"url": "/files/"},
        {"url": "/versions/"},
        {"url": "/versions/latest/"},
        {"url": "/government-documentation/"},
    ]


class VersionSitemapView(AbstractSitemapClass):
    """
    A machine-readable list of all version detali pages.
    """
    build_path = 'version-sitemap.xml'
    template_name = 'calaccess_website/version-sitemap.xml'
    model = RawDataVersion


class FileSitemapView(AbstractSitemapClass):
    """
    A machine-readable list of all file detail pages.
    """
    build_path = 'file-sitemap.xml'
    template_name = 'calaccess_website/file-sitemap.xml'
    queryset = get_model_list()


class FormSitemapView(AbstractSitemapClass):
    """
    A machine-readable list of all form detail pages.
    """
    build_path = 'file-sitemap.xml'
    template_name = 'calaccess_website/form-sitemap.xml'
    queryset = all_filing_forms
