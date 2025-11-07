from django.contrib import admin
from general.models import User
from django.contrib.auth.models import Group
from rangefilter.filters import DateRangeFilter
from django_admin_listfilter_dropdown.filters import ChoiceDropdownFilter
from general.models import (
    Post,
    User,
    Comment,
    Reaction,
)
from general.filters import AuthorFilter, AutocompleteFilter, PostFilter


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "username",
        "email",
        "is_staff",
        "is_superuser",
        "is_active",
        "date_joined",
    )
    fields = (
        "first_name",
        "last_name",
        "username",
        "password",
        "email",
        "is_staff",
        "is_superuser",
        "is_active",
        "friends",
        "date_joined",
        "last_login",
    )
    readonly_fields = (
        "date_joined",
        "last_login",
    )
    # search_fields = (
    #     "id",
    #     "username",
    #     "email",
    # )
    list_filter = (
        "is_staff",
        "is_superuser",
        "is_active",
        ("date_joined", DateRangeFilter),
    )


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "author",
        "title",
        "body",
        "created_at",
    )
    readonly_fields = (
        "created_at",
    )
    search_fields = (
        "id",
        "title",
        "author__username",
    )
    list_filter = (
        AuthorFilter,
        ("created_at", DateRangeFilter),
    )
    
    def get_body(self, obj):
        max_length = 64
        if len(obj.body) > max_length:
            return obj.body[:61] + "..."
        return obj.body
    
    get_body.short_description = "body"
    
    def get_comment_count(self, obj):
        return obj.comments.count()


@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "body",
        "author",
        "post",
        "created_at",
    )
    
    list_display_links = (
        "id",
        "body",
    )
    search_fields = (
        AuthorFilter,
        PostFilter,
    )


@admin.register(Reaction)
class ReactionModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "value",
        "author",
        "post",
    )
    list_filter = (
        PostFilter,
        AuthorFilter,
        ("value", ChoiceDropdownFilter),
    )


admin.site.unregister(Group)
# admin.site.register(User)