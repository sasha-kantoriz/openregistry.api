# -*- coding: utf-8 -*-
from openregistry.api.adapters import ContentConfigurator
from .constants import STATUS_CHANGES


class DummyTestResourceConfigurator(ContentConfigurator):
    """ Testing resource configuration adapter """

    name = "Test Resource configurator"
    model = None
    available_statuses = STATUS_CHANGES
