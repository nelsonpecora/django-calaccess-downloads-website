from django.conf.urls import url
from calaccess_website import views, sitemaps


urlpatterns = [
    # The homepage
    url(
        r'^$',
        views.Home.as_view(),
        name="home",
    ),

    # Version archive views
    url(
        r'^downloads/$',
        views.VersionArchiveIndex.as_view(),
        name="version_archive_index",
    ),
    url(
        r'^downloads/(?P<year>[0-9]{4})/$',
        views.VersionYearArchiveList.as_view(),
        name="version_archive_year"
    ),
    url(
        r'^downloads/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$',
        views.VersionMonthArchiveList.as_view(),
        name="version_archive_month"
    ),
    url(
        r'^downloads/latest/$',
        views.LatestVersion.as_view(),
        name='version_latest'
    ),
    url(
        r'^downloads/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/(?P<time>[0-9]{6})/$',
        views.VersionDetail.as_view(),
        name="version_detail"
    ),

    # File views
    url(
        r'^files/$',
        views.FileList.as_view(),
        name='file_list'
    ),
    url(
        r'^files/(?P<slug>[-\w]+)/$',
        views.FileDetail.as_view(),
        name='file_detail',
    ),
    url(
        r'^files/(?P<slug>[-\w]+)/downloads/$',
        views.FileDownloadsList.as_view(),
        name='file_downloads_list',
    ),

    # Form views
    url(
        r'^forms/$',
        views.FormList.as_view(),
        name='form_list'
    ),
    url(
        r'^forms/(?P<id>\w+)/$',
        views.FormDetail.as_view(),
        name='form_detail',
    ),

    # Official documentation
    url(
        r'^government-documentation/$',
        views.GovernmentDocumentation.as_view(),
        name='government_documentation'
    ),

    # Machine-readable stuff
    url(
        r'^robots.txt$',
        views.CalAccessRobotsTxt.as_view(),
        name='robots_txt'
    ),
    url(
        r'^file-sitemap.xml$',
        sitemaps.FileSitemap.as_view(),
        name='file_sitemap'
    ),
    url(
        r'^file-downloads-sitemap.xml$',
        sitemaps.FileDownloadsSitemap.as_view(),
        name='file_downloads_sitemap'
    ),
    url(
        r'^form-sitemap.xml$',
        sitemaps.FormSitemap.as_view(),
        name='form_sitemap'
    ),
    url(
        r'^downloads-sitemap.xml$',
        sitemaps.VersionSitemap.as_view(),
        name='version_sitemap'
    ),
    url(
        r'^downloads-year-sitemap.xml$',
        sitemaps.VersionYearSitemap.as_view(),
        name='version_archive_year_sitemap'
    ),
    url(
        r'^downloads-month-sitemap.xml$',
        sitemaps.VersionMonthSitemap.as_view(),
        name='version_archive_month_sitemap'
    ),
    url(
        r'^other-sitemap.xml$',
        sitemaps.OtherSitemap.as_view(),
        name='other_sitemap'
    ),
]
