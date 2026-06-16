from .models import UserProfile


def get_user_role(user):
    if not user.is_authenticated:
        return None
    if user.is_superuser or user.is_staff:
        return UserProfile.Role.ADMIN
    profile, _ = UserProfile.objects.get_or_create(user=user)
    return profile.role


def is_admin(user):
    return get_user_role(user) == UserProfile.Role.ADMIN


def is_company(user):
    return get_user_role(user) == UserProfile.Role.COMPANY


def is_investor(user):
    return get_user_role(user) == UserProfile.Role.INVESTOR
