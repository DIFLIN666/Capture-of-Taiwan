import pygame
import random

pygame.init()

TICKRATE = 60
BG_COLOR = (186, 85, 211)
CARD_COLOR = (255, 250, 205)
WIN_COLOR = (50, 205, 50)
LOSE_COLOR = (139, 0, 0)
#размеры окна игры
window =pygame.display.set_mode((500, 500))
#установка цвета фона игры
window.fill(BG_COLOR)

clock = pygame.time.Clock()

#созданние класса карт
class Card():
    def __init__(self, x):
        self.rect = pygame.Rect(x, 170, 70, 100)
        self.color = CARD_COLOR
        self.font = pygame.font.Font(None, 30)
        self.text = self.font.render('CLICK', True, (0, 0, 0))


    def draw(self, need_text):
        pygame.draw.rect(window, self.color, self.rect)
        if need_text:
            window.blit(self.text, (self.rect.x + 5, self.rect.y + 40))

class Text():
    def __init__(self, x, y, text):
        self.font = pygame.font.Font(None, 30)
        self.text = self.font.render(text, True, (0, 0, 0))
        self.pos = (x, y)

    def draw(self):
        window.blit(self.text, self.pos)


    def update(self, text):
        self.text = self.font.render(text, True, (0, 0, 0))


cards = []

#количество карт и расстояние между ними
x= 70
for i in range(4):
    cards.append(Card(x))
    x += 100

card_cd = 0 
score = 0
timer = 0
timer_cd = TICKRATE 

score_text = Text(10, 10, 'Счёт: 0')
timer_text = Text(10, 40, 'Время: 0')

win_text = Text(180, 250, 'Ты победил!')
lose_text = Text(180, 250, 'Ты проиграл!')
state = 'play'

#игровой цикл
while True:
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            exit()
    if state == 'play':
        if card_cd == 0:
            card_cd = TICKRATE // 2
            rand_card = random.randint(0, 3)
            for i in range(4):
                cards[i].color = CARD_COLOR
        else:
            card_cd -= 1

        if timer_cd == 0:
            timer += 1
            timer_text.update(f'Время: {timer}')
            timer_cd = TICKRATE
        else:
            timer_cd -= 1


        window.fill(BG_COLOR)
        score_text.draw()
        timer_text.draw()


        for i in range(4):
            if i == rand_card:
                cards[i].draw(True)
            else:
                cards[i].draw(False)



    #возможность выйти из игры
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                x, y = e.pos 
                for i in range(4):
                    if cards[i].rect.collidepoint(x, y):
                        if i == rand_card:
                            cards[i].color = WIN_COLOR
                            score += 1
                        else:
                            cards[i].color = LOSE_COLOR
                            score -= 1
                        score_text.update(f'Счёт: {score}')
        if score >= 5 and timer <= 10:
            state = 'win'
        elif score < 5 and timer > 10:
            state = 'lose'
    elif state == 'win':
        window.fill(WIN_COLOR)
        win_text.draw()
    elif state == 'lose':
        window.fill(LOSE_COLOR)
        lose_text.draw()




    pygame.display.flip()
    clock.tick(TICKRATE)