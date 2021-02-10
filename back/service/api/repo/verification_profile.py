
PROFILES = [
    {
        "photo_id": 546546,
        "photo_prev": "https://cdnimg.rg.ru/pril/article/192/96/77/7_SELFI_uralskij_mars.JPG",
        "selfie_prev": "https://www.cableman.ru/sites/default/files/nikolay_krasovskiy.jpg",
        "created_at": "2020-12-14 17:51:27",
        "user": {
            "user_id": 115536,
            "name": "Петр",
            "years": 21,
            "city": "Москва",
            "avatar": "https://cdnimg.rg.ru/pril/article/192/96/77/7_SELFI_uralskij_mars.JPG"
        }
    },
    {
        "photo_id": 5464,
        "photo_prev": "https://cdnimg.rg.ru/pril/article/192/96/77/7_SELFI_uralskij_mars.JPG",
        "selfie_prev": "https://www.cableman.ru/sites/default/files/nikolay_krasovskiy.jpg",
        "created_at": "2020-12-14 13:12:20",
        "user": {
            "user_id": 216586,
            "name": "Евгений",
            "years": 33,
            "city": "Новосибирск",
            "avatar": "https://cdnimg.rg.ru/pril/article/192/96/77/7_SELFI_uralskij_mars.JPG"
        }
    },
    {
        "photo_id": 8825,
        "photo_prev": "https://cdnimg.rg.ru/pril/article/192/96/77/7_SELFI_uralskij_mars.JPG",
        "selfie_prev": "https://www.cableman.ru/sites/default/files/nikolay_krasovskiy.jpg",
        "created_at": "2020-10-14 07:11:27",
        "user": {
            "user_id": 864,
            "name": "Romis",
            "years": 19,
            "city": "Италия",
            "avatar": "https://cdnimg.rg.ru/pril/article/192/96/77/7_SELFI_uralskij_mars.JPG"
        }
    },
    {
        "photo_id": 5353,
        "photo_prev": "https://cdnimg.rg.ru/pril/article/192/96/77/7_SELFI_uralskij_mars.JPG",
        "selfie_prev": "https://www.cableman.ru/sites/default/files/nikolay_krasovskiy.jpg",
        "created_at": "2020-12-14 10:01:07",
        "user": {
            "user_id": 1863,
            "name": "Артем",
            "years": 36,
            "city": "Москва",
            "avatar": "https://cdnimg.rg.ru/pril/article/192/96/77/7_SELFI_uralskij_mars.JPG"
        }
    },
    {
        "photo_id": 6587,
        "photo_prev": "https://cdnimg.rg.ru/pril/article/192/96/77/7_SELFI_uralskij_mars.JPG",
        "selfie_prev": "https://www.cableman.ru/sites/default/files/nikolay_krasovskiy.jpg",
        "created_at": "2020-12-13 16:51:58",
        "user": {
            "user_id": 1698,
            "name": "Петр",
            "years": 48,
            "city": "Владивосток",
            "avatar": "https://cdnimg.rg.ru/pril/article/192/96/77/7_SELFI_uralskij_mars.JPG"
        }
    },
    {
        "photo_id": 5784,
        "photo_prev": "https://cdnimg.rg.ru/pril/article/192/96/77/7_SELFI_uralskij_mars.JPG",
        "selfie_prev": "https://www.cableman.ru/sites/default/files/nikolay_krasovskiy.jpg",
        "created_at": "2020-12-14 17:50:27",
        "user": {
            "user_id": 13554,
            "name": "Максим",
            "years": 21,
            "city": "Москва",
            "avatar": "https://cdnimg.rg.ru/pril/article/192/96/77/7_SELFI_uralskij_mars.JPG"
        }
    },
]


def remove_profile(user_id):
    for profile in PROFILES:
        if profile["user"]["user_id"] == user_id:
            PROFILES.remove(profile)
            return True
    return False
