from project import *


def test_place_get():
   assert place_get("porto") == "41.1579438, -8.629105299999999"
   assert place_get("new york") == "40.7127753, -74.0059728"
   assert place_get("sydney") == "-33.8688197, 151.2092955"
   assert place_get("tokyo") == "35.6761919, 139.6503106"


def test_attraction_select():
   assert attraction_select("41.1579438, -8.629105299999999") == (
       "41.1579438, -8.629105299999999",
       20000,
       "bar",
   )
   assert attraction_select("40.7127753, -74.0059728") == (
       "40.7127753, -74.0059728",
       10000,
       "gym",
   )
   assert attraction_select("-33.8688197, 151.2092955") == (
       "-33.8688197, 151.2092955",
       30000,
       "cafe",
   )
   assert attraction_select("35.6761919, 139.6503106") == (
       "35.6761919, 139.6503106",
       40000,
       "museum",
   )

def test_get_attraction():
    assert get_attraction("41.1579438, -8.629105299999999", 20000, "bar") != ""

def test_final_result():
    resulting = [
        {
            "name": "Hotel da Música",
            "rating": 4.3,
            "number of reviews": 1265,
            "address": "Mercado do Bom Sucesso, Largo Ferreira Lapa, 21 a 183, Porto",
        },
        {
            "name": "Linha22 | Garrafeira & GuestHouse",
            "rating": 4.6,
            "number of reviews": 243,
            "address": "Rua dos Clérigos 23, Porto",
        },
        {
            "name": "Supernova Café",
            "rating": 4.5,
            "number of reviews": 665,
            "address": "Rua Guedes de Azevedo 217, Porto",
        },
        {
            "name": "TRYP Porto Centro Hotel",
            "rating": 4,
            "number of reviews": 950,
            "address": "Rua da Alegria 685 689, Porto",
        },
        {
            "name": "Cats Hostel Porto",
            "rating": 4.4,
            "number of reviews": 637,
            "address": "Rua do Cativo 26 28, Porto",
        },
        {
            "name": "Planoviável",
            "rating": 3,
            "number of reviews": 2,
            "address": "Praça do Bom Sucesso 61, Porto",
        },
        {
            "name": "Padaria Cristal",
            "rating": 4.4,
            "number of reviews": 288,
            "address": "Rua de Cedofeita n 585, Porto",
        },
        {
            "name": "Restaurante Terrella",
            "rating": 3.9,
            "number of reviews": 522,
            "address": "Rua Ofélia Diogo da Costa 105 A, Porto",
        },
        {
            "name": "Pixote Karaoke Bar",
            "rating": 4,
            "number of reviews": 504,
            "address": "Rua do Campo Alegre 241 loja 4, Porto",
        },
        {
            "name": "Diu Palace",
            "rating": 4,
            "number of reviews": 1379,
            "address": "Rua da Boavista 651, Porto",
        },
        {
            "name": "OKNA",
            "rating": 4.8,
            "number of reviews": 58,
            "address": "Rua da Igreja de Cedofeita 27, Porto",
        },
        {
            "name": "Apartamento",
            "rating": 4.5,
            "number of reviews": 623,
            "address": "Rua de Cedofeita 607, Porto",
        },
        {
            "name": "Bali-Hai Polynesian Bar",
            "rating": 4.5,
            "number of reviews": 752,
            "address": "Rua das Águas Férreas 9, Porto",
        },
        {
            "name": "Gato Vadio",
            "rating": 4.7,
            "number of reviews": 88,
            "address": "Rua da Maternidade 124, Porto",
        },
        {
            "name": "Restaurante 1858 bbGourmet criativo",
            "rating": 4.5,
            "number of reviews": 322,
            "address": "Rua de Cedofeita 377 379, Porto",
        },
        {
            "name": "Catraio Craft Beer Shop & Bar",
            "rating": 4.7,
            "number of reviews": 2140,
            "address": "Rua de Cedofeita 256, Porto",
        },
        {
            "name": "Espiga - Espaço de Imaginação Gosto e Artes",
            "rating": 4.6,
            "number of reviews": 230,
            "address": "Rua de Clemente Meneres 65, Porto",
        },
        {
            "name": "Capela Incomum",
            "rating": 4.5,
            "number of reviews": 1269,
            "address": "79-81, Travessa do Carregal 77, Porto",
        },
        {
            "name": "Bulas Wine House",
            "rating": 4.6,
            "number of reviews": 274,
            "address": "Cais das Pedras 13, Porto",
        },
        {
            "name": "Monchique Bar Restaurant",
            "rating": 4.2,
            "number of reviews": 992,
            "address": "Cais das Pedras 5, Porto",
        },
    ]
    nearby = {
        "html_attributions": [],
        "next_page_token": "AcYSjRjIjpsjZmcsMAU98mey5HeNA51tX3Oaxd48B0ZuORPa0yktkSnOHVZ0_IFPrw_Tqu0xajqo5zsGkEqiBcDb-w27xHDHfZuWRldQIxAyEr9a1MO-mApIFBDMqGMLZPj3k-DvJaxhkX0nGAptq40g0IZgaKOR0FwKf2KUFpG2CjVAhbo1hB_R0u72shBOSNKajJQLgtIX-eiEKVRU_UN8vLSTqvlsRyKyL24wjIHCicukgvvbQ1cH-XY1_NhTMfSvFRT8zBZNoDQC8CeCj0YXMkUOVHCbWBL1Meh6mbr5OdtQWo7rIi1rGaNoBIfW7Z38XdqFqHl9PhzAz4vWHVMDZWRq2zjR2I4erLzSZU25KYuBhQaH7dMIMqvoWWeykCK4bdJYBscARurneqCopjLn8XyZm-bI9_60mhBmZs75ea29pEFPUMI",
        "results": [
            {
                "business_status": "OPERATIONAL",
                "geometry": {
                    "location": {"lat": 41.15636, "lng": -8.62924},
                    "viewport": {
                        "northeast": {
                            "lat": 41.15779028029149,
                            "lng": -8.627874519708497,
                        },
                        "southwest": {
                            "lat": 41.15509231970849,
                            "lng": -8.630572480291502,
                        },
                    },
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/lodging-71.png",
                "icon_background_color": "#909CE1",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/hotel_pinlet",
                "name": "Hotel da Música",
                "opening_hours": {"open_now": True},
                "photos": [
                    {
                        "height": 1944,
                        "html_attributions": [
                            '<a href="https://maps.google.com/maps/contrib/109189698348595067806">Hotel da Música</a>'
                        ],
                        "photo_reference": "AcYSjRgvQ39WlUNlwiWmbf5L_9r5aPuvSndP7l1coUiLYl6VeXFT4xMzfvJw4HyRNnoAWiPn70mECWapZBPQ-FQ1Xda9BodIDwjg4lJWUl5LNgVDII7PC_Qsg8sfJqNkagzsmJAeIfIwa7-PmsRBjBz98hSNDJnts8KwW5UeV46sXdRU6u1j",
                        "width": 2592,
                    }
                ],
                "place_id": "ChIJrfpZ9AhlJA0RDRwt5Ox15vs",
                "plus_code": {
                    "compound_code": "594C+G8 Porto, Portugal",
                    "global_code": "8CHH594C+G8",
                },
                "rating": 4.3,
                "reference": "ChIJrfpZ9AhlJA0RDRwt5Ox15vs",
                "scope": "GOOGLE",
                "types": [
                    "bar",
                    "lodging",
                    "parking",
                    "restaurant",
                    "food",
                    "point_of_interest",
                    "establishment",
                ],
                "user_ratings_total": 1265,
                "vicinity": "Mercado do Bom Sucesso, Largo Ferreira Lapa, 21 a 183, Porto",
            },
            {
                "business_status": "OPERATIONAL",
                "geometry": {
                    "location": {"lat": 41.1458589, "lng": -8.6127667},
                    "viewport": {
                        "northeast": {"lat": 41.1472632802915, "lng": -8.6114266197085},
                        "southwest": {
                            "lat": 41.1445653197085,
                            "lng": -8.614124580291504,
                        },
                    },
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/bar-71.png",
                "icon_background_color": "#FF9E67",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/bar_pinlet",
                "name": "Linha22 | Garrafeira & GuestHouse",
                "opening_hours": {"open_now": False},
                "photos": [
                    {
                        "height": 460,
                        "html_attributions": [
                            '<a href="https://maps.google.com/maps/contrib/102901887696348182191">Linha22 | Garrafeira &amp; GuestHouse</a>'
                        ],
                        "photo_reference": "AcYSjRhY90fv9awkSCDyMSF-BffjxtgEPDHqyajbIhN-i_JUGzYjy2PwU2fgBQ19jQ5sGzCfnuL_LWY3ArYnm4tQxOWs-6T7TicmEoYmFRQdUt1gA4Xp5RLbRjP59IkLiR9_j_Gb5JBDiCEhmSjxKyHQQXPyY15-tmqfPdm9l0Xo20IMvUD6",
                        "width": 840,
                    }
                ],
                "place_id": "ChIJE6r-seNkJA0RUndS_BtPOoI",
                "plus_code": {
                    "compound_code": "49WP+8V Porto, Portugal",
                    "global_code": "8CHH49WP+8V",
                },
                "price_level": 2,
                "rating": 4.6,
                "reference": "ChIJE6r-seNkJA0RUndS_BtPOoI",
                "scope": "GOOGLE",
                "types": [
                    "bar",
                    "grocery_or_supermarket",
                    "lodging",
                    "store",
                    "restaurant",
                    "food",
                    "point_of_interest",
                    "establishment",
                ],
                "user_ratings_total": 243,
                "vicinity": "Rua dos Clérigos 23, Porto",
            },
            {
                "business_status": "OPERATIONAL",
                "geometry": {
                    "location": {"lat": 41.1524522, "lng": -8.607644800000001},
                    "viewport": {
                        "northeast": {"lat": 41.1538153802915, "lng": -8.6062388197085},
                        "southwest": {
                            "lat": 41.1511174197085,
                            "lng": -8.608936780291504,
                        },
                    },
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/cafe-71.png",
                "icon_background_color": "#FF9E67",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/cafe_pinlet",
                "name": "Supernova Café",
                "opening_hours": {"open_now": True},
                "photos": [
                    {
                        "height": 750,
                        "html_attributions": [
                            '<a href="https://maps.google.com/maps/contrib/111009595031407532793">Supernova Café</a>'
                        ],
                        "photo_reference": "AcYSjRgBoR3GASuY3yk9kFZrV6WGfO_LqWlZ9ZqnhjGVxolRl0byQIEh5defBQ0CzbmM-9Knzr55uFe6ViL6K3-PTGfCWq4DK8Ga4a7hAaQvnVvSZeU-N_fDgV5H8Tsic_WbRGa6SkDIFyDTQ-cfMUY5r8PkJnq8A-ijoVQ7aEgBZWucGa04",
                        "width": 1000,
                    }
                ],
                "place_id": "ChIJKZSMUvpkJA0RC2FhWkVDTQo",
                "plus_code": {
                    "compound_code": "592R+XW Porto, Portugal",
                    "global_code": "8CHH592R+XW",
                },
                "price_level": 1,
                "rating": 4.5,
                "reference": "ChIJKZSMUvpkJA0RC2FhWkVDTQo",
                "scope": "GOOGLE",
                "types": [
                    "cafe",
                    "bar",
                    "lodging",
                    "store",
                    "restaurant",
                    "food",
                    "point_of_interest",
                    "establishment",
                ],
                "user_ratings_total": 665,
                "vicinity": "Rua Guedes de Azevedo 217, Porto",
            },
            {
                "business_status": "OPERATIONAL",
                "geometry": {
                    "location": {"lat": 41.157131, "lng": -8.602122999999999},
                    "viewport": {
                        "northeast": {
                            "lat": 41.1584629802915,
                            "lng": -8.600718269708498,
                        },
                        "southwest": {
                            "lat": 41.1557650197085,
                            "lng": -8.603416230291502,
                        },
                    },
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/lodging-71.png",
                "icon_background_color": "#909CE1",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/hotel_pinlet",
                "name": "TRYP Porto Centro Hotel",
                "opening_hours": {"open_now": True},
                "photos": [
                    {
                        "height": 2667,
                        "html_attributions": [
                            '<a href="https://maps.google.com/maps/contrib/109936213668285424397">TRYP Porto Centro Hotel</a>'
                        ],
                        "photo_reference": "AcYSjRi_uhdx-zHKmsTn7VNoh5AKGMgkOiGaL3YQpwQloHrkXIGTuImMG04nbaMrJMrfgFIw_xydyJTzirDnnqWUa3-QB-_A_kOUB16So4Cx3UZi__Wum1X95RPchS4A1wnJAysvkXpC3FcTxFH8FarjoVrk-9AtbFj-hFe209-GyPmbyLZP",
                        "width": 4000,
                    }
                ],
                "place_id": "ChIJWV_o_vZkJA0R2I1Becx3Jvw",
                "plus_code": {
                    "compound_code": "594X+V5 Porto, Portugal",
                    "global_code": "8CHH594X+V5",
                },
                "rating": 4,
                "reference": "ChIJWV_o_vZkJA0R2I1Becx3Jvw",
                "scope": "GOOGLE",
                "types": [
                    "bar",
                    "lodging",
                    "parking",
                    "point_of_interest",
                    "establishment",
                ],
                "user_ratings_total": 950,
                "vicinity": "Rua da Alegria 685 689, Porto",
            },
            {
                "business_status": "CLOSED_TEMPORARILY",
                "geometry": {
                    "location": {"lat": 41.1442306, "lng": -8.608990200000001},
                    "viewport": {
                        "northeast": {
                            "lat": 41.1456132802915,
                            "lng": -8.607643619708497,
                        },
                        "southwest": {
                            "lat": 41.1429153197085,
                            "lng": -8.610341580291502,
                        },
                    },
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/lodging-71.png",
                "icon_background_color": "#909CE1",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/hotel_pinlet",
                "name": "Cats Hostel Porto",
                "permanently_closed": True,
                "photos": [
                    {
                        "height": 3024,
                        "html_attributions": [
                            '<a href="https://maps.google.com/maps/contrib/116342165489964115376">Cats Hostel Porto</a>'
                        ],
                        "photo_reference": "AcYSjRjttQujrvOPHtTsQ1Tp_3UPXqNO04Rdx7TLxBtk3KubIpUHLBR5tleiB4nN611iSUxprH1QlSHhOVv8VJAyFfmTBHRg2jDPbu6rzztLmSW4ir2haE6lEGsSctnh2Drn6hyGouLpXgxjzzyhmmOzJxqXX51Q2a8wagYjL77VyjP2wgfV",
                        "width": 4032,
                    }
                ],
                "place_id": "ChIJny5XnuZkJA0RjMBssShAwhQ",
                "plus_code": {
                    "compound_code": "49VR+MC Porto, Portugal",
                    "global_code": "8CHH49VR+MC",
                },
                "rating": 4.4,
                "reference": "ChIJny5XnuZkJA0RjMBssShAwhQ",
                "scope": "GOOGLE",
                "types": [
                    "bar",
                    "lodging",
                    "restaurant",
                    "food",
                    "point_of_interest",
                    "establishment",
                ],
                "user_ratings_total": 637,
                "vicinity": "Rua do Cativo 26 28, Porto",
            },
            {
                "business_status": "CLOSED_TEMPORARILY",
                "geometry": {
                    "location": {"lat": 41.1551027, "lng": -8.6297251},
                    "viewport": {
                        "northeast": {
                            "lat": 41.1564361802915,
                            "lng": -8.628013069708498,
                        },
                        "southwest": {
                            "lat": 41.1537382197085,
                            "lng": -8.630711030291502,
                        },
                    },
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/bar-71.png",
                "icon_background_color": "#FF9E67",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/bar_pinlet",
                "name": "Planoviável",
                "permanently_closed": True,
                "place_id": "ChIJTdoy_ghlJA0RQQu4pfmy0I0",
                "plus_code": {
                    "compound_code": "594C+24 Porto, Portugal",
                    "global_code": "8CHH594C+24",
                },
                "rating": 3,
                "reference": "ChIJTdoy_ghlJA0RQQu4pfmy0I0",
                "scope": "GOOGLE",
                "types": ["bar", "point_of_interest", "establishment"],
                "user_ratings_total": 2,
                "vicinity": "Praça do Bom Sucesso 61, Porto",
            },
            {
                "business_status": "OPERATIONAL",
                "geometry": {
                    "location": {"lat": 41.155876, "lng": -8.6193407},
                    "viewport": {
                        "northeast": {
                            "lat": 41.15722983029151,
                            "lng": -8.617953469708498,
                        },
                        "southwest": {
                            "lat": 41.15453186970851,
                            "lng": -8.620651430291502,
                        },
                    },
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png",
                "icon_background_color": "#FF9E67",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet",
                "name": "Padaria Cristal",
                "opening_hours": {"open_now": False},
                "photos": [
                    {
                        "height": 720,
                        "html_attributions": [
                            '<a href="https://maps.google.com/maps/contrib/112600280459470922684">Susana Melo</a>'
                        ],
                        "photo_reference": "AcYSjRghSGfaFTsvAegckVT-DlFT2sKwWOrbIZWBV38LJ-DqEkzkwpoX7cQ8S36YCRf3LAxuSPHzEM6YzFuNRWqdDT6HBySiUfnTR2cJrmKbw6RfZcHAES3v_p1sW3Njx8hCfwmA13YPUiUM0V0YFKhaSSAm9aIZ-kGAXEOzDMPezOwqA8a3",
                        "width": 960,
                    }
                ],
                "place_id": "ChIJS9_5AgFlJA0RlnrHNz35jqk",
                "plus_code": {
                    "compound_code": "594J+97 Porto, Portugal",
                    "global_code": "8CHH594J+97",
                },
                "price_level": 1,
                "rating": 4.4,
                "reference": "ChIJS9_5AgFlJA0RlnrHNz35jqk",
                "scope": "GOOGLE",
                "types": [
                    "bakery",
                    "bar",
                    "store",
                    "food",
                    "point_of_interest",
                    "establishment",
                ],
                "user_ratings_total": 288,
                "vicinity": "Rua de Cedofeita n 585, Porto",
            },
            {
                "business_status": "OPERATIONAL",
                "geometry": {
                    "location": {"lat": 41.1594901, "lng": -8.631615199999999},
                    "viewport": {
                        "northeast": {
                            "lat": 41.16098588029149,
                            "lng": -8.630125019708496,
                        },
                        "southwest": {"lat": 41.1582879197085, "lng": -8.6328229802915},
                    },
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png",
                "icon_background_color": "#FF9E67",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet",
                "name": "Restaurante Terrella",
                "opening_hours": {"open_now": False},
                "photos": [
                    {
                        "height": 1200,
                        "html_attributions": [
                            '<a href="https://maps.google.com/maps/contrib/100053471759365034661">Restaurante Terrella</a>'
                        ],
                        "photo_reference": "AcYSjRhR1-kcMsVM2kgAeeGK5TflBN4jvuztnrxn38Yh8ErMl_h8iQsylD7uXE3kNenLnARhVLd88sgrwp2F3J9JLPujduGh1qkL2ZaELHJqkzZgQHbYtu3hb4Ljz_SHn6qwXNXzyvQI7WM3qk3tIuCHs7_kUIn0PUcFCQhmaqAVuIUqFoto",
                        "width": 1800,
                    }
                ],
                "place_id": "ChIJgxopP6dlJA0RZX_JotuoXjQ",
                "plus_code": {
                    "compound_code": "5959+Q9 Porto, Portugal",
                    "global_code": "8CHH5959+Q9",
                },
                "price_level": 2,
                "rating": 3.9,
                "reference": "ChIJgxopP6dlJA0RZX_JotuoXjQ",
                "scope": "GOOGLE",
                "types": [
                    "restaurant",
                    "bar",
                    "food",
                    "point_of_interest",
                    "establishment",
                ],
                "user_ratings_total": 522,
                "vicinity": "Rua Ofélia Diogo da Costa 105 A, Porto",
            },
            {
                "business_status": "OPERATIONAL",
                "geometry": {
                    "location": {"lat": 41.15252069999999, "lng": -8.631059399999998},
                    "viewport": {
                        "northeast": {
                            "lat": 41.15392343029149,
                            "lng": -8.629695419708497,
                        },
                        "southwest": {
                            "lat": 41.15122546970849,
                            "lng": -8.632393380291502,
                        },
                    },
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/bar-71.png",
                "icon_background_color": "#FF9E67",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/bar_pinlet",
                "name": "Pixote Karaoke Bar",
                "opening_hours": {"open_now": False},
                "photos": [
                    {
                        "height": 4000,
                        "html_attributions": [
                            '<a href="https://maps.google.com/maps/contrib/103894796966133867060">Pixote Karaoke Bar</a>'
                        ],
                        "photo_reference": "AcYSjRg_4642QofEVDL_YYtsKQMZCha6lprBHSJvxhtbmt2lPWeyb9meSEGpN2B8R51QqNKIEbLxMeOJRs2aUqt3TVdM7H7-NPZiyzXZyq0qLD-ouAgImi7LzYRh-eHc2a_dHaBQvsnQHHI1tCevXf6KKDqaXrOxt5Gh1K6WrX_9l4Of8sM-",
                        "width": 3000,
                    }
                ],
                "place_id": "ChIJG4mOyg5lJA0RCxpPelAL0ZY",
                "plus_code": {
                    "compound_code": "5939+2H Porto, Portugal",
                    "global_code": "8CHH5939+2H",
                },
                "price_level": 2,
                "rating": 4,
                "reference": "ChIJG4mOyg5lJA0RCxpPelAL0ZY",
                "scope": "GOOGLE",
                "types": ["bar", "point_of_interest", "establishment"],
                "user_ratings_total": 504,
                "vicinity": "Rua do Campo Alegre 241 loja 4, Porto",
            },
            {
                "business_status": "OPERATIONAL",
                "geometry": {
                    "location": {"lat": 41.1565111, "lng": -8.6209957},
                    "viewport": {
                        "northeast": {
                            "lat": 41.15789163029149,
                            "lng": -8.619637619708499,
                        },
                        "southwest": {
                            "lat": 41.1551936697085,
                            "lng": -8.622335580291503,
                        },
                    },
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png",
                "icon_background_color": "#FF9E67",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet",
                "name": "Diu Palace",
                "opening_hours": {"open_now": True},
                "photos": [
                    {
                        "height": 2448,
                        "html_attributions": [
                            '<a href="https://maps.google.com/maps/contrib/118003147484732163595">Georgia Archer</a>'
                        ],
                        "photo_reference": "AcYSjRj2znoDBUc0qapXIbBjANjTqmnWXB61rGjNfIKuk265ml7ItZ3NR7ToglliwVnRyDqjy0vqR9PnrRVUe1WRYb5hZkDNxkqLDuuKHOkFqf0bIYEkH2UI2eAk1gGnUZowM37Ha_6LizFGqmwe4czDg2p1Ow8kDwvW4PjjN6wq7imPb3_H",
                        "width": 3264,
                    }
                ],
                "place_id": "ChIJM3k90ABlJA0RZxD_FKU803E",
                "plus_code": {
                    "compound_code": "594H+JJ Porto, Portugal",
                    "global_code": "8CHH594H+JJ",
                },
                "price_level": 2,
                "rating": 4,
                "reference": "ChIJM3k90ABlJA0RZxD_FKU803E",
                "scope": "GOOGLE",
                "types": [
                    "restaurant",
                    "liquor_store",
                    "bar",
                    "bakery",
                    "store",
                    "food",
                    "point_of_interest",
                    "establishment",
                ],
                "user_ratings_total": 1379,
                "vicinity": "Rua da Boavista 651, Porto",
            },
            {
                "business_status": "OPERATIONAL",
                "geometry": {
                    "location": {"lat": 41.15582799999999, "lng": -8.6201736},
                    "viewport": {
                        "northeast": {
                            "lat": 41.15715803029151,
                            "lng": -8.618813419708497,
                        },
                        "southwest": {
                            "lat": 41.15446006970851,
                            "lng": -8.621511380291501,
                        },
                    },
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/generic_business-71.png",
                "icon_background_color": "#7B9EB0",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/generic_pinlet",
                "name": "OKNA",
                "opening_hours": {"open_now": False},
                "photos": [
                    {
                        "height": 1250,
                        "html_attributions": [
                            '<a href="https://maps.google.com/maps/contrib/101508789135070433543">OKNA</a>'
                        ],
                        "photo_reference": "AcYSjRjG-QeL7vIX9jx8Lw3vAwMkL_bTs2AWNJFvtvn0FFw5I_dsiRw2nQbgv3ORLFq7XinA6ltgUKP5iILMdrTqrH0WktBSu09vPQuyRasVCEBy1-kIDohnxvQ9tW8wfXXO8B6dytMRbNfRZoiZyufUSWSCyn5vocsUATwl11yBu0rswEQ7",
                        "width": 1880,
                    }
                ],
                "place_id": "ChIJ84DSr_1kJA0RX_V6p2Yo9ew",
                "plus_code": {
                    "compound_code": "594H+8W Porto, Portugal",
                    "global_code": "8CHH594H+8W",
                },
                "rating": 4.8,
                "reference": "ChIJ84DSr_1kJA0RX_V6p2Yo9ew",
                "scope": "GOOGLE",
                "types": [
                    "cafe",
                    "library",
                    "bar",
                    "store",
                    "food",
                    "point_of_interest",
                    "establishment",
                ],
                "user_ratings_total": 58,
                "vicinity": "Rua da Igreja de Cedofeita 27, Porto",
            },
            {
                "business_status": "OPERATIONAL",
                "geometry": {
                    "location": {"lat": 41.1560547, "lng": -8.619365199999999},
                    "viewport": {
                        "northeast": {
                            "lat": 41.1574066302915,
                            "lng": -8.617993169708498,
                        },
                        "southwest": {
                            "lat": 41.1547086697085,
                            "lng": -8.620691130291501,
                        },
                    },
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png",
                "icon_background_color": "#FF9E67",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet",
                "name": "Apartamento",
                "opening_hours": {"open_now": False},
                "photos": [
                    {
                        "height": 568,
                        "html_attributions": [
                            '<a href="https://maps.google.com/maps/contrib/100944587600398192419">Apartamento</a>'
                        ],
                        "photo_reference": "AcYSjRjjj1elbLR-fWSGlCZrNKtlWRP541bqbndfmaoK-pTaMtimZK5nKPZDMG1llkSeqE6_fJZ7Rd5JXl67afdjfbuUPvCAbNFU544X1V9sSDDs1en1Ruw-oKlsevYfI1qBMu4dQk9GCV8XSCMv6BKlMmf2zx41fp-J4ll1Vc0gixhC2Pnn",
                        "width": 844,
                    }
                ],
                "place_id": "ChIJ0wWDAgFlJA0RnweAA4wgrOE",
                "plus_code": {
                    "compound_code": "594J+C7 Porto, Portugal",
                    "global_code": "8CHH594J+C7",
                },
                "price_level": 1,
                "rating": 4.5,
                "reference": "ChIJ0wWDAgFlJA0RnweAA4wgrOE",
                "scope": "GOOGLE",
                "types": [
                    "restaurant",
                    "cafe",
                    "bar",
                    "store",
                    "food",
                    "point_of_interest",
                    "establishment",
                ],
                "user_ratings_total": 623,
                "vicinity": "Rua de Cedofeita 607, Porto",
            },
            {
                "business_status": "OPERATIONAL",
                "geometry": {
                    "location": {"lat": 41.15626379999999, "lng": -8.6179855},
                    "viewport": {
                        "northeast": {
                            "lat": 41.1575145802915,
                            "lng": -8.616668119708498,
                        },
                        "southwest": {
                            "lat": 41.15481661970851,
                            "lng": -8.619366080291503,
                        },
                    },
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/bar-71.png",
                "icon_background_color": "#FF9E67",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/bar_pinlet",
                "name": "Bali-Hai Polynesian Bar",
                "opening_hours": {"open_now": False},
                "photos": [
                    {
                        "height": 810,
                        "html_attributions": [
                            '<a href="https://maps.google.com/maps/contrib/118058233033644871353">Bali-Hai Polynesian Bar</a>'
                        ],
                        "photo_reference": "AcYSjRgYwlH-COhgw0_D3XTZ9FPGxlh0hGrKiGdoTKQUsJkqAE8AvCPFrgM0GTsTJsq8XlSGy7t3zibw5-_oU7Zg4wBPNCZBO0-w_Wk4xAX-LTe9NUYfqFPul4qHlSCDB2ni9vLHVR-JgdZjTEuUHHkz6aIK0GjvIiGmA-s3cvTEFKSnTBeD",
                        "width": 1439,
                    }
                ],
                "place_id": "ChIJHWwZTQBlJA0R_AAhiozjXSU",
                "plus_code": {
                    "compound_code": "594J+GR Porto, Portugal",
                    "global_code": "8CHH594J+GR",
                },
                "rating": 4.5,
                "reference": "ChIJHWwZTQBlJA0R_AAhiozjXSU",
                "scope": "GOOGLE",
                "types": ["bar", "point_of_interest", "establishment"],
                "user_ratings_total": 752,
                "vicinity": "Rua das Águas Férreas 9, Porto",
            },
            {
                "business_status": "OPERATIONAL",
                "geometry": {
                    "location": {"lat": 41.15154039999999, "lng": -8.6214014},
                    "viewport": {
                        "northeast": {
                            "lat": 41.15292223029149,
                            "lng": -8.620083319708499,
                        },
                        "southwest": {
                            "lat": 41.1502242697085,
                            "lng": -8.622781280291502,
                        },
                    },
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/shopping-71.png",
                "icon_background_color": "#4B96F3",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/shopping_pinlet",
                "name": "Gato Vadio",
                "opening_hours": {"open_now": False},
                "photos": [
                    {
                        "height": 3024,
                        "html_attributions": [
                            '<a href="https://maps.google.com/maps/contrib/117312494241443045222">Leo Slater</a>'
                        ],
                        "photo_reference": "AcYSjRgGrPUwq9rAnPUVPAaO5NMQWr4JvD3Zg3X1dktkJ1TXxyQnSAgdJttVwsgDw1ohtYCvF7hVc8czTxLLu3vIaPKVwx5E-yLiQU1tlefmuZ2Xz-LuR2Eh9XIxD7sKBQ48Y0jJHhdurKKIpd3g-cty6mprc_ZkKlgm7qKqy_JgbKBfzr7U",
                        "width": 4032,
                    }
                ],
                "place_id": "ChIJBY8eggNlJA0RkBcwDsQXUrE",
                "plus_code": {
                    "compound_code": "592H+JC Porto, Portugal",
                    "global_code": "8CHH592H+JC",
                },
                "price_level": 1,
                "rating": 4.7,
                "reference": "ChIJBY8eggNlJA0RkBcwDsQXUrE",
                "scope": "GOOGLE",
                "types": [
                    "book_store",
                    "bar",
                    "store",
                    "point_of_interest",
                    "establishment",
                ],
                "user_ratings_total": 88,
                "vicinity": "Rua da Maternidade 124, Porto",
            },
            {
                "business_status": "OPERATIONAL",
                "geometry": {
                    "location": {"lat": 41.1532107, "lng": -8.6184555},
                    "viewport": {
                        "northeast": {
                            "lat": 41.15456743029149,
                            "lng": -8.617067869708498,
                        },
                        "southwest": {
                            "lat": 41.15186946970849,
                            "lng": -8.619765830291502,
                        },
                    },
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png",
                "icon_background_color": "#FF9E67",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet",
                "name": "Restaurante 1858 bbGourmet criativo",
                "opening_hours": {"open_now": True},
                "photos": [
                    {
                        "height": 1067,
                        "html_attributions": [
                            '<a href="https://maps.google.com/maps/contrib/118017383103067972171">Restaurante 1858 bbGourmet criativo</a>'
                        ],
                        "photo_reference": "AcYSjRgRIukpeBZMXfR-qncZ09kqt6Yet2nJcnoi7eTajrv9XRrR17UljRYGXnJxgLKzNovVeqahCdXUZFiig_-wNHbVCor-uow7WcWYd0YEFyov7Cqnrq0_WVBtBo4IPoWXKHhMfE9fx3uSrpTbdWHRrvdCCzMjWO60bejnPBhgnoDX70Jm",
                        "width": 1600,
                    }
                ],
                "place_id": "ChIJsTdfLgJlJA0RnyzQOH9Pk-s",
                "plus_code": {
                    "compound_code": "593J+7J Porto, Portugal",
                    "global_code": "8CHH593J+7J",
                },
                "price_level": 2,
                "rating": 4.5,
                "reference": "ChIJsTdfLgJlJA0RnyzQOH9Pk-s",
                "scope": "GOOGLE",
                "types": [
                    "restaurant",
                    "bar",
                    "food",
                    "point_of_interest",
                    "establishment",
                ],
                "user_ratings_total": 322,
                "vicinity": "Rua de Cedofeita 377 379, Porto",
            },
            {
                "business_status": "OPERATIONAL",
                "geometry": {
                    "location": {"lat": 41.151108, "lng": -8.617305},
                    "viewport": {
                        "northeast": {
                            "lat": 41.1522605302915,
                            "lng": -8.615899969708495,
                        },
                        "southwest": {"lat": 41.1495625697085, "lng": -8.6185979302915},
                    },
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/bar-71.png",
                "icon_background_color": "#FF9E67",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/bar_pinlet",
                "name": "Catraio Craft Beer Shop & Bar",
                "opening_hours": {"open_now": True},
                "photos": [
                    {
                        "height": 809,
                        "html_attributions": [
                            '<a href="https://maps.google.com/maps/contrib/106780221526985857570">Catraio Craft Beer Shop &amp; Bar</a>'
                        ],
                        "photo_reference": "AcYSjRgxzoC0UE3ljyDinzCLecO5f1bPIWmwYxmZq0FhhNdQkzEPjR2-nyeCDzDnwgyD2z3YLe1BLZO3Jj-nIY5s6i0l2EOcP108ffG1GCa-yYwDD_208as9bj2EtbhXZ0iBUP19d2WDy0vDyriOotk9DWcPGzJHQUhB2qKqUg-8ZIcVOIYu",
                        "width": 1440,
                    }
                ],
                "place_id": "ChIJUZv6igJlJA0RTRQyaiTpfAI",
                "plus_code": {
                    "compound_code": "592M+C3 Porto, Portugal",
                    "global_code": "8CHH592M+C3",
                },
                "price_level": 2,
                "rating": 4.7,
                "reference": "ChIJUZv6igJlJA0RTRQyaiTpfAI",
                "scope": "GOOGLE",
                "types": [
                    "liquor_store",
                    "bar",
                    "store",
                    "restaurant",
                    "food",
                    "point_of_interest",
                    "establishment",
                ],
                "user_ratings_total": 2140,
                "vicinity": "Rua de Cedofeita 256, Porto",
            },
            {
                "business_status": "OPERATIONAL",
                "geometry": {
                    "location": {"lat": 41.1487421, "lng": -8.6192912},
                    "viewport": {
                        "northeast": {
                            "lat": 41.1501004302915,
                            "lng": -8.617933169708499,
                        },
                        "southwest": {
                            "lat": 41.1474024697085,
                            "lng": -8.620631130291503,
                        },
                    },
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/generic_business-71.png",
                "icon_background_color": "#7B9EB0",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/generic_pinlet",
                "name": "Espiga - Espaço de Imaginação Gosto e Artes",
                "opening_hours": {"open_now": True},
                "photos": [
                    {
                        "height": 3464,
                        "html_attributions": [
                            '<a href="https://maps.google.com/maps/contrib/113682824314006019072">Alexander Russell</a>'
                        ],
                        "photo_reference": "AcYSjRjN-FyfF6r54x3o7ZxiaHFXRL9qYs0I_e1hm7SwLkuFBQspCmZjK8qk9-m4R8PoFx2YqwlFEoqU98BJA3l-s1OTn2WKjRdk-BsI2Y5VRBh7yR50nfXDYKH4fL18q9icOgaDdtLtj-YiTtMPngVDyojVh0YOhWHUue-kNdoHNUnOJ1nS",
                        "width": 4618,
                    }
                ],
                "place_id": "ChIJ_bVyKx1lJA0Rbb0NEAcq8-8",
                "plus_code": {
                    "compound_code": "49XJ+F7 Porto, Portugal",
                    "global_code": "8CHH49XJ+F7",
                },
                "price_level": 2,
                "rating": 4.6,
                "reference": "ChIJ_bVyKx1lJA0Rbb0NEAcq8-8",
                "scope": "GOOGLE",
                "types": [
                    "art_gallery",
                    "bar",
                    "restaurant",
                    "food",
                    "point_of_interest",
                    "establishment",
                ],
                "user_ratings_total": 230,
                "vicinity": "Rua de Clemente Meneres 65, Porto",
            },
            {
                "business_status": "OPERATIONAL",
                "geometry": {
                    "location": {"lat": 41.14907280000001, "lng": -8.617830900000001},
                    "viewport": {
                        "northeast": {
                            "lat": 41.1503885302915,
                            "lng": -8.616474519708499,
                        },
                        "southwest": {
                            "lat": 41.1476905697085,
                            "lng": -8.619172480291503,
                        },
                    },
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/bar-71.png",
                "icon_background_color": "#FF9E67",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/bar_pinlet",
                "name": "Capela Incomum",
                "opening_hours": {"open_now": True},
                "photos": [
                    {
                        "height": 2976,
                        "html_attributions": [
                            '<a href="https://maps.google.com/maps/contrib/115290510578873107073">Capela Incomum</a>'
                        ],
                        "photo_reference": "AcYSjRh0X6T-IqRokYXUgDWtFpXAmI0bx38m3lBq7RicKuNxBhxkPIy5hevLVerJFzwxyFWdTeUw-BpEEXDwI7FrwqYV72VZUenD4UP37TxD7W3z5bo-tBnBSU60nicmK28J38FblmvIVXrXFvBNWEbZDgsz7FZu6_OwLAKPeYILQkMJqsed",
                        "width": 3968,
                    }
                ],
                "place_id": "ChIJL_2vzgJlJA0RM9680REujIo",
                "plus_code": {
                    "compound_code": "49XJ+JV Porto, Portugal",
                    "global_code": "8CHH49XJ+JV",
                },
                "price_level": 2,
                "rating": 4.5,
                "reference": "ChIJL_2vzgJlJA0RM9680REujIo",
                "scope": "GOOGLE",
                "types": [
                    "liquor_store",
                    "bar",
                    "store",
                    "restaurant",
                    "food",
                    "point_of_interest",
                    "establishment",
                ],
                "user_ratings_total": 1269,
                "vicinity": "79-81, Travessa do Carregal 77, Porto",
            },
            {
                "business_status": "OPERATIONAL",
                "geometry": {
                    "location": {"lat": 41.145585, "lng": -8.629687199999998},
                    "viewport": {
                        "northeast": {
                            "lat": 41.1469360802915,
                            "lng": -8.628337219708499,
                        },
                        "southwest": {
                            "lat": 41.1442381197085,
                            "lng": -8.631035180291502,
                        },
                    },
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/bar-71.png",
                "icon_background_color": "#FF9E67",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/bar_pinlet",
                "name": "Bulas Wine House",
                "opening_hours": {"open_now": True},
                "photos": [
                    {
                        "height": 2268,
                        "html_attributions": [
                            '<a href="https://maps.google.com/maps/contrib/102394630377717244825">Nuno Monteiro</a>'
                        ],
                        "photo_reference": "AcYSjRgzwGw2OYxwHuujHjBpMIa19d5xUI0eOGtjJJQpN-eZO7bSLHD1CTSCxWuFipS-klbYjyHC4PBkCMhqBnY-Ri8havPf1tcEpkkdrKcsRa97dOis099VeAP65RZ6mTUf_0iy5ZRbtOVo66THV0KNNiaiqSfserpkW35ZPtpww6qW0oh2",
                        "width": 4032,
                    }
                ],
                "place_id": "ChIJp8bz-xBlJA0RD2ttwv2A-cI",
                "plus_code": {
                    "compound_code": "49WC+64 Porto, Portugal",
                    "global_code": "8CHH49WC+64",
                },
                "price_level": 2,
                "rating": 4.6,
                "reference": "ChIJp8bz-xBlJA0RD2ttwv2A-cI",
                "scope": "GOOGLE",
                "types": [
                    "liquor_store",
                    "bar",
                    "store",
                    "restaurant",
                    "food",
                    "point_of_interest",
                    "establishment",
                ],
                "user_ratings_total": 274,
                "vicinity": "Cais das Pedras 13, Porto",
            },
            {
                "business_status": "OPERATIONAL",
                "geometry": {
                    "location": {"lat": 41.1455597, "lng": -8.6294066},
                    "viewport": {
                        "northeast": {
                            "lat": 41.1468612802915,
                            "lng": -8.628111969708497,
                        },
                        "southwest": {
                            "lat": 41.1441633197085,
                            "lng": -8.630809930291502,
                        },
                    },
                },
                "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/restaurant-71.png",
                "icon_background_color": "#FF9E67",
                "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/restaurant_pinlet",
                "name": "Monchique Bar Restaurant",
                "opening_hours": {"open_now": True},
                "photos": [
                    {
                        "height": 9000,
                        "html_attributions": [
                            '<a href="https://maps.google.com/maps/contrib/109590982160208223205">Bruno Wega</a>'
                        ],
                        "photo_reference": "AcYSjRjR8CUrxDB6lNUv9KpE6Th_9UA5sAMLT1mNcq3Y1xYJThR0BOCLc6GSS_yxlVLcG_U2m5-25JtAG_vgJ1jthrGzAsoIuAjZwL84uG8dIrqfgo4v7hNIquVAq9YDKVvc0SyOf_KYXgIUBn94sjAuZ2aeVJgYhAmNTh9Drr9oBCR71tjG",
                        "width": 12000,
                    }
                ],
                "place_id": "ChIJMXgpVBBlJA0RelH_Aq4F10Y",
                "plus_code": {
                    "compound_code": "49WC+66 Porto, Portugal",
                    "global_code": "8CHH49WC+66",
                },
                "price_level": 2,
                "rating": 4.2,
                "reference": "ChIJMXgpVBBlJA0RelH_Aq4F10Y",
                "scope": "GOOGLE",
                "types": [
                    "restaurant",
                    "liquor_store",
                    "bar",
                    "grocery_or_supermarket",
                    "bakery",
                    "store",
                    "food",
                    "point_of_interest",
                    "establishment",
                ],
                "user_ratings_total": 992,
                "vicinity": "Cais das Pedras 5, Porto",
            },
        ],
        "status": "OK",
    }
    type_of_attraction = "bar"
    assert final_result(resulting, nearby, type_of_attraction) == final_result(
        resulting, nearby, type_of_attraction
    )


def test_main():
   assert final_result(*get_attraction(*attraction_select("41.1579438, -8.629105299999999"))) == final_result(*get_attraction(*attraction_select("41.1579438, -8.629105299999999")))
   assert final_result(*get_attraction(*attraction_select("40.7127753, -74.0059728"))) == final_result(*get_attraction(*attraction_select("40.7127753, -74.0059728")))
   assert final_result(*get_attraction(*attraction_select("-33.8688197, 151.2092955"))) == final_result(*get_attraction(*attraction_select("-33.8688197, 151.2092955")))
   assert final_result(*get_attraction(*attraction_select("35.6761919, 139.6503106"))) == final_result(*get_attraction(*attraction_select("35.6761919, 139.6503106")))