#!/usr/bin/python3
# Festive Holiday Wish Generator

import random

class HolidayWishGenerator:
    def __init__(self):
        self.adjectives = ["Merry", "Joyful", "Magical", "Enchanting", "Whimsical", "Sparkling", "Radiant"]
        self.nouns = ["Holidays", "Celebration", "Wonderland", "Festivities", "Jubilation", "Harmony", "Rejoice"]
        self.verbs = ["Wishing", "Spreading", "Sharing", "Creating", "Dancing", "Singing", "Glowing"]

    def generate_wish(self):
        adjective = random.choice(self.adjectives)
        noun = random.choice(self.nouns)
        verb = random.choice(self.verbs)

        wish = f"{adjective} {noun} to You and Yours! May your days be filled with {verb} happiness and {adjective.lower()} moments."

        return wish

if __name__ == "__main__":
    wish_generator = HolidayWishGenerator()
    holiday_wish = wish_generator.generate_wish()

    print(holiday_wish)
