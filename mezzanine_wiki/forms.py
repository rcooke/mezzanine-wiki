from django import forms
from django.utils.translation import gettext_lazy as _
from mezzanine_wiki.models import WikiPage
from mezzanine.core.models import CONTENT_STATUS_DRAFT

# These fields need to be in the form, hidden, with default values,
# since it posts to the blog post admin, which includes these fields
# and will use empty values instead of the model defaults, without
# these specified.
hidden_field_defaults = ("status", "gen_description", "allow_comments")



class WikiPageForm(forms.ModelForm):
    summary = forms.CharField(label=_("Edit summary"),
                                  max_length=400, required=False)

    class Meta:
        model = WikiPage
        fields = ('title', 'content', 'summary', 'status',)+ hidden_field_defaults

    def __init__(self, *args, **kwargs):
        super(WikiPageForm, self).__init__(*args, **kwargs)
        # Hide title for existing page
        if 'instance' in kwargs:
            del self.fields["title"]
