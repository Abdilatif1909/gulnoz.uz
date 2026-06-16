from .models import Project


def get_total_projects():
    return Project.objects.count()


def get_open_projects():
    return Project.objects.filter(status=Project.Status.OPEN).count()


def get_completed_projects():
    return Project.objects.filter(status=Project.Status.COMPLETED).count()
