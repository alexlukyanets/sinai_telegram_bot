from django.shortcuts import render
from django.db.models.functions import TruncDay, TruncMonth, TruncYear
from django.db.models import Count
from .models import TelegramUser
from datetime import datetime, timedelta
import json

def user_activity_view(request):
    now = datetime.now()
    last_month = now - timedelta(days=30)
    last_year = now - timedelta(days=365)

    # Format these querysets to convert datetime objects to strings
    def format_queryset(queryset):
        return [
            {'date': item['date'].strftime('%Y-%m-%d'), 'count': item['count']}
            for item in queryset
        ]

    new_users_month = format_queryset(TelegramUser.objects.filter(created_at__gte=last_month)
                                      .annotate(date=TruncDay('created_at'))
                                      .values('date')
                                       .annotate(count=Count('tg_user_id'))
                                      .order_by('date'))

    new_users_year = format_queryset(TelegramUser.objects.filter(created_at__gte=last_year)
                                     .annotate(date=TruncMonth('created_at'))
                                     .values('date')
                                      .annotate(count=Count('tg_user_id'))
                                     .order_by('date'))

    activity_day = format_queryset(TelegramUser.objects.annotate(date=TruncDay('updated_at'))
                                   .values('date')
                                    .annotate(count=Count('tg_user_id'))
                                   .order_by('date'))

    activity_month = format_queryset(TelegramUser.objects.annotate(date=TruncMonth('updated_at'))
                                     .values('date')
                                      .annotate(count=Count('tg_user_id'))
                                     .order_by('date'))

    activity_year = format_queryset(TelegramUser.objects.annotate(date=TruncYear('updated_at'))
                                    .values('date')
                                     .annotate(count=Count('tg_user_id'))
                                    .order_by('date'))

    context = {
        'new_users_month': json.dumps(new_users_month),
        'new_users_year': json.dumps(new_users_year),
        'activity_day': json.dumps(activity_day),
        'activity_month': json.dumps(activity_month),
        'activity_year': json.dumps(activity_year),
    }

    if request.path == '/user-activity/':
        return render(request, 'user_activity_list.html', context)
    return render(request, 'user_activity_graph.html', context)
