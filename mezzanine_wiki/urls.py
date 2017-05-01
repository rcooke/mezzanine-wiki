from django.conf.urls import url
from mezzanine_wiki import views as wikiviews

# Wiki patterns.
urlpatterns = [
    url("^$", wikiviews.wiki_index, name="wiki_index"),
    url("^pages/$", wikiviews.wiki_page_list, name="wiki_page_list"),
    url("^pages:new/$", wikiviews.wiki_page_new, name="wiki_page_new"),
    url("^pages:changes/$", wikiviews.wiki_page_changes, name="wiki_page_changes"),
    url("^tag:(?P<tag>.*)/$", wikiviews.wiki_page_list, name="wiki_page_list_tag"),
    url("^category:(?P<category>.*)/$", wikiviews.wiki_page_list,
                                              name="wiki_page_list_category"),
    url("^author:(?P<username>.*)/$", wikiviews.wiki_page_list,
                                              name="wiki_page_list_author"),
    url("^(?P<slug>.*)/history/$", wikiviews.wiki_page_history,
                                              name="wiki_page_history"),
    url("^(?P<slug>.*)/history/(?P<rev_id>\d+)/$", wikiviews.wiki_page_revision,
                                              name="wiki_page_revision"),
    url("^(?P<slug>.*)/diff/$", wikiviews.wiki_page_diff,
                                              name="wiki_page_diff"),
    url("^(?P<slug>.*)/revert/(?P<revision_pk>[0-9]+)/$", wikiviews.wiki_page_revert,
                                              name="wiki_page_revert"),
    url("^(?P<slug>.*)/undo/(?P<revision_pk>[0-9]+)/$", wikiviews.wiki_page_undo,
                                              name="wiki_page_undo"),
    url("^(?P<slug>.*)/edit/$", wikiviews.wiki_page_edit, name="wiki_page_edit"),
    url("^(?P<slug>.*)/$", wikiviews.wiki_page_detail, name="wiki_page_detail"),
]
