# Text-to-CAD Coach

A Codex plugin that turns rough physical-part ideas into measurable, printable CAD requirements and self-contained implementation prompts.

The coach asks focused questions about geometry, mating interfaces, dimensions, fit, manufacturing constraints, and validation. It is especially useful for 3D-printed parts that must connect to existing objects, including Duplo-compatible designs.

## What It Does

- Asks up to three high-value refining questions at a time.
- Separates confirmed measurements, nominal references, and assumptions.
- Identifies missing dimensions that would materially change the model.
- Covers printer, material, nozzle, support, and orientation constraints.
- Recommends fit coupons for mating and clutch features.
- Produces a structured requirements specification.
- Produces a copy-ready prompt for a text-to-CAD implementation agent.

## Install in Codex

Add this repository as a plugin marketplace:

```powershell
codex plugin marketplace add jonawilliams14/Text-to-CAD-Coach
```

Install the plugin:

```powershell
codex plugin add text-to-cad-coach@text-to-cad-local
```

Start a new Codex thread after installation. Invoke the plugin explicitly with:

```text
@text-to-cad-coach Help me refine an idea into a CAD-ready specification.
```

Codex may also invoke the bundled skill automatically when a request matches its description.

## Example

```text
@text-to-cad-coach Help me design a removable platform that connects a
miniature spiral staircase to a Duplo set.
```

The coach will first establish the connection direction, footprint, measured mating dimensions, desired clutch strength, and printing process. It will not invent proprietary compatibility dimensions.

## Repository Structure

```text
.agents/plugins/marketplace.json
plugins/text-to-cad-coach/
  .codex-plugin/plugin.json
  skills/text-to-cad-requirements-coach/
    SKILL.md
    references/
```

## Development

Validate the plugin with Codex's `plugin-creator` validator:

```powershell
python scripts/validate_plugin.py <path-to-plugin>
```

After changing an installed local plugin, update its cachebuster or reinstall it, then test from a new Codex thread.

## License

MIT
