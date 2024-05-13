from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Review


class WordFilter(admin.SimpleListFilter):
    title = "Filter by words!"
    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("elon", "Tweets with Elon"),
            ("no_elon", "Tweets without Elon"),
        ]

    def queryset(self, request, tweets):
        likes = self.value()
        if likes == "elon":
            return tweets.filter(payload__contains="Elon Musk")
        elif likes == "no_elon":
            return tweets.exclude(payload__contains="Elon Musk")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "payload",
    )

    list_filter = (
        WordFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )
