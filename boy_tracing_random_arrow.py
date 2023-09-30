from pico2d import *
import random

def handle_event():
    global running

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

def run_motion():
    global frame
    
    if (arrow_location[0] - x1 >= 0):
        character.clip_draw(frame * 100, 0, 100, 100, x2, y2)
    else:
        character.clip_composite_draw(frame * 100, 0, 100, 100, 0, 'h', x2, y2, 100, 100)
    frame = (frame + 1) % 8

def route_for_run():
    global arrow_location, x1, y1, x2, y2, route_rate

    x2 = (1 - route_rate / 14) * x1 + (route_rate / 14) * arrow_location[0]
    y2 = (1 - route_rate / 14) * y1 + (route_rate / 14) * arrow_location[1]
    route_rate = (route_rate + 1) % 15

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)

character = load_image("run_animation.png")
arrow = load_image("hand_arrow.png")
background = load_image("TUK_GROUND.png")

running = True

x1, y1 = TUK_WIDTH // 2, TUK_HEIGHT // 2
x2, y2 = x1, y1
frame = 0
route_rate = 0

arrow_location = []

arrow_location = [random.randint(0, TUK_WIDTH - 1), random.randint(0, TUK_HEIGHT - 1)]

while running:
    if (arrow_location[0], arrow_location[1]) == (x2, y2):
        arrow_location = [random.randint(0, TUK_WIDTH - 1), random.randint(0, TUK_HEIGHT - 1)]
        x1, y1 = x2, y2
    route_for_run()

    background.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    arrow.draw(arrow_location[0], arrow_location[1])
    run_motion()

    handle_event()
    update_canvas()
    delay(0.05)

close_canvas()