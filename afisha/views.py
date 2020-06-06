from django.shortcuts import render
from .models import Places
from django.http import HttpResponse,Http404,JsonResponse
import json
from django.urls import reverse

def get_places_info(request):
    places = Places.objects.all()
    places_descriptions= []
    places_info = {"type": "FeatureCollection","features":places_descriptions}
    for place in places:
        places_descriptions.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",

                    "coordinates": [place.lat, place.long]
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
    try:
        place  = Places.objects.get(pk=place_id)
        images = [place_image.image.url for place_image in place.place_images.all()]
        place_description = {
            'title': place.title,
            'imgs':images,
            'description_short':place.description_short,
            'description_long':place.description_long,
            'coordinates':{
                'lat':place.lat,
                'lng':place.long,
            }
        }
        return HttpResponse(json.dumps(place_description, indent=6,ensure_ascii=False),
                     content_type="application/json")
    except:
        raise Http404("Page not found")

