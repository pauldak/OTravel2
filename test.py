from trymap import generate_google_maps_embed

start_place = "Windhoek, Namibia"
end_place = "Etosha National Park, Namibia"
google_maps_embed = generate_google_maps_embed(start_place, end_place)
print(google_maps_embed)