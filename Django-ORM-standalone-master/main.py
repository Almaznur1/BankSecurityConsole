import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard, Visit  # noqa: E402
from django.utils.timezone import localtime


if __name__ == '__main__':
    # step1 Count passcards
    # print('Количество пропусков:', Passcard.objects.count())  # noqa: T001

    # step2 Get all passcards
    # cards = Passcard.objects.all()
    # print(cards)

    # step3 Get information about passcard holder
    # cards = Passcard.objects.all()
    # card = cards[0]
    # print(card.owner_name)
    # print(card.passcode)
    # print(card.created_at)
    # print(card.is_active)

    # step4 Get active passcards with for loop
    # cards = Passcard.objects.all()
    # active_passcards = [cards[i] for i in range(len(cards)) if cards[i].is_active]
    # print('Активных пропусков:', len(active_passcards))
    
    # step5 Get active passcards with filter()
    # active_passcards = Passcard.objects.filter(is_active=True)
    # print('Активных пропусков:', len(active_passcards))

    # step8 Get visits
    # visits = Visit.objects.all()
    # print(visits)

    # step9 Who is in vault currently
    # visitors_in_vault = Visit.objects.filter(leaved_at=None)
    # print(visitors_in_vault)

    # step10 Time spent in vault
    visits = Visit.objects.all()
    print('Entered at, MSK: {}\nLocated in vault: {}'.format(
        localtime(visits[0].entered_at),
        visits[0].leaved_at - visits[0].entered_at
        )
    )

    # step11 The names of those who are currently in vault
    visitors_in_vault = Visit.objects.filter(leaved_at=None)
    for i in range(len(visitors_in_vault)):
        print(visitors_in_vault[i].passcard.owner_name)
    all_passcards = Passcard.objects.filter(is_active=True)
    print(all_passcards)