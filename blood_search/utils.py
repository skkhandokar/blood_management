

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginationProject(request, projects, results):
    page = request.GET.get('page')
    paginator = Paginator(projects, results)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)

    leftIndex = (int(page) - 3)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page)+5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages+1

    custom_range = range(leftIndex, rightIndex)
    return custom_range, projects
