#!/usr/bin/env python3
"""One test per mechanical check, plus palette and determinism tests.

Run from the repository root:
    python3 scripts/tests/test_diagram.py
"""

from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from importlib.machinery import SourceFileLoader
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKILL = ROOT / "skills" / "productivity" / "create-diagram"
SCRIPT = ROOT / "scripts" / "diagram"
FIXTURES = Path(__file__).resolve().parent / "fixtures"

loader = SourceFileLoader("diagram_tool", str(SCRIPT))
spec = importlib.util.spec_from_loader("diagram_tool", loader)
diagram = importlib.util.module_from_spec(spec)
loader.exec_module(diagram)


def load(name: str) -> dict:
    return json.loads((SKILL / name).read_text(encoding="utf-8"))


def compile_clean() -> tuple[dict, dict, dict]:
    plan = load("examples/plan.json")
    palette = diagram.load_palette(str(SKILL / "examples" / "palette.json"))
    shape = diagram.plan_shape(plan)
    page = diagram.plan_page(plan, shape)
    output = diagram.compile_plan(plan, palette, json.dumps(plan).encode(), shape, page)
    return plan, palette, output


def findings_for(plan, palette, output, only=None) -> list[tuple[int, str]]:
    sink = diagram.Findings()
    diagram.check(plan, output, palette, sink, None, SKILL)
    return [item for item in sink.items if not only or item[0] in only]


class CleanPlan(unittest.TestCase):
    def test_clean_plan_has_no_findings(self):
        plan, palette, output = compile_clean()
        self.assertEqual(findings_for(plan, palette, output), [])

    def test_every_edge_has_an_arrow(self):
        plan, _, output = compile_clean()
        ids = {el["id"] for el in output["elements"] if el["type"] == "arrow"}
        self.assertEqual(ids, {edge["id"] for edge in plan["edges"]})

    def test_recompile_is_byte_identical(self):
        plan, palette, _ = compile_clean()
        shape = diagram.plan_shape(plan)
        page = diagram.plan_page(plan, shape)
        first = json.dumps(diagram.compile_plan(plan, palette, b"x", shape, dict(page)), sort_keys=True)
        second = json.dumps(diagram.compile_plan(plan, palette, b"x", shape, dict(page)), sort_keys=True)
        self.assertEqual(first, second)


class Traps(unittest.TestCase):
    def setUp(self):
        self.plan, self.palette, self.output = compile_clean()
        self.page = self.output["_diagram"]["page"]

    def test_crossing_fires_c16(self):
        output = copy.deepcopy(self.output)
        arrow = next(el for el in output["elements"] if el["id"] == "e_client")
        y = arrow["y"] + 60
        output["elements"].append(
            {
                **copy.deepcopy(arrow),
                "id": "trap",
                "x": arrow["x"] - 50,
                "y": y - 20,
                "width": 400,
                "height": 0,
                "points": [[0, 0], [400, 0]],
                "startBinding": None,
                "endBinding": None,
                "customData": {"kind": "edge"},
            }
        )
        numbers = {number for number, _ in findings_for(self.plan, self.palette, output, {16})}
        self.assertIn(16, numbers)

    def test_wrong_port_fires_c15(self):
        output = copy.deepcopy(self.output)
        arrow = next(el for el in output["elements"] if el["id"] == "e_service")
        arrow["points"][0] = [arrow["points"][0][0], arrow["points"][0][1] + 80]
        numbers = {number for number, _ in findings_for(self.plan, self.palette, output, {15})}
        self.assertIn(15, numbers)

    def test_diagonal_fires_c18(self):
        output = copy.deepcopy(self.output)
        arrow = next(el for el in output["elements"] if el["id"] == "e_db")
        arrow["points"].insert(1, [arrow["points"][1][0] + 17, arrow["points"][1][1] + 17])
        numbers = {number for number, _ in findings_for(self.plan, self.palette, output, {18})}
        self.assertIn(18, numbers)

    def test_out_of_band_fires_c23(self):
        output = copy.deepcopy(self.output)
        node = next(el for el in output["elements"] if el["id"] == "db")
        node["x"] = self.page["width"] - 40
        numbers = {number for number, _ in findings_for(self.plan, self.palette, output, {23})}
        self.assertIn(23, numbers)

    def test_legend_opt_out_is_not_a_finding(self):
        plan = copy.deepcopy(self.plan)
        plan["legend"] = False
        palette = self.palette
        output = diagram.compile_plan(
            plan, palette, json.dumps(plan).encode(), diagram.plan_shape(plan), diagram.plan_page(plan, "stack")
        )
        numbers = {number for number, _ in findings_for(plan, palette, output, {13})}
        self.assertNotIn(13, numbers)

    def test_annotation_inside_a_node_fires_c21(self):
        output = copy.deepcopy(self.output)
        node = next(el for el in output["elements"] if el["id"] == "gateway")
        annotation = next(
            el for el in output["elements"]
            if el.get("customData", {}).get("kind") == "annotation"
        )
        annotation["x"], annotation["y"] = node["x"] + 10, node["y"] + 10
        numbers = {number for number, _ in findings_for(self.plan, self.palette, output, {21})}
        self.assertIn(21, numbers)

    def test_unknown_field_is_refused(self):
        plan = copy.deepcopy(self.plan)
        plan["annontations"] = []
        with self.assertRaises(SystemExit) as caught:
            diagram.compile_plan(
                plan, self.palette, json.dumps(plan).encode(), "stack", diagram.plan_page(plan, "stack")
            )
        self.assertIn("unknown field", str(caught.exception))

    def test_legend_wraps_inside_the_page(self):
        plan = {
            "title": "Five roles",
            "shape": "stack",
            "page": "a4",
            "legend": True,
            "tiers": ["a", "b", "c"],
            "elements": [
                {"id": "n0", "role": "process", "tier": "a", "text": "One"},
                {"id": "n1", "role": "decision", "tier": "a", "text": "Two"},
                {"id": "n2", "role": "outcome", "tier": "b", "text": "Three"},
                {"id": "n3", "role": "exception", "tier": "b", "text": "Four"},
                {"id": "n4", "role": "external", "tier": "c", "text": "Five"},
            ],
            "edges": [
                {"id": "e1", "from": "n0", "to": "n2"},
                {"id": "e2", "from": "n1", "to": "n3"},
                {"id": "e3", "from": "n2", "to": "n4"},
            ],
        }
        shape = diagram.plan_shape(plan)
        page = diagram.plan_page(plan, shape)
        output = diagram.compile_plan(plan, self.palette, json.dumps(plan).encode(), shape, page)
        numbers = {number for number, _ in findings_for(plan, self.palette, output, {23})}
        self.assertNotIn(23, numbers)
        legend = [
            el for el in output["elements"]
            if el.get("customData", {}).get("kind") in ("legend", "legend-label")
        ]
        self.assertTrue(legend)
        self.assertLessEqual(max(el["x"] + el["width"] for el in legend), page["width"] - 20)
        self.assertLessEqual(max(el["y"] + el["height"] for el in legend), page["height"] - 20)

    def test_wide_edge_label_clears_the_tier_label(self):
        plan = {
            "title": "Wide label",
            "shape": "conveyor",
            "page": "a4-landscape",
            "tiers": ["a", "b", "c"],
            "elements": [
                {"id": "n0", "role": "process", "tier": "a", "text": "One"},
                {"id": "n1", "role": "process", "tier": "b", "text": "Two"},
                {"id": "n2", "role": "process", "tier": "c", "text": "Three"},
            ],
            "edges": [
                {"id": "e0", "from": "n0", "to": "n1", "label": "a long relationship label"},
                {"id": "e1", "from": "n1", "to": "n2", "label": "a long relationship label"},
            ],
        }
        output = diagram.compile_plan(
            plan, self.palette, json.dumps(plan).encode(), "conveyor", diagram.plan_page(plan, "conveyor")
        )
        by_id = {el["id"]: el for el in output["elements"]}
        for edge_id, tier_id in (("e0", "a"), ("e1", "b")):
            label, tier = by_id[f"{edge_id}_label"], by_id[f"tier_{tier_id}"]
            self.assertLessEqual(label["y"] + label["height"], tier["y"])

    def test_wide_label_on_a_z_route_clears_its_leg(self):
        plan = {
            "title": "Z route",
            "shape": "stack",
            "tiers": ["a", "b", "c"],
            "elements": [
                {"id": "n0", "role": "start", "tier": "a", "text": "Open PR"},
                {"id": "n1", "role": "process", "tier": "b", "text": "Reviewer"},
                {"id": "n2", "role": "outcome", "tier": "c", "text": "Merge"},
            ],
            "edges": [
                {"id": "e1", "from": "n0", "to": "n1", "label": "requests review"},
                {"id": "e2", "from": "n1", "to": "n2", "label": "approves"},
            ],
        }
        shape = diagram.plan_shape(plan)
        output = diagram.compile_plan(
            plan, self.palette, json.dumps(plan).encode(), shape, diagram.plan_page(plan, shape)
        )
        by_id = {el["id"]: el for el in output["elements"]}
        label = by_id["e1_label"]
        box = diagram.element_box(label)
        for segment in diagram.arrow_segments(by_id["e1"]):
            self.assertFalse(diagram.segment_intersects_box(segment, box, pad=1))

    def test_long_labels_from_one_source_do_not_overlap(self):
        plan = {
            "title": "Fan",
            "shape": "stack",
            "tiers": ["a", "b"],
            "elements": [
                {"id": "q", "role": "process", "tier": "a", "text": "Triage queue"},
                {"id": "e1", "role": "process", "tier": "b", "text": "Engineer"},
                {"id": "e2", "role": "process", "tier": "b", "text": "Known issue"},
            ],
            "edges": [
                {"id": "ea", "from": "q", "to": "e1", "label": "assigned to the on-call engineer who owns it"},
                {"id": "eb", "from": "q", "to": "e2", "label": "matches a known issue already tracked"},
            ],
        }
        shape = diagram.plan_shape(plan)
        output = diagram.compile_plan(
            plan, self.palette, json.dumps(plan).encode(), shape, diagram.plan_page(plan, shape)
        )
        labels = [
            el for el in output["elements"]
            if el.get("customData", {}).get("kind") == "edge-label"
        ]
        numbers = {number for number, _ in findings_for(plan, self.palette, output, {21})}
        self.assertNotIn(21, numbers)
        self.assertFalse(diagram.boxes_overlap(diagram.element_box(labels[0]), diagram.element_box(labels[1])))

    def test_two_branch_ports_follow_target_side(self):
        base = {
            "title": "Decision",
            "shape": "stack",
            "tiers": ["a", "b"],
            "elements": [
                {"id": "s", "role": "decision", "tier": "a", "text": "Scan passes?"},
                {"id": "ok", "role": "outcome", "tier": "b", "text": "Accepted"},
                {"id": "bad", "role": "exception", "tier": "b", "text": "Quarantine"},
            ],
            "edges": [
                {"id": "e_clean", "from": "s", "to": "ok", "label": "clean"},
                {"id": "e_fail", "from": "s", "to": "bad", "label": "fails"},
            ],
        }
        for edges in (base["edges"], list(reversed(base["edges"]))):
            plan = dict(base, edges=edges)
            shape = diagram.plan_shape(plan)
            output = diagram.compile_plan(
                plan, self.palette, json.dumps(plan).encode(), shape, diagram.plan_page(plan, shape)
            )
            numbers = {number for number, _ in findings_for(plan, self.palette, output, {17})}
            self.assertNotIn(17, numbers)

    def test_c27_survives_a_different_host_palette(self):
        plan, _, output = compile_clean()
        other = diagram.load_palette(
            str(ROOT / "evals" / "skills" / "productivity" / "create-diagram" / "fixtures" / "palette-slate.json")
        )
        numbers = {number for number, _ in findings_for(plan, other, output, {27})}
        self.assertNotIn(27, numbers)

    def test_delivered_drift_fires_c27(self):
        output = copy.deepcopy(self.output)
        node = next(el for el in output["elements"] if el["id"] == "gateway")
        node["x"] += 3
        numbers = {number for number, _ in findings_for(self.plan, self.palette, output, {27})}
        self.assertIn(27, numbers)

    def test_stray_hex_fires_c08(self):
        output = copy.deepcopy(self.output)
        node = next(el for el in output["elements"] if el["id"] == "gateway")
        node["backgroundColor"] = "#123456"
        numbers = {number for number, _ in findings_for(self.plan, self.palette, output, {8})}
        self.assertIn(8, numbers)

    def test_clipped_text_fires_c22(self):
        output = copy.deepcopy(self.output)
        node = next(el for el in output["elements"] if el["id"] == "gateway")
        node["width"] = 120
        numbers = {number for number, _ in findings_for(self.plan, self.palette, output, {22})}
        self.assertIn(22, numbers)

    def test_low_contrast_fires_c09(self):
        output = copy.deepcopy(self.output)
        text = next(el for el in output["elements"] if el["id"] == "gateway_t")
        text["strokeColor"] = self.palette["roles"]["process"]["fill"]
        numbers = {number for number, _ in findings_for(self.plan, self.palette, output, {9})}
        self.assertIn(9, numbers)


class Palette(unittest.TestCase):
    def test_vendored_runtime_fires_c28(self):
        plan, palette, output = compile_clean()
        with tempfile.TemporaryDirectory() as directory:
            runtime = Path(directory) / "node_modules" / "pkg"
            runtime.mkdir(parents=True)
            (runtime / "index.js").write_text("x")
            sink = diagram.Findings()
            diagram.check(plan, output, palette, sink, None, Path(directory))
            self.assertIn(28, {number for number, _ in sink.items})

    def test_tampered_variant_fires_c14(self):
        plan, palette, output = compile_clean()
        tampered = copy.deepcopy(output)
        tampered["_diagram"]["palette"]["variant"] = "dark"
        numbers = {number for number, _ in findings_for(plan, palette, tampered, {14})}
        self.assertIn(14, numbers)

    def test_swap_changes_colour_only(self):
        plan = load("examples/plan.json")
        warm = diagram.load_palette(str(SKILL / "examples" / "palette.json"))
        cool = copy.deepcopy(warm)
        cool["roles"] = {
            role: {
                "fill": diagram.mix(warm["canvas"], "#38618c", 0.2),
                "stroke": "#24425f",
                "text": warm["ink"],
            }
            for role in warm["roles"]
        }
        shape = diagram.plan_shape(plan)
        page = diagram.plan_page(plan, shape)
        first = diagram.compile_plan(plan, warm, b"x", shape, dict(page))
        second = diagram.compile_plan(plan, cool, b"x", shape, dict(page))
        for left, right in zip(first["elements"], second["elements"]):
            for key in ("type", "x", "y", "width", "height", "text", "points"):
                self.assertEqual(left.get(key), right.get(key), f"{left['id']}.{key}")

    def test_kitty_adapter(self):
        tokens = diagram.load_palette(str(FIXTURES / "kitty.conf"))
        self.assertEqual(tokens["canvas"].lower(), "#101418")
        self.assertEqual(len(diagram.token_table(tokens)), 7 + 3 * len(diagram.ROLE_SLOTS))

    def test_alacritty_adapter(self):
        tokens = diagram.load_palette(str(FIXTURES / "alacritty.toml"))
        self.assertEqual(tokens["canvas"].lower(), "#101418")

    def test_base16_adapter(self):
        tokens = diagram.load_palette(str(FIXTURES / "base16.yaml"))
        self.assertEqual(tokens["canvas"].lower(), "#fbfaf7")
        self.assertEqual(tokens["variant"], "light")

    def test_pywal_adapter(self):
        tokens = diagram.load_palette(str(FIXTURES / "colors"))
        self.assertEqual(tokens["canvas"].lower(), "#1b1d21")

    def test_contrast_floors_hold(self):
        tokens = diagram.load_palette(str(SKILL / "examples" / "palette.json"))
        for role, entry in tokens["roles"].items():
            self.assertGreaterEqual(diagram.contrast(entry["text"], entry["fill"]), 4.5, role)
            self.assertGreaterEqual(diagram.contrast(entry["stroke"], entry["fill"]), 3, role)
            self.assertGreaterEqual(diagram.contrast(entry["stroke"], tokens["canvas"]), 3, role)


class Render(unittest.TestCase):
    @unittest.skipUnless(diagram.BUNDLE.is_file(), "renderer bundle is not built")
    def test_png_dimensions(self):
        plan, palette, output = compile_clean()
        with tempfile.TemporaryDirectory() as tmp:
            png = Path(tmp) / "plan.png"
            path, width, height = diagram.render(png, output, 2, None)
            self.assertEqual((width, height), (1588, 2246))
            self.assertEqual(path.read_bytes()[:8], b"\x89PNG\r\n\x1a\n")


if __name__ == "__main__":
    unittest.main(verbosity=2)
