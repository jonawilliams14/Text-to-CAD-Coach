# DUPLO-Scale Spider Figure

This example is a one-piece, non-articulated, spider-hero figure sized for
DUPLO-style play. It has a chunky printable silhouette, raised mask and chest
details, and two sockets beneath the feet.

## Files

- `duplo_spider_figure.py`: parametric build123d source exposing `gen_step()`.
- `duplo_spider_figure.stl`: generated binary print mesh.

## Geometry

- Overall envelope: 48.0 x 32.02 x 78.0 mm.
- Body: one connected solid.
- Foot socket pitch: 16.0 mm (`assumed`).
- Foot socket diameter: 9.8 mm (`assumed`).
- Foot socket depth: 4.2 mm (`assumed`).

The socket dimensions are calibration starting points, not guaranteed
commercial-brick dimensions. Measure the actual mating studs and print a small
socket coupon with the intended printer, material, orientation, and slicer
settings before printing the complete figure.

## Validation

The source and included STL were checked as:

- one valid, positive-volume source solid;
- 48.0 x 32.02 x 78.0 mm source bounding box;
- 20,130 STL triangles with a valid binary STL record size;
- build-plane minimum at approximately Z = 0 mm.

The STL has not been certified for a particular slicer. Run the slicer's mesh
repair and preview checks before printing.


