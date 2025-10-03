import csv

genre_counter = {}

with open ('gameclass.csv', newline='',encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:
        genre = row['género']

        if genre in genre_counter:
            genre_counter[genre] += 1
        else:
            genre_counter[genre] = 1

print("Video games count by genre:\n")
for genre in sorted(genre_counter):
    print(f"{genre}: {genre_counter[genre]}")