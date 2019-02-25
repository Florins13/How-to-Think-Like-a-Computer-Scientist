import pygame
import random
# You can find solution to exercise to in drawqueens.py
# Exercise 3 from python game!
# Pass on 4 and 5 exercise.


class Card:
    def __init__(self, img, position, number):
        self.image = img
        self.pos = position
        self.number = number
        print(self.number)

    def draw(self, target_surface):
        my_width = self.image.get_width()
        my_height = self.image.get_height()
        row = my_width // 13
        col = my_height // 4
        #print(row, col)
        if self.number <= 12:
            target_surface.blit(self.image, (self.pos), (row*self.number, 0, 75, 100))
        if self.number > 12 and self.number <= 25:
            target_surface.blit(self.image, (self.pos), (row*(self.number - 13), col*1, 75, 100))
            #print(row*(self.number % 13))
        if self.number > 25 and self.number <= 38:
            target_surface.blit(self.image, (self.pos), (row*(self.number - 26), col*2, 75, 100))
        if self.number > 38:
            target_surface.blit(self.image, (self.pos), (row*(self.number - 39), col*3, 75, 100))


def shuffle():
    pygame.init()
    my_clock = pygame.time.Clock()
    main_surface = pygame.display.set_mode((1000, 600))  # prepare the surface
    main_surface.fill((0, 100, 100))
    my_font = pygame.font.SysFont("Courier", 17)  # font for text
    cards = pygame.image.load("cards.png")
    listcard = list(range(52))
    random.shuffle(listcard)
    print(listcard)
    cardobject = []
    print(cardobject)
    count = 0
    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        if ev.type == pygame.KEYDOWN:
            key = ev.dict["key"]
            if key == 27:
                break
            elif key == ord("a"):
                for i in range(5):
                    card = Card(cards, (100*i, 150), listcard[count])
                    cardobject.append(card)
                    count += 1
            elif key == ord("r"):
                for i in range(5):
                    cardobject.pop(0)
            elif key == ord("g"):
                for card in cardobject:
                    card.draw(main_surface)
            elif key == ord("c"):
                main_surface.fill((0, 100, 100))

        the_text = my_font.render("Press 'a' to pick first 5 cards from a deck.", True, (0, 255, 0))
        the_text1 = my_font.render("Press 'g' to show the cards!", True, (255, 255, 0))
        the_text2 = my_font.render("Press 'r' to remove first 5 cards!", True, (0, 255, 50))
        the_text3 = my_font.render("Press 'c' to clear the screen.", True, (0, 255, 255))
        the_text4 = my_font.render("Press 'ESC' to exit.", True, (0, 100, 255))
        main_surface.blit(the_text, (10, 10))
        main_surface.blit(the_text1, (10, 30))
        main_surface.blit(the_text2, (10, 50))
        main_surface.blit(the_text3, (10, 70))
        main_surface.blit(the_text4, (10, 90))
        pygame.display.flip()
        my_clock.tick(60)
    pygame.quit()


shuffle()
