"""Parametric one-piece DUPLO-scale spider-hero figure.

Origin: midpoint between the two foot sockets on the build plate.
XY: build plate, with the figure facing -Y. +Z: upward.

The stud interface dimensions are provisional calibration assumptions.
"""

from build123d import Align, Box, Cylinder, Pos, Sphere, fillet


# Assumed DUPLO mating dimensions; verify against the actual brick and printer.
STUD_PITCH = 16.0
SOCKET_DIAMETER = 9.8
SOCKET_DEPTH = 4.2

# Chunky figure envelope and printable feature sizes.
LEG_WIDTH = 14.0
LEG_DEPTH = 20.0
LEG_HEIGHT = 24.0
TORSO_WIDTH = 31.0
TORSO_DEPTH = 22.0
TORSO_HEIGHT = 30.0
ARM_WIDTH = 10.0
ARM_DEPTH = 18.0
ARM_HEIGHT = 32.0
HEAD_WIDTH = 32.0
HEAD_DEPTH = 28.0
HEAD_HEIGHT = 27.0
RELIEF = 1.2


def rounded_box(width, depth, height, radius, center):
    shape = Box(width, depth, height, align=(Align.CENTER, Align.CENTER, Align.CENTER))
    shape = fillet(shape.edges(), radius=radius)
    return Pos(*center) * shape


def gen_step():
    # Feet and legs overlap slightly at the center and fuse into the torso.
    left_leg = rounded_box(
        LEG_WIDTH,
        LEG_DEPTH,
        LEG_HEIGHT,
        2.5,
        (-STUD_PITCH / 2, 0, LEG_HEIGHT / 2),
    )
    right_leg = rounded_box(
        LEG_WIDTH,
        LEG_DEPTH,
        LEG_HEIGHT,
        2.5,
        (STUD_PITCH / 2, 0, LEG_HEIGHT / 2),
    )
    torso = rounded_box(
        TORSO_WIDTH,
        TORSO_DEPTH,
        TORSO_HEIGHT,
        4.0,
        (0, 0, LEG_HEIGHT + TORSO_HEIGHT / 2 - 1.0),
    )

    shoulder_z = LEG_HEIGHT + TORSO_HEIGHT - 5.0
    left_arm = rounded_box(
        ARM_WIDTH,
        ARM_DEPTH,
        ARM_HEIGHT,
        4.0,
        (-(TORSO_WIDTH / 2 + ARM_WIDTH / 2 - 1.5), 0, shoulder_z - ARM_HEIGHT / 2),
    )
    right_arm = rounded_box(
        ARM_WIDTH,
        ARM_DEPTH,
        ARM_HEIGHT,
        4.0,
        ((TORSO_WIDTH / 2 + ARM_WIDTH / 2 - 1.5), 0, shoulder_z - ARM_HEIGHT / 2),
    )

    head_z = LEG_HEIGHT + TORSO_HEIGHT + HEAD_HEIGHT / 2 - 3.0
    head = rounded_box(HEAD_WIDTH, HEAD_DEPTH, HEAD_HEIGHT, 7.0, (0, 0, head_z))
    figure = left_leg + right_leg + torso + left_arm + right_arm + head

    # Two vertical sockets open from the underside of the feet.
    for x in (-STUD_PITCH / 2, STUD_PITCH / 2):
        socket = Pos(x, 0, 0) * Cylinder(
            SOCKET_DIAMETER / 2,
            SOCKET_DEPTH,
            align=(Align.CENTER, Align.CENTER, Align.MIN),
        )
        figure = figure - socket

    # Raised mask eyes on the front face.
    front_y = -(HEAD_DEPTH / 2 + RELIEF * 0.35)
    eye_z = head_z + 1.5
    for x in (-7.0, 7.0):
        eye = Sphere(5.0).scale(0.72)
        figure = figure + Pos(x, front_y, eye_z) * eye

    # Bold raised web motif: center spine plus horizontal bands on mask/torso.
    spine = Box(1.4, RELIEF, 43.0, align=(Align.CENTER, Align.CENTER, Align.CENTER))
    figure = figure + Pos(0, -(TORSO_DEPTH / 2 + RELIEF / 2 - 0.2), 48.0) * spine

    for z, width, face_y in (
        (head_z - 5.0, 24.0, front_y),
        (head_z + 7.0, 20.0, front_y),
        (LEG_HEIGHT + 12.0, 24.0, -(TORSO_DEPTH / 2 + RELIEF / 2 - 0.2)),
        (LEG_HEIGHT + 23.0, 27.0, -(TORSO_DEPTH / 2 + RELIEF / 2 - 0.2)),
    ):
        band = Box(width, RELIEF, 1.4, align=(Align.CENTER, Align.CENTER, Align.CENTER))
        figure = figure + Pos(0, face_y, z) * band

    # A robust spider chest emblem made from a central body and eight short legs.
    emblem_y = -(TORSO_DEPTH / 2 + RELIEF * 0.65)
    emblem_z = LEG_HEIGHT + 17.0
    emblem = Pos(0, emblem_y, emblem_z) * Sphere(2.8)
    for sx in (-1, 1):
        for dz in (-5.0, -2.0, 2.0, 5.0):
            leg = Box(6.5, RELIEF, 1.4, align=(Align.CENTER, Align.CENTER, Align.CENTER))
            emblem = emblem + Pos(sx * 4.0, emblem_y, emblem_z + dz) * leg
    figure = figure + emblem

    figure.label = "duplo_spider_figure"
    return figure


