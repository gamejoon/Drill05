from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)

character = load_image("run_animation.png")
hand = load_image("hand_arrow.png")
background = load_image("TUK_GROUND.png")

running = True

def handle_event():
    global running

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

while running:
    background.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    handle_event()
    update_canvas()

close_canvas()