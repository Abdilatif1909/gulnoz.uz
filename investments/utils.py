from django.db.models import Sum

from .models import Investment


def get_total_investments():
    return Investment.objects.count()


def get_open_investments():
    return Investment.objects.filter(status=Investment.Status.OPEN).count()


def get_total_required_amount():
    return Investment.objects.aggregate(total=Sum('required_amount'))['total'] or 0
