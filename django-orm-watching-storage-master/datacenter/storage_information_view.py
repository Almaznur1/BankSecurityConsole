from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    # Программируем здесь
    visits = Visit.objects.filter(leaved_at=None)[0]
    who_entered = Visit.passcard.get_object
    non_closed_visits = [
        {
            'who_entered': visits.passcard.owner_name,
            'entered_at': visits.entered_at,
            'duration': Visit.format_duration(Visit.get_duration(visits)),
            'is_strange': '',
        }
    ]
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
