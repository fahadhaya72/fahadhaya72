# Update imedeatily 

import json
from datetime import datetime

with open("stats.json") as f:
    stats = json.load(f)

updated = datetime.utcnow().strftime("%Y-%m-%d")

terminal = f"""
┌──────────────────────────────────────┐
│ FHD Competitive Programming           │
├──────────────────────────────────────┤
│ LeetCode      {str(stats['leetcode']).ljust(12)} │
│ Codeforces    {str(stats['codeforces']).ljust(12)} │
│ CodeChef      {str(stats['codechef']).ljust(12)} │
│ GFG           {str(stats['gfg']).ljust(12)} │
│ HackerRank    {str(stats['hackerrank']).ljust(12)} │
├──────────────────────────────────────┤
│ Total Solved  {str(stats['total']).ljust(12)} │
├──────────────────────────────────────┤
│ Updated: {updated}                    │
└──────────────────────────────────────┘
"""

svg = f"""<svg xmlns="http://www.w3.org/2000/svg"
     width="900"
     height="350"
     viewBox="0 0 900 350">
    <rect width="100%" height="100%" fill="#0d1117"/>
    <rect x="20" y="20" width="860" height="310" rx="10"
          fill="#161b22" stroke="#00ff88" stroke-width="2"/>
    <text x="40" y="60" fill="#00ff88" font-family="monospace"
          font-size="22" xml:space="preserve">{terminal}</text>
</svg>
"""

with open("assests/coding_dashboard.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("SVG generated successfully")
