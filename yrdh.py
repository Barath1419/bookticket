# UPDATE `bookmyshow`.`movies` SET `availableseats` = '{\"A1\": 0, \"A2\": 0, \"A3\": 0, \"A4\": 0, \"A5\": 0, \"A6\": 0, \"B1\": 0, \"B2\": 0, \"B3\": 0, \"B4\": 0, \"B5\": 0, \"B6\": 0, \"C1\": 0, \"C2\": 0, \"C3\": 0, \"C4\": 0, \"C5\": 0, \"C6\": 0, \"D1\": 0, \"D2\": 0, \"D3\": 0, \"D4\": 0, \"D5\": 0, \"D6\": 0}' WHERE (`id` = '10');
import requests
import json
movie_name = input("Enter the movie name : ")
response_API = requests.get(f'http://www.omdbapi.com/?t={movie_name}&plot=full&apikey=5e6996f7')
raw_data = response_API.text
movie_details = json.loads(raw_data)
print(movie_details)