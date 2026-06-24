import json
from datetime import datetime

with open("stats.json", "r") as f:
    stats = json.load(f)

updated = datetime.utcnow().strftime("%Y-%m-%d")

svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
width="1000"
height="450"
viewBox="0 0 1000 450">

<rect width="100%" height="100%" fill="#0d1117"/>

<rect x="20"
      y="20"
      width="960"
      height="410"
      rx="15"
      fill="#161b22"
      stroke="#00ff88"
      stroke-width="2"/>

<text x="40"
      y="70"
      fill="#00ff88"
      font-family="monospace"
      font-size="28"
      font-weight="bold">
FHD Competitive Programming
</text>

<line x1="40" y1="95" x2="940" y2="95"
      stroke="#00ff88"
      stroke-width="2"/>

<text x="50" y="150"
      fill="white"
      font-family="monospace"
      font-size="24">
LeetCode      : {stats["leetcode"]}
</text>

<text x="50" y="200"
      fill="white"
      font-family="monospace"
      font-size="24">
Codeforces    : {stats["codeforces"]}
</text>

<text x="50" y="250"
      fill="white"
      font-family="monospace"
      font-size="24">
CodeChef      : {stats["codechef"]}
</text>

<text x="50" y="300"
      fill="white"
      font-family="monospace"
      font-size="24">
GeeksforGeeks : {stats["gfg"]}
</text>

<text x="50" y="350"
      fill="white"
      font-family="monospace"
      font-size="24">
HackerRank    : {stats["hackerrank"]}
</text>

<line x1="40" y1="380" x2="940" y2="380"
      stroke="#00ff88"
      stroke-width="2"/>

<text x="50"
      y="415"
      fill="#00ff88"
      font-family="monospace"
      font-size="28"
      font-weight="bold">
Total Solved : {stats["total"]}
</text>

<text x="720"
      y="415"
      fill="#888888"
      font-family="monospace"
      font-size="18">
Updated: {updated}
</text>

</svg>'''

with open("assets/coding_dashboard.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("SVG generated successfully")
