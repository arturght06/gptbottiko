from pymongo import MongoClient
import asyncio
import json

global colectiob
cluster = MongoClient('mongodb+srv://Admin:root@cluster0.wa7hj.mongodb.net/userdata?retryWrites=true&w=majority')
db = cluster['userdataTEST']
collection = db['users']

async def print_all():
    result_dict = {}
    for x in collection.find():
        # print(x)
        result_dict[x['id_user']] = x['language']
    return result_dict

async def saveAllToJson():
	data = await print_all()
	with open("users.json", "w") as write_file:
		json.dump(data, write_file)
	return 'all info saved into json file'

async def saveOneToJson(user_id, language):
	with open("users.json", "r") as write_file:
		data = json.load(write_file)
		data[str(user_id)] = language
	with open('users.json', 'w') as write_file:
		json.dump(data, write_file)
	return 'one account saved into json file'



async def write_update_lang(id_user, language):
    if collection.count_documents({'id_user': id_user}) == 1:
        collection.update_one({'id_user': id_user}, {'$set': {'language': language}})
        return True
    elif collection.count_documents({'id_user': id_user}) == 0:
        collection.insert_one({'id_user': id_user, 'language': language})
        return True
    else:
        return False

async def check(user_id):
	with open("users.json", "r") as write_file:
		data = json.load(write_file)
		if str(user_id) not in data:
			return False
		else:
			return data[str(user_id)]