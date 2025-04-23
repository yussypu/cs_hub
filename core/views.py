from django.shortcuts import render, reverse

def landing(request):
    return render(request, 'core/landing.html')

def index(request):
    return render(request, 'core/index.html')

def course_matrix(request):
    return render(request, 'core/course_matrix.html')

def period_view(request, year, period):
    if year == 2 and period == 5:
        sections = [
            {
                "name": "Logic and Modelling",
                "notes_url": reverse("logic_notes"),
                "practice_url": "#",
                "exam_url": "#"
            },
            {
                "name": "Databases",
                "notes_url": reverse("databases_notes"),
                "practice_url": "#",
                "exam_url": "#",
                "topics": [
                    {"name": "Introduction", "url": reverse("databases_intro")},
                ]
            },
            {
                "name": "Discrete Math and Calc",
                "notes_url": "#",
                "practice_url": "#",
                "exam_url": "#"
            },
            {
                "name": "Information Management",
                "notes_url": reverse("info_management_notes"),
                "practice_url": "#",
                "exam_url": "#"
            },
        ]
    else:
        sections = []

    return render(request, "core/period.html", {
        "year": year,
        "period": period,
        "sections": sections
    })

def logic_notes(request):
    return render(request, 'core/logic_notes.html')

def databases_notes(request):
    return render(request, 'core/databases_notes.html')

def databases_intro(request):
    return render(request, 'core/databases_intro.html')

def info_management_notes(request):
    return render(request, 'core/information_management_notes.html')

def info_management_information_systems(request):
    return render(request, "core/info_management_information_systems.html")