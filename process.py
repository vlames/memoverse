# File: process.py
# Description: the file contains code that supplies the javascript file with api data when requested

from flask.views import MethodView, request
import requests
import json
import os


class Process(MethodView):
    def post(self):

        API_KEY = os.environ["BIBLE_API_KEY"]
        headers = {"api-key": API_KEY}
        common_api_route = "https://api.scripture.api.bible/v1/bibles"
        
        req = request.get_json()

        # Prints specific request error
        def print_response_error(error, resource):
            print("\n" + resource + " request: " + str(error["statusCode"]) + ", " + error["error"] + ", " + error["message"] + "\n")
            pass

        # Gets one of the Bible versions from the api and then returns books on success
        # https://api.scripture.api.bible/v1/bibles
        if (req["bibleInfo"] == "books"):
            bible_version = "King James (Authorised) Version"
            url = common_api_route
            response = requests.get(url, headers=headers)
            if (response.ok == False):
                error = response.json()
                print_response_error(error, "Bibles")
                req["version"] = {"name": "Failed to get a name", "id": "Failed to get an id"}
            else:
                bible_list = response.json()["data"]
                specific_bible_list = [ {"name": str(bible["name"]), "id": str(bible["id"])} for bible in bible_list if bible["name"] == bible_version ]
                req["version"] = specific_bible_list[1]

            # Gets Bible books from the api
            # /v1/bibles/
            url = common_api_route + "/" + req["version"]["id"] + "/books"
            response = requests.get(url, headers=headers)
            if (response.ok == False):
                error = response.json()
                print_response_error(error, "Books")
                req["books"] = [ {"name": "Failed to get names", "id": "Failed to get ids"} ]
            else:
                book_list = response.json()["data"]
                req["books"] = [ {"name": str(book["name"]), "id": str(book["id"])} for book in book_list ]
            return json.dumps(req)
        

        # Gets chapters for a selected book
        # /v1/bibles/{bibleId}/books/{bookId}/chapters 
        elif (req["bibleInfo"] == "chapters"):
            url = common_api_route + "/" + str(req["version"]["id"]) + "/books/" + str(req["selected_book"]) + "/chapters"
            response = requests.get(url, headers=headers)
            if (response.ok == False):
                error = response.json()
                print_response_error(error, "Chapters")
                req["chapters"] = [{"number": "Failed to get chapter numbers", "id": "Failed to get ids"}]
            else:
                chapter_list = response.json()["data"]
                req["chapters"] = [ {"number": str(chapter["number"]), "id": str(chapter["id"])} for chapter in chapter_list ]
            return json.dumps(req)


        # Gets verses for a selected chapter
        # /v1/bibles/{bibleId}/chapters/{chapterId}/verses 
        elif (req["bibleInfo"] == "verses"):
            url = common_api_route + "/" + str(req["version"]["id"]) + "/chapters/" + str(req["selected_chapter"]) + "/verses"
            response = requests.get(url, headers=headers)
            if (response.ok == False):
                error = response.json()
                print_response_error(error, "Verses")
                req["verses"] = [ {"number": "Failed to get verse numbers", "id": "Failed to get ids"} ]
            else:
                verse_list = response.json()["data"]
                req["verses"] = [ {"number": "", "id": str(verse["id"])} for verse in verse_list ]
                verse_num = 1
                for verse in req["verses"]:
                    verse["number"] = str(verse_num)
                    verse_num = verse_num + 1
            return json.dumps(req)
        

        # Finally, gets a specific verse value, verse reference, and meta data for the selected verse
        # /v1/bibles/{bibleId}/verses/{verseId}  
        elif (req["bibleInfo"] == "verse"):
            url = common_api_route + "/" + str(req["version"]["id"]) + "/verses/" + str(req["selected_verse"])
            response = requests.get(url, headers=headers)
            if (response.ok == False):
                error = response.json()
                print_response_error(error, "Verse")
                req["verse"] = "Failed to get the verse"
                req["reference"] = "Failed to get a reference"
                req["meta"] = {"fums": "Failed to get fums"}
            else:
                response = response.json()
                req["verse"] = response["data"]["content"]
                req["reference"] = response["data"]["reference"]
                req["meta"] = response["meta"]
            return json.dumps(req)
            
        return json.dumps("")