# -*- coding: utf-8 -*-
#
# Copyright (C) 2020 CERN.
# Copyright (C) 2020 Northwestern University.
#
# Invenio-RDM-Records is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Record response serializers."""

from .csl import CSLJSONSerializer, StringCitationSerializer
from .datacite import DataCite43JSONSerializer
from .ui import UIJSONSerializer

__all__ = (
    "CSLJSONSerializer",
    "DataCite43JSONSerializer",
    "StringCitationSerializer",
    "UIJSONSerializer",
)
