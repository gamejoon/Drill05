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

def random_arrow_location():
    global arrow_location
    arrow_location = [random.randint(0, TUK_WIDTH - 1), random.randint(0, TUK_HEIGHT - 1)]

def run_motion():
    global frame, x, y
    
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    frame = (frame + 1) % 8

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)

character = load_image("run_animation.png")
arrow = load_image("hand_arrow.png")
background = load_image("TUK_GROUND.png")

running = True

x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0

arrow_location = []

random_arrow_location()

while running:
    background.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    arrow.draw(arrow_location[0], arrow_location[1])
    run_motion()

    handle_event()
    update_canvas()
    delay(0.05)

close_canvas()