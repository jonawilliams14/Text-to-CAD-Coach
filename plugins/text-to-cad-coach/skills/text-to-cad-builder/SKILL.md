---
name: text-to-cad-builder
description: Create, modify, export, and validate parametric CAD parts from natural-language requirements or a completed Text-to-CAD specification. Use for Python CAD source, STEP/STP generation, STL/3MF export, geometry inspection, dimensional changes, fit coupons, printable parts, and assemblies. If essential fit-critical requirements are missing, invoke the bundled requirements coach before modeling.
---

# Text-to-CAD Builder

Create the requested CAD model end to end. Prefer the target repository's existing CAD library and conventions. If none exist, prefer build123d; use CadQuery when it is already installed or better matches the project.

## Route incomplete requests

Inspect the request before editing. If missing information could substantially change topology, mating geometry, overall size, or manufacturing method, use the bundled `text-to-cad-requirements-coach` skill first. Otherwise proceed with explicit, conservative assumptions.

Do not ask the user to restate information already present in the conversation or requirements handoff.

## Build workflow

1. Classify the work as a new part, assembly, modification, fit coupon, or export/inspection task.
2. Create a compact internal brief containing dimensions, coordinate convention, parameters, manufacturing constraints, outputs, and acceptance criteria.
3. Inspect the target repository and follow its CAD library, file naming, and export patterns.
4. Define named parameters for dimensions likely to change. Keep the geometry simple and directly traceable to the specification.
5. Edit parametric source rather than generated artifacts. Use millimeters, the XY base plane, and positive Z unless the specification says otherwise.
6. Generate STEP as the primary artifact. Generate STL or 3MF only when requested or needed for printing.
7. Validate the model using the checks in [validation.md](references/validation.md).
8. Repair the smallest responsible source section and regenerate when a check fails.
9. Present created files, checks actually run, assumptions, and any dimensions still requiring physical calibration.

## Modeling rules

- Produce closed, positive-volume solids unless surfaces are explicitly requested.
- Keep source and generated files together and use matching basenames when practical.
- Expose critical dimensions as clearly named constants or function parameters.
- Preserve separate solids or an assembly when parts move, print separately, or require distinct materials.
- Add fillets, chamfers, shells, ribs, or decorative features only when requested or functionally justified.
- Never claim a fit, strength, tolerance, or print result that was not measured or tested.
- For commercial-product compatibility, distinguish measured, nominal, and assumed dimensions.
- For fit-critical printed features, generate a small coupon with several clearance variants before the full part when practical.

## Tool selection

Use an installed CAD skill or repository toolchain when available. When no specialized tool exists, run the generated Python source directly with the active project interpreter. Do not install large CAD dependencies unless generation requires them and the user approves the installation.

When a render/viewer skill is available, hand created STEP/STL/3MF files to it after geometric validation. A render supplements dimensional checks; it does not replace them.

## Required output

For a completed build, report:

- Parametric source path.
- STEP path and any requested secondary exports.
- Bounding box, solid count, and validity result when tools expose them.
- Acceptance criteria checked and their results.
- Assumptions and calibration caveats.
- Viewer link or preview result when available.

Do not report a check as passed unless it actually ran or follows directly from inspected geometry output.

