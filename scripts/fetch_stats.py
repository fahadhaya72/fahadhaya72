import requests
import json

USERNAMES = {
    "leetcode": "cyberfahad72",
    "codeforces": "MeowBark",
    "gfg": "cyberfahad72",
    "codechef": "cyberfahad72",
    "hackerrank": "cyberfahad72"
}

stats = {}

# =========================
# LeetCode
# =========================

query = """
query userProfile($username: String!) {
  matchedUser(username: $username) {
    submitStats {
      acSubmissionNum {
        difficulty
        count
      }
    }
  }
}
"""

try:
    r = requests.post(
        "https://leetcode.com/graphql",
        json={
            "query": query,
            "variables": {
                "username": USERNAMES["leetcode"]
            }
        },
        timeout=20
    )

    data = r.json()

    total = sum(
        item["count"]
        for item in data["data"]["matchedUser"]["submitStats"]["acSubmissionNum"]
        if item["difficulty"] != "All"
    )

    stats["leetcode"] = total

except Exception:
    stats["leetcode"] = 0


# =========================
# Codeforces
# =========================

try:
    r = requests.get(
        f"https://codeforces.com/api/user.status?handle={USERNAMES['codeforces']}",
        timeout=20
    )

    accepted = set()

    for sub in r.json()["result"]:
        if sub.get("verdict") == "OK":
            problem = (
                str(sub["problem"].get("contestId", ""))
                + sub["problem"].get("index", "")
            )
            accepted.add(problem)

    stats["codeforces"] = len(accepted)

except Exception:
    stats["codeforces"] = 0


# =========================
# Temporary values
# Replace later with scraping
# =========================

stats["gfg"] = 36
stats["codechef"] = 0
stats["hackerrank"] = 92


# =========================
# Total
# =========================

stats["total"] = (
    stats["leetcode"]
    + stats["codeforces"]
    + stats["gfg"]
    + stats["codechef"]
    + stats["hackerrank"]
)

with open("stats.json", "w") as f:
    json.dump(stats, f, indent=4)

print("stats.json generated")
