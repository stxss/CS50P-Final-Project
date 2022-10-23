import googlemaps
import pprint
import random
import csv
from tabulate import tabulate
import sys

#INSERT API KEY - edited mine for privacy reasons
API_KEY = ""
gmaps = googlemaps.Client(key=API_KEY)

"""main : function that executes the program"""


def main():
    location = input("\nEnter desired location: ")
    coordinates = place_get(location)
    attraction_tailor = attraction_select(coordinates)
    result_attr = get_attraction(*attraction_tailor)
    final = final_result(*result_attr)
    print(final)
    search_again()


"""place_get : function that gets the desired location coordinates"""


def place_get(location):
    places_result = gmaps.places(location)

    coords_to_str = list(places_result["results"][0]["geometry"]["location"].values())
    return f"{coords_to_str[0]}, {coords_to_str[1]}"


"""
place_nearby: function that retrieves nearby places based on the users input of location, \
              radius of search and type of establishment/attraction. \
              If not specified, will randonly define an attraction type per google API
"""


def attraction_select(coords):

    radius = 0
    while True:

        try:
            radius = input("Enter desired radius (in km): ")
            if radius != "":
                radius = int(radius)
                radius *= 1000
            elif radius == "":
                radius = 20000

            break
        except ValueError:
            print("\nPlease, insert a number")
            continue

    attraction_types = ["accounting","airport","amusement_park","aquarium","art_gallery",
                        "atm","bakery","bank","bar","beauty_salon","bicycle_store","book_store","bowling_alley","bus_station","cafe",
                        "campground","car_dealer","car_rental","car_repair","car_wash","casino","cemetery",
                        "church","city_hall","clothing_store","convenience_store","courthouse","dentist","department_store",
                        "doctor","drugstore","electrician","electronics_store","embassy","fire_station","florist",
                        "funeral_home","furniture_store","gas_station","gym","hair_care","hardware_store",
                        "hindu_temple","home_goods_store","hospital","insurance_agency","jewelry_store","laundry","lawyer",
                        "library","light_rail_station","liquor_store","local_government_office","locksmith","lodging",
                        "meal_delivery","meal_takeaway","mosque","movie_rental","movie_theater","moving_company",
                        "museum","night_club","painter","park","parking","pet_store",
                        "pharmacy","physiotherapist","plumber","police","post_office",
                        "primary_school","real_estate_agency","restaurant","roofing_contractor","rv_park",
                        "school","secondary_school","shoe_store","shopping_mall","spa",
                        "stadium","storage","store","subway_station",
                        "supermarket","synagogue","taxi_stand","tourist_attraction","train_station",
                        "transit_station","travel_agency","university","veterinary_care","zoo"
    ]

    table = []
    with open("/workspaces/93729036/project/attractions.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            table.append(row)
        headers = table[0]
    org_table = tabulate(table[1:], headers, tablefmt="grid")

    while True:
        try:
            attraction = input(
                "\nIf you want to see the possible types of attractions, establishments or services, either type 'attractions' or leave the line blank and press Enter.\
                                    \nIf you don't have a preference and want a completely random selection, type 'random' and press Enter.\n\nType of Attraction: "
            )
            attraction.replace(" ", "_")

            if attraction == "" or attraction == "attractions":
                print(org_table)
                continue
            elif attraction == "random":
                random_attraction = random.choice(attraction_types)
                print(f"{random_attraction} was selected.")
            elif attraction not in org_table:
                print(org_table)
                print(f"Please, enter a valid type of attraction from the table above")
                continue
            else:
                print(f"\n{attraction} was selected.")
            break

        except ValueError:
            continue

    coordinates = str(coords)
    radius = int(radius)
    attraction = str(attraction)

    return coordinates, radius, attraction


def get_attraction(coords, radius, type_of_attraction):
    nearby = gmaps.places_nearby(
        location=str(coords),
        radius=int(radius),
        open_now=False,
        type=type_of_attraction,
    )

    resulting = []

    for i in range(len(nearby["results"])):
        try:
            top_name = nearby["results"][i]["name"]
            top_rating = nearby["results"][i]["rating"]
            user_ratings_total = nearby["results"][i]["user_ratings_total"]
            top_vicinity = nearby["results"][i]["vicinity"]
        except KeyError:
            continue

        resulting.append(
            {
                "name": top_name,
                "rating": top_rating,
                "number of reviews": user_ratings_total,
                "address": top_vicinity,
            }
        )
    print(f"\nFound {len(nearby['results'])} results")
    resulting = list(resulting)
    nearby = dict(nearby)
    attraction = str(type_of_attraction)
    return resulting, nearby, attraction


def final_result(resulting, nearby, type_of_attraction):
    how_many = 0
    while True:
        try:
            how_many = int(
                input("\nHow many places do you want to see?\nEnter a number: ")
            )
            if how_many < 0:
                print("\nPlease, insert a positive number")
                continue
            elif how_many > len(nearby["results"]):
                print("\nPlease, insert a smaller number")
                continue
            break
        except ValueError:
            print("\nPlease, insert a number")
            continue

    while True:
        try:
            choose_sorting = input(
                "Choose your sorting filter. The available filters are: 'Name', 'Rating' and 'Number of Reviews'. The default filter is 'Number of Reviews'.\n"
            ).lower()
            if choose_sorting == "name":
                resulting_sorted = sorted(
                    resulting, key=lambda d: d["name"], reverse=False
                )
            elif choose_sorting == "rating":
                resulting_sorted = sorted(
                    resulting, key=lambda d: d["rating"], reverse=True
                )
            elif choose_sorting == "number of reviews" or choose_sorting == "":
                resulting_sorted = sorted(
                    resulting, key=lambda d: d["number of reviews"], reverse=True
                )
            break
        except ValueError:
            print("\nPlease, insert the filter by which you want to sort")
            continue

    user_results = []

    for i in range(int(how_many)):
        if i == 0:
            statement = f"\nThe most recommended {type_of_attraction} is {resulting_sorted[i]['name']} with a rating of {resulting_sorted[i]['rating']} based on {resulting_sorted[i]['number of reviews']} reviews. This places's address is {resulting_sorted[i]['address']}"
        elif i == 1:
            statement = f"The second most recommended {type_of_attraction} is {resulting_sorted[i]['name']} with a rating of {resulting_sorted[i]['rating']} based on {resulting_sorted[i]['number of reviews']} reviews. This places's address is {resulting_sorted[i]['address']}"
        elif i == 2:
            statement = f"The third most recommended {type_of_attraction} is {resulting_sorted[i]['name']} with a rating of {resulting_sorted[i]['rating']} based on {resulting_sorted[i]['number of reviews']} reviews. This places's address is {resulting_sorted[i]['address']}"
        else:
            statement = f"The next {type_of_attraction} on the list is {resulting_sorted[i]['name']} with a rating of {resulting_sorted[i]['rating']} based on {resulting_sorted[i]['number of reviews']} reviews. This places's address is {resulting_sorted[i]['address']}"
        user_results.append(statement)

    return "\n\n".join(user_results)


def search_again():
    while True:
        ask_user = input("\nDo you want to do another search? [y/n] ")
        if ask_user.lower() == "yes" or ask_user.lower() == "y":
            main()
        elif ask_user.lower() == "no" or ask_user.lower() == "n":
            sys.exit("Thank you! Come back again! :)")
        else:
            continue


if __name__ == "__main__":
    main()