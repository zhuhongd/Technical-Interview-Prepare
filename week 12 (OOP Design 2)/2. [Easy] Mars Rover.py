r"""
Mars Rover — EECS4070 (Top‑Down Design + Clean OOP + Clear Tests)

Problem
-------
Simulate a Mars Rover moving on a rectangular plateau (grid). A rover has a position (x, y)
with an orientation facing one of {N, E, S, W}. It executes a command string over the alphabet:
- 'L' : turn left (90° counter‑clockwise)
- 'R' : turn right (90° clockwise)
- 'M' : move forward one cell in the current direction

The rover must remain within plateau bounds. (Out‑of‑bounds moves become no‑ops.)
Optionally, with multiple rovers on the same plateau, moving into an occupied cell is disallowed
and becomes a no‑op (we keep the simple rule here; you can choose to raise instead).

Goal
----
Given plateau size and rover(s) with initial states and command strings, return the final
position(s) and headings.

Link
----
Classic interview prompt; a common variant appears in many OOD katas.

Top‑Down Design
---------------
1) **Grid/Plateau** — knows width/height and (optionally) occupied cells.
   - `in_bounds(x, y)`
   - `is_free(x, y)` and `occupy`/`release` when we track collisions.

2) **Rover** — owns (x, y, dir). Pure operations:
   - `turn_left()`, `turn_right()` → update orientation
   - `forward()` → propose next (x', y')
   - `execute(cmds)` → iterate commands, apply with plateau checks

3) **Orientation** — map to motion deltas and left/right transitions via small lookup tables.

Conventions
-----------
- Coordinates are 0‑based. Grid is `0..max_x` × `0..max_y` **inclusive**.
- On an out‑of‑bounds or into‑occupied forward move, we do **no‑op** and continue.
- Invalid command characters are ignored (or could raise — here we ignore).

Complexity
----------
Each command runs in **O(1)** (pure table lookups and a couple of checks). Total is O(#commands).
"""

from dataclasses import dataclass
from typing import List, Tuple, Set, Dict

# ----------------------------------
# Orientation helpers
# ----------------------------------
LEFT = {"N": "W", "W": "S", "S": "E", "E": "N"}
RIGHT = {"N": "E", "E": "S", "S": "W", "W": "N"}
STEP = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}


class Plateau:
    """Rectangular grid with optional collision tracking.

    Bounds are inclusive: valid x in [0, max_x], valid y in [0, max_y].
    """

    def __init__(self, max_x: int, max_y: int, track_collisions: bool = True):
        assert max_x >= 0 and max_y >= 0
        self.max_x = max_x
        self.max_y = max_y
        self.track = track_collisions
        self.occ: Set[Tuple[int, int]] = set()

    # ---- bounds & occupancy ----
    def in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x <= self.max_x and 0 <= y <= self.max_y

    def is_free(self, x: int, y: int) -> bool:
        return (not self.track) or ((x, y) not in self.occ)

    def occupy(self, x: int, y: int) -> None:
        if self.track:
            self.occ.add((x, y))

    def release(self, x: int, y: int) -> None:
        if self.track:
            self.occ.discard((x, y))


@dataclass
class Rover:
    x: int
    y: int
    dir: str  # one of N,E,S,W
    grid: Plateau

    def turn_left(self) -> None:
        self.dir = LEFT[self.dir]

    def turn_right(self) -> None:
        self.dir = RIGHT[self.dir]

    def forward(self) -> None:
        dx, dy = STEP[self.dir]
        nx, ny = self.x + dx, self.y + dy
        if self.grid.in_bounds(nx, ny) and self.grid.is_free(nx, ny):
            # move: update occupancy if tracking
            self.grid.release(self.x, self.y)
            self.x, self.y = nx, ny
            self.grid.occupy(self.x, self.y)
        # else: no‑op (blocked by bounds or another rover)

    def execute(self, commands: str) -> None:
        for c in commands:
            if c == 'L':
                self.turn_left()
            elif c == 'R':
                self.turn_right()
            elif c == 'M':
                self.forward()
            else:
                # ignore unknown commands
                continue

    def state(self) -> Tuple[int, int, str]:
        return (self.x, self.y, self.dir)


# ----------------------------------
# Teaching helpers (optional)
# ----------------------------------

def _snapshot(grid: Plateau, rovers: List[Rover]) -> str:
    """ASCII top‑down view: y=max..0, x=0..max. N/E/S/W on rover cells."""
    # Build a map from (x,y) to symbol
    sym: Dict[Tuple[int, int], str] = {}
    for r in rovers:
        sym[(r.x, r.y)] = r.dir
    lines: List[str] = []
    for y in range(grid.max_y, -1, -1):
        row = []
        for x in range(0, grid.max_x + 1):
            row.append(sym.get((x, y), '.'))
        lines.append(' '.join(row))
    return '\n'.join(lines)


# ----------------------------------
# Clear Offline Tests
# ----------------------------------

def _run_tests() -> None:
    # Test 1 — Classic NASA kata examples
    print("\n[Test 1] Classic examples (plateau 5x5)")
    g = Plateau(5, 5, track_collisions=True)
    r1 = Rover(1, 2, 'N', g)
    r2 = Rover(3, 3, 'E', g)
    # mark starting occupancy
    g.occupy(r1.x, r1.y)
    g.occupy(r2.x, r2.y)
    r1.execute("LMLMLMLMM")
    r2.execute("MMRMMRMRRM")
    print("r1:", r1.state(), "expected -> (1, 3, 'N')")
    print("r2:", r2.state(), "expected -> (5, 1, 'E')")
    assert r1.state() == (1, 3, 'N')
    assert r2.state() == (5, 1, 'E')

    # Test 2 — Out‑of‑bounds moves become no‑ops
    print("\n[Test 2] Bounds (no‑op when moving outside)")
    g2 = Plateau(2, 2, track_collisions=False)
    r = Rover(0, 0, 'S', g2)  # facing south at lower edge
    r.execute("MMMR")  # M's should no‑op; then a right turn
    print("state:", r.state(), "expected -> (0, 0, 'W')")
    assert r.state() == (0, 0, 'W')

    # Test 3 — Multiple rovers with collision rule: stay put if target occupied
    print("\n[Test 3] Collision avoidance (no‑op into occupied)")
    g3 = Plateau(3, 1, track_collisions=True)
    a = Rover(0, 0, 'E', g3)
    b = Rover(2, 0, 'W', g3)
    g3.occupy(a.x, a.y)
    g3.occupy(b.x, b.y)
    a.execute("M")  # a -> (1,0)
    b.execute("M")  # b would like (1,0) but it's occupied; no‑op
    print(_snapshot(g3, [a, b]))
    print("a:", a.state(), "expected -> (1, 0, 'E')")
    print("b:", b.state(), "expected -> (2, 0, 'W')")
    assert a.state() == (1, 0, 'E')
    assert b.state() == (2, 0, 'W')

    # Test 4 — Ignore unknown commands
    print("\n[Test 4] Unknown commands are ignored")
    g4 = Plateau(1, 1)
    r = Rover(0, 0, 'N', g4)
    g4.occupy(0, 0)
    r.execute("M?R!M")  # '?' and '!' ignored
    print("state:", r.state(), "expected -> (1, 1, 'E')")
    assert r.state() == (1, 1, 'E')

    print("\nAll tests passed. ✅")


if __name__ == "__main__":
    _run_tests()
