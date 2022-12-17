from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    # Программируем здесь
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for i in range(len(visits)):
        non_closed_visits.append(
            {
                'who_entered': visits[i].passcard.owner_name,
                'entered_at': visits[i].entered_at,
                'duration': Visit.format_duration(Visit.get_duration(visits[i])),
                'is_strange': Visit.is_visit_long(visits[i]),
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
