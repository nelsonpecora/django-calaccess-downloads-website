from django.conf.urls import url
from calaccess_website import views


urlpatterns = [
    url(
        r'^$',
        views.VersionArchiveIndex.as_view(),
        name="version_index",
    ),
    url(r'^versions/archive/(?P<year>[0-9]{4})/$',
        views.VersionYearArchiveList.as_view(),
        name="version_year_archive"),
    url(
        r'^versions/(?P<pk>[0-9]{1,})/$',
        views.VersionDetail.as_view(),
        name="version_detail"
    ),
    url(r'^latest/$', views.LatestVersion.as_view(), name='latest'),
    url(
        r'^raw_data_files/$',
        views.RawDataFileList.as_view(),
        name='raw_data_files'
    ),
    url(
        r'^raw_data_files/(?P<file_name>\w+)/$',
        views.RawDataFileDetail.as_view(),
        name='raw_data_file',
    ),
]