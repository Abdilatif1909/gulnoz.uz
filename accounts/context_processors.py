from .utils import get_user_role


def user_role(request):
    role = get_user_role(request.user)
    return {
        'current_role': role,
        'is_admin_role': role == 'ADMIN',
        'is_company_role': role == 'COMPANY',
        'is_investor_role': role == 'INVESTOR',
    }
