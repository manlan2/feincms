"""
This introduces a new page type, which has no content of its own but inherits
all content from the linked page.
"""

from django.db import models
from django.utils.translation import ugettext_lazy as _

from feincms.models import ContentProxy


def register(cls, admin_cls):
    cls.add_to_class('symlinked_page', models.ForeignKey('self', blank=True, null=True,
        verbose_name=_('symlinked page'),
        help_text=_('All content is inherited from this page if given.')))

    def content(self):
        if not hasattr(self, '_content_proxy'):
            if self.symlinked_page:
                self._content_proxy = ContentProxy(self.symlinked_page)
            else:
                self._content_proxy = ContentProxy(self)

        return self._content_proxy

    setattr(cls, 'content', property(content))
