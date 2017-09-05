# -*- coding: utf-8 -*-
from schematics.types import StringType
from zope.interface import implementer

from openregistry.api.models.common import BaseResourceItem
from openregistry.api.interfaces import IORContent


class IResource(IORContent):
    """ Marker interface for dummy test resource """


@implementer(IResource)
class DummyTestResource(BaseResourceItem):
    resourceType = StringType(default="basic")
