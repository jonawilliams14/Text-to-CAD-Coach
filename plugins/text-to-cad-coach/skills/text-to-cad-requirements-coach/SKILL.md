---
name: text-to-cad-requirements-coach
description: Refine rough physical-part and 3D-printing ideas into measurable CAD requirements, then hand ready specifications to the bundled Text-to-CAD builder. Use for dimensional discovery, mating-fit questions, print constraints, Duplo-compatible parts, prompt review, and requirements handoff.
---

# Text-to-CAD Requirements Coach

Turn an early physical-product idea into an unambiguous specification for a parametric text-to-CAD workflow. Remain in coaching mode until the requirements are ready.

## Start the session

1. Restate the intended object and use in one or two sentences.
2. Record these four items briefly before asking questions:
   - User goal.
   - Assumptions that affect the result.
   - Smallest reasonable scope.
   - Important tradeoffs or risks.
3. Ask no more than three questions at a time. Ask the questions whose answers most affect topology, fit, strength, printability, or compatibility.
4. Offer a concise recommended default when the user may not know the CAD terminology.

## Track evidence

Never invent dimensions. Label dimensions and other material decisions as:

- `confirmed`: supplied or measured by the user.
- `nominal`: taken from a cited specification or reference.
- `assumed`: a proposed starting value that needs approval or testing.

Use millimeters unless requested otherwise. Preserve both original and converted values when converting units.

Treat compatibility with commercial products as a fit requirement rather than a guarantee. Ask the user to measure the actual mating object. Recommend a small tolerance coupon before a complete print whenever printer calibration, shrinkage, or clutch force can affect success.

## Discover requirements

Cover the following topics, skipping anything irrelevant or already answered:

1. Purpose and scope: intended use, user, required features, and explicit exclusions.
2. Interfaces: mating objects, surfaces, studs, tubes, holes, fasteners, and connection direction.
3. Dimensions: overall envelope, critical feature sizes, pitch, wall thickness, and clearances.
4. Behavior: fixed or moving parts, loads, assembly, orientation, and desired looseness or retention.
5. Manufacturing: process, printer, material, nozzle or minimum feature size, supports, layer orientation, and separate parts.
6. Appearance: shape language, symmetry, edge treatment, text, and finish.
7. Deliverables: parametric source, STEP, STL/3MF, drawings, assemblies, and file names.
8. Validation: measurements, fit coupons, interference checks, and observable acceptance criteria.

Prioritize interfaces and critical dimensions over appearance. For mating features, identify whether the intended fit is clearance, sliding, friction, snap, or press.

For Duplo-compatible work, establish at minimum:

- Exact mating object and whether connection is on top, bottom, or both.
- Stud or tube count and layout.
- Measured center-to-center pitch and mating diameters.
- Available insertion depth and surrounding wall thickness.
- Desired clutch strength, printer, and material.
- Whether a fit coupon should precede the complete model.

Do not assume published brick dimensions compensate for the user's printer, material, slicer settings, or specific mating part.

## Decide readiness

Do not call the requirements ready while a missing answer could substantially change topology, mating geometry, overall size, or manufacturing method.

When only low-risk details remain, propose conservative defaults and ask for approval. When material information is missing, provide a short `Still needed` list and continue coaching.

## Produce the handoff

Once ready, create both outputs below. If the user asked to create the model, continue directly with the bundled `text-to-cad-builder` skill using the completed specification. Do not make the user repeat the request.

### 1. Requirements specification

Use the complete format in [requirements-template.md](references/requirements-template.md). Include assumptions and confidence labels directly in the specification.

### 2. Copy-ready implementation prompt

Write a compact prompt addressed to the bundled Text-to-CAD builder. It must stand alone without relying on the conversation. Include every critical dimension, coordinate convention, manufacturing constraint, named source parameter, deliverable, and acceptance criterion.

For mating geometry, include the fit-test plan and state which dimensions remain subject to calibration. Prefer the simplest geometry that meets the stated need and do not add speculative features or configurability.

Use [duplo-compatible-platform.md](references/duplo-compatible-platform.md) as an example of the questioning and validation pattern, not as a source of dimensions.

