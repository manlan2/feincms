# flake8: noqa
from __future__ import absolute_import, unicode_literals

import warnings

from feincms.contents import TemplateContent

warnings.warn(
    'Import TemplateContent from feincms.contents.',
    DeprecationWarning, stacklevel=2)
