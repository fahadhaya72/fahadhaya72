import json
from datetime import datetime

with open("stats.json") as f:
    stats = json.load(f)

updated = datetime.utcnow().strftime("%Y-%m-%d")

svg = f"""
<svg width="900" height="450"
xmlns="http://www.w3.org/2000/svg">

<style>
.title {{
    font: bold 32px monospace;
    fill: #00ff88;
}}

.text {{
    font: 22px monospace;
    fill: #ffffff;
}}

.total {{
    font: bold 28px monospace;
    fill: #00ff88;
}}

.small {{
    font: 16px monospace;
    fill: #888888;
}}
</style>

<rect
width="100%"
height="100%"
fill="#0d1117"
/>

<rect
x="20"
y="20"
width="860"
height="410"
rx="15"
fill="#161b22"
stroke="#00ff88"
stroke-width="2"
/>

<text
x="40"
y="70"
class="title">
FHD Coding Command Center
</text>

<text x="50" y="130" class="text">
▶ LeetCode      : {stats['leetcode']}
</text>

<text x="50" y="180" class="text">
▶ Codeforces    : {stats['codeforces']}
</text>

<text x="50" y="230" class="text">
▶ CodeChef      : {stats['codechef']}
</text>

<text x="50" y="280" class="text">
▶ GeeksforGeeks : {stats['gfg']}
</text>

<text x="50" y="330" class="text">
▶ HackerRank    : {stats['hackerrank']}
</text>

<line
x1="40"
y1="360"
x2="850"
y2="360"
stroke="#00ff88"
/>

<text
x="50"
y="405"
class="total">
TOTAL PLATFORM SOLVES : {stats['total']}
</text>

<text
x="650"
y="405"
class="small">
Updated: {updated}
</text>

</svg>
"""

with open("assets/coding_dashboard.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("SVG generated successfully")
