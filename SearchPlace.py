import requests
import json
import random

def get_request(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    nowlat = request_json['lat']
    nowlng = request_json['lng']
    genre = request_json['type']
    dis = request_json['dis']

    result = search_place(nowlat, nowlng, genre, dis)
    return result

def search_place(nowlat, nowlng, genre, dis):
    #検索ジャンルリスト
    genrefood = ['bakery', 'cafe', 'restaurant']
    genreactive = ['amusement_park', 'campground', 'bowling_alley', 'casino', 'night_club', 'gym', 'park', 'shopping_mall', 'movie_theater']
    genrespot = ['museum', 'aquarium', 'art_gallery']
    typerelax = ['bar', 'clothing_store', 'department_store', 'electronics_store', 'furniture_store', 'hardware_store', 'home_goods_store', 'jewelry_store', 'library', 'pet_store', 'spa', 'store']

    #検索範囲
    if dis == 0:
        radius = 100
    elif dis == 1:
        radius = 200
    elif dis == 2:
        radius = 300

    while(1):
        if genre == 0:
            genre_name = genrefood[random.randrange(len(genrefood))]
        elif genre == 1:
            genre_name = genreactive[random.randrange(len(genreactive))]
        elif genre == 2:
            genre_name = genrespot[random.randrange(len(genrespot))]
        print(genre_name)

        MapAPI = '<API KEY>'
        url_reseach_place = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + str(nowlat)+','+str(nowlng) +'&radius=' + str(radius) + '&type='+str(genre_name)+'&language=ja&key=' + MapAPI

        #types=foodなど、配列などで指定する必要あり
        res_json = requests.get(url_reseach_place)

        # 結果はJSON形式なのでデコードする
        res_dict = json.loads(res_json.text)	#result配列のjson要素を抽出
        if res_dict['status'] =='OK': break;

    print(res_dict)


    #place_list = []
    for x in res_dict['results']:
        place_list = res_dict['results'] #検索結果のplaceを全てlistとして格納
    print(type(place_list))

    '''
    ratingを加味したplaceを提案できるようにする
    （['rating']が謎にerrorを吐くので，一旦stop）0:21:30現在
    highrate_list = []
    for place in res_dict:
        if('rating' in place and place['rating'] >= 2.0):
            highrate_list.append(place)
            print('Name：{}'.format(place['name']))
            print('レート：{}'.format(place['rating']))
    if(len(highrate_list) == 0): highrate_list.append(random.randint(1, len(place_list)) -1)
    fortune_place = random.choice(highrate_list)
    '''
    # print(place_list)

    fortune_place = place_list[random.randrange(len(place_list))]
    print(fortune_place['place_id'])
    #print(fortune_place)
    #print(fortune_place['place_id'])
    result = get_place_info(fortune_place['place_id'])

    return result


def get_place_info(place_id):
    api = "https://maps.googleapis.com/maps/api/place/details/json?&language=ja&placeid={place}&key={key}"

    MapAPI = '<API KEY>'

    url_get_place_info = api.format(place = place_id, key = MapAPI)

    # 実際にAPIにリクエストを送信して結果を取得する
    res_json = requests.get(url_get_place_info)

    # 結果はJSON形式なのでデコードする
    data = json.loads(res_json.text)
    json_dict = data['result']

    print(json)

    name = json_dict['name']
    if 'formatted_phone_number' in json_dict:
        tel = json_dict['formatted_phone_number']
    else:
        tel = 'null'
    address = json_dict['formatted_address']
    if 'opening_hours' in json_dict:
        open_now = str(json_dict['opening_hours']['open_now'])
    else:
        open_now = 'null'
    if 'price_level' in json_dict:
        price_level = json_dict['price_level']
    else:
        price_level = 'null'
    if 'website' in json_dict:
        website = json_dict['website']
    else:
        website = 'null'
    location = json_dict['geometry']['location']

    place_dict = {
        'name': name,
        'tel': tel,
        'address': address,
        'opening_now': open_now,
        'price_level': price_level,
        'website': website,
        'lat': location['lat'],
        'lng': location['lng']
    }

    place_json = json.dumps(place_dict, ensure_ascii=False)

    print(place_json)

    return  place_json

if __name__ == '__main__':
    print("It's test...")
    place = search_place(34.985849, 135.758767, 2, 0)
    # place = search_place(34.702485,135.49595, 0, 0)
    # place = search_place(34.7063096,135.5010824, 0, 0)
    # place_json = get_place_info('ChIJpWEus43mAGARotvu_0tmRjw')

    # print(place)
