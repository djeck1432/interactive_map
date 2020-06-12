from django.core.management.base import BaseCommand, CommandError
from afisha.models import Place,PlaceImage
from io import BytesIO
import requests



class Command(BaseCommand):
    help = 'Put in the link on json file with description of place'

    def add_arguments(self, parser):
        parser.add_argument('load_place', help='Add link to json file')

    def download_image(self,urls,place_title):
        place = Place.objects.get(title=place_title)
        image_name = place.title.replace(' ', '_')
        for num, url in enumerate(urls):
            response = requests.get(url)
            response_image = BytesIO(response.content)
            new_image_object = place.place_images.create(place=place,position=num)
            new_image_object.image.save(f'{image_name}_{num}', response_image, save=True)


    def handle(self,*args,**options):
        url = options['load_place']
        try:
            response = requests.get(url)
            if response.status_code in [200,201]:
                place_info = response.json()
                place_images = place_info['imgs']
                place_title = place_info['title']
                Place.objects.get_or_create(
                    title=place_title,
                    description_short=place_info['description_short'],
                    description_long=place_info['description_long'],
                    long=place_info['coordinates']['lng'],
                    lat=place_info['coordinates']['lat'],
                )
                self.download_image(place_images, place_title)
        except requests.exceptions.MissingSchema:
            print(f'Perhaps you meant http://{url}')



