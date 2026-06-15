# Text-to-CAD

An end-to-end Codex plugin that turns rough physical-part ideas into validated parametric CAD files.

The plugin bundles two cooperating skills:

- **Requirements Coach:** asks focused questions, records measurement confidence, and produces an implementation-ready specification.
- **CAD Builder:** writes parametric Python, generates STEP-first geometry, exports requested STL/3MF files, and validates the result.

## Capabilities

- Refine dimensions, interfaces, fit, manufacturing constraints, and acceptance criteria.
- Distinguish confirmed, nominal, and assumed dimensions.
- Generate parametric CAD source using the repository's existing CAD library.
- Produce STEP as the primary artifact and optional STL/3MF exports.
- Check source execution, solid validity, bounding dimensions, critical features, and printability.
- Generate tolerance coupons before fit-critical parts when practical.
- Hand supported files to an available CAD viewer.

The CAD Python library and any viewer remain local runtime dependencies. The plugin orchestrates those tools rather than embedding a CAD kernel.

## Install

```powershell
codex plugin marketplace add jonawilliams14/Text-to-CAD-Coach
codex plugin add text-to-cad-coach@text-to-cad-local
```

Start a new Codex thread after installation.

## Use

Refine an idea and build it:

```text
@text-to-cad-coach Design and generate a removable Duplo-compatible
platform for a miniature spiral staircase.
```

Build from complete requirements:

```text
@text-to-cad-coach Create a 60 x 40 x 4 mm mounting plate with four
4.5 mm corner holes, then export validated STEP and STL files.
```

The plugin will route incomplete fit-critical requests through the coach and send ready specifications directly to the builder.

## Structure

```text
.agents/plugins/marketplace.json
plugins/text-to-cad-coach/
  .codex-plugin/plugin.json
  skills/
    text-to-cad-requirements-coach/
    text-to-cad-builder/
```

## Runtime

Use an existing project CAD environment when possible. The builder prefers build123d when starting fresh and supports CadQuery projects by following their existing conventions.

## License

MIT
