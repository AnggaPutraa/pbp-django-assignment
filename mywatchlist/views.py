from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import WatchItem

def show_my_watch_list(request):
    obj = WatchItem.objects
    data = obj.all()
    status = obj.filter(
        watched = True
    ).count() > obj.filter(
        watched = False
    ).count()

    return render(
        request,
        'mywatchlist.html',
        {
            'name' : 'Angga',
            'student_id': 2106650065,
            'status': 
                'Selamat, kamu sudah banyak menonton!' if status 
                else 'Wah, kamu masih sedikit menonton!',
            'watchList' : data,
        }
    )

def show_my_wishlist_html(request):
    obj = WatchItem.objects
    data = obj.all()
    status = obj.filter(
        watched = True
    ).count() > obj.filter(
        watched = False
    ).count()

    return render(
        request,
        'mywatchlist.html',
        {
            'name' : 'Angga',
            'student_id': 2106650065,
            'status': 
                'Selamat, kamu sudah banyak menonton!' if status 
                else 'Wah, kamu masih sedikit menonton!',
            'watchList' : data,
        }
    )

def show_my_watchlist_json(request):
    data = WatchItem.objects.all()

    return HttpResponse(
        serializers.serialize("json", data), 
        content_type="application/json"
    )

def show_my_watchlist_xml(request):
    data = WatchItem.objects.all()

    return HttpResponse(
        serializers.serialize("xml", data),
        content_type="application/xml"
    )
