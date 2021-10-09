import pygame
import pygame.gfxdraw
import math


def main():
    pygame.init()

    display             = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
    clock               = pygame.time.Clock()
    process_interrupted = False

    pygame.display.set_caption("Segment Snake")
    pygame.display.set_icon(pygame.image.load("lib/images/segmentsnake.png"))

    # -----------------------------------------------------

    font = pygame.font.Font("lib/fonts/font.ttf", 25)

    # -----------------------------------------------------

    amount_of_segments = 10
    segment_length     = 30

    x = [0 for _ in range(amount_of_segments)]
    y = [0 for _ in range(amount_of_segments)]

    info_text = [
        font.render(f"amount of segments: {amount_of_segments}", True, (255, 255, 255)),
        font.render(f"segment length: {segment_length}", True, (255, 255, 255))
    ]

    # -----------------------------------------------------

    while not process_interrupted:
        pygame.display.set_caption(f"Segment Snake    FPS {clock.get_fps():.0f}")

        display.fill((0, 0, 0))

        # Drag segment ------------------------------------

        mouse_position     = pygame.mouse.get_pos()

        for segment in range(amount_of_segments):
            if segment == 0:
                angle = math.atan2(
                    mouse_position[1] - y[segment],
                    mouse_position[0] - x[segment]
                )

                x[0] = mouse_position[0] - (math.cos(angle) * segment_length)
                y[0] = mouse_position[1] - (math.sin(angle) * segment_length)
            else:
                angle = math.atan2(
                    y[segment - 1] - y[segment],
                    x[segment - 1] - x[segment]
                )

                x[segment] = x[segment - 1] - (math.cos(angle) * segment_length)
                y[segment] = y[segment - 1] - (math.sin(angle) * segment_length)

            # Draw segment --------------------------------

            pygame.draw.aaline(
                display, (255, 255, 255), (
                    x[segment], y[segment]
                ), (
                    x[segment] + (math.cos(angle) * segment_length),
                    y[segment] + (math.sin(angle) * segment_length)
                )
            )

            pygame.gfxdraw.circle(
                display, int(x[segment]), int(y[segment]), 5, (200, 200, 200)
            )

        # -------------------------------------------------

        for text in range(len(info_text)):
            text_rect = info_text[text].get_rect()
            display.blit(info_text[text], (10, 10 + (text_rect.h * text)))

        # -------------------------------------------------

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                process_interrupted = True

            if event.type == pygame.KEYDOWN:

                # Increase / Decrease the length of the snake

                if event.key == pygame.K_UP:

                    amount_of_segments += 1
                    x.append(0)
                    y.append(0)

                if event.key == pygame.K_DOWN:
                    if amount_of_segments > 1:

                        amount_of_segments -= 1
                        x.pop()
                        y.pop()

                # Increase / Decrease the length of the segment

                if event.key == pygame.K_RIGHT:
                    segment_length += 1

                if event.key == pygame.K_LEFT:
                    if segment_length > 1:
                        segment_length -= 1

            # Update info texts
            info_text = [
                font.render(f"amount of segments: {amount_of_segments}", True, (255, 255, 255)),
                font.render(f"segment length: {segment_length}", True, (255, 255, 255))
            ]

        pygame.display.update()
        clock.tick()

    pygame.quit()


if __name__ == '__main__':
    main()
