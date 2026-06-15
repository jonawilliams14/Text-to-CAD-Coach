# CAD Validation Checklist

Run the checks supported by the active CAD library and repository tooling.

## Required Checks

1. Source executes without errors.
2. STEP export exists and can be reopened or inspected.
3. Geometry contains the expected number of solids.
4. Each intended part has positive volume and valid closed topology.
5. Bounding-box dimensions match the specification within stated tolerance.
6. Critical diameters, spacing, thicknesses, and clearances match named parameters.
7. Separate parts do not unintentionally intersect in their assembled position.
8. Requested STL/3MF exports derive from the validated source geometry.

## Printability Checks

- Walls and small features meet the stated process minimums.
- Holes, bridges, and overhangs are compatible with the planned orientation or are marked as requiring supports.
- Functional loads are not concentrated across weak layer directions without acknowledgment.
- Fit-critical values are identified as measured, nominal, or assumed.
- A tolerance coupon is included when printer calibration materially affects success.

## Reporting

Report measured values from the tools, not intended values from source constants. If a check cannot run, identify it as unverified and explain the practical test needed.

