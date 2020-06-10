from django.shortcuts import render,get_object_or_404
from .models import Place
from django.http import HttpResponse,Http404,JsonResponse
import json
from django.urls import reverse

def get_places_info(request):
    places = Place.objects.all()
    places_descriptions= []
    places_info = {"type": "FeatureCollection","features":places_descriptions}
    for place in places:
        places_descriptions.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",

                    "coordinates": [place.long,place.lat]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": reverse(place_detail_view,args=[place.id]),
                }
            }
        )
    context = {'places_info':places_info}
    return render(request,'index.html',context)

def place_detail_view(request,place_id):
    place = get_object_or_404(Place,pk=place_id)
    images = [place_image.image.url for place_image in place.place_images.all()]
    place_description = {
        'title': place.title,
        'imgs':images,
        'description_short':place.description_short,
        'description_long':place.description_long,
        'coordinates':{
            'lng':place.long,
            'lat':place.lat,
        }
    }
    return JsonResponse(place_description, safe=False)


