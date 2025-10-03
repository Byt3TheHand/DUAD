hotel = {
"name":"Grand Hotel",
"star_grade":"5",
"rooms":[
    {"number":7,"floor": 22,"price_per_night":250},
    {"number":8,"floor": 22,"price_per_night":350}
    ]
}

print( hotel["name"]," Price :", hotel["rooms"][1]["price_per_night"],'$')  
