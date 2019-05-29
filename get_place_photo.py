import base64

def get_place_photo(photo_refer):
    api = "https://maps.googleapis.com/maps/api/place/photo?maxwidth={width}&photoreference={photo_refer}&key={key}"

    MapAPI = 'AIzaSyCOoFPnodxekD07cJpKh8tz0GNoU9_tyGU'

    img_file = api.format(width = 400, photo_refer = photo_refer, key = MapAPI)

    print(type(img_file))
    # b64 = base64.encodestring(open(img_file, 'rb').read())

    # return b64


if __name__ == '__main__':
    print("It's test...")
    photo_refer ='CmRaAAAAKyMhpS7btJkC2Ib2NBYumW87-yUndtyT7AJHjl2u5f9o7gjvNrXbjhZdDLgmbp2i8QnM16oXcUWhv5AKfWpts1r79HTK65TRoWFgSWKTKs_4shnrAO_SfxELeu06MnvlEhCES08ug5LpeCwL7EOu1t-nGhSNbcL3ewyFEcakawKBCqATQ-y8Qw'
    # place = get_place_photo(photo_refer)
    print(get_place_photo(photo_refer))
