# -*- coding: utf-8 -*-

STATUS_CHANGES = {
    "draft": {
        "editing_permissions": ["resource_owner", "Administrator"],
        "next_status": {
            "pending": ["resource_owner", "Administrator"],
        }
    },
    "pending": {
        "editing_permissions": ["resource_owner", "Administrator"],
        "next_status": {
            "draft": ["Administrator"],
            "deleted": ["resource_owner", "Administrator"],
            "verification": ["resource_owner", "Administrator"]
        }
    }
}
