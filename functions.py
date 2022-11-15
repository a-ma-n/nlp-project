import json


# import firebase_admin
# from firebase_admin import credentials, firestore
#
# cred = credentials.Certificate('./google-services.json')
# firebase_admin.initialize_app(cred)
#
# print("initializing storage access")
# db = firestore.client()


def get_audio(keywords: list, only_one: bool = False):
    res = {}
    with open("sounds.json", "r") as file:
        ls = json.load(file)
        for keyword in keywords:
            flag = 0
            for doc in ls:
                if keyword in doc["keywords"]:
                    flag = 1
                    res[keyword] = doc['media']
                    break
            if flag == 1 and only_one:
                break
            if flag == 0:
                print(f"Could not find {keyword}")
                # db.collection(u'report').document(u'model').update({keyword: firestore.Increment(1)})
        file.close()
    if len(res.keys()) > 0:
        return res
    return None


# def get_audio(keywords: list, onlyOne: bool = False):
#     sounds = []
#     for word in keywords:
#         flag = 0
#         print(f"searching for sounds related to {word}")
#         audio_ref = db.collection(u'sounds')
#         try:
#             docs = audio_ref.where(u'keywords', u'array_contains', word).limit(1).stream()
#             for doc in docs:
#                 if doc.exists:
#                     flag = 1
#                     sounds.append({word: doc.to_dict()['media']})
#                     if onlyOne:
#                         return sounds
#                     break
#             if flag == 0:
#                 db.collection(u'report').document(u'model').update(
#                     {word: firestore.Increment(1)})
#         except:
#             return "error"
#     return sounds


def report(word):
    print(f'Adding {word} to firestore')
    try:
        # db.collection(u'report').document(u'user').update(
        #     {word: firestore.Increment(1)})
        return "success"
    except:
        return "error"


if __name__ == "__main__":
    print("finding docs")
    print(get_audio(['lion', 'aaaa', 'wolf', 'tiger'], only_one=False))
