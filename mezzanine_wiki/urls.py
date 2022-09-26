from django.urls import re_path
from mezzanine_wiki import views as wikiviews

# Wiki patterns.
urlpatterns = [
    re_path("^$", wikiviews.wiki_index, name="wiki_index"),
    re_path("^pages/$", wikiviews.wiki_page_list, name="wiki_page_list"),
    re_path("^pages:new/$", wikiviews.wiki_page_new, name="wiki_page_new"),
    re_path("^pages:changes/$", wikiviews.wiki_page_changes, name="wiki_page_changes"),
    re_path("^tag:(?P<tag>.*)/$", wikiviews.wiki_page_list, name="wiki_page_list_tag"),
    re_path("^category:(?P<category>.*)/$", wikiviews.wiki_page_list,
                                              name="wiki_page_list_category"),
    re_path("^author:(?P<username>.*)/$", wikiviews.wiki_page_list,
                                              name="wiki_page_list_author"),
    re_path("^(?P<slug>.*)/history/$", wikiviews.wiki_page_history,
                                              name="wiki_page_history"),
    re_path("^(?P<slug>.*)/history/(?P<rev_id>\d+)/$", wikiviews.wiki_page_revision,
                                              name="wiki_page_revision"),
    re_path("^(?P<slug>.*)/diff/$", wikiviews.wiki_page_diff,
                                              name="wiki_page_diff"),
    re_path("^(?P<slug>.*)/revert/(?P<revision_pk>[0-9]+)/$", wikiviews.wiki_page_revert,
                                              name="wiki_page_revert"),
    re_path("^(?P<slug>.*)/undo/(?P<revision_pk>[0-9]+)/$", wikiviews.wiki_page_undo,
                                              name="wiki_page_undo"),
    re_path("^(?P<slug>.*)/edit/$", wikiviews.wiki_page_edit, name="wiki_page_edit"),
    re_path("^(?P<slug>.*)/$", wikiviews.wiki_page_detail, name="wiki_page_detail"),
]
