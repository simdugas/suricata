import requests
import argparse

parser = argparse.ArgumentParser(prog='submit', description='Lightweight script to trigger local docker buildbot builds for newer buildbot versions')
parser.add_argument('-u', '--username', help='format is "FirstName LastName <email@address>"')
parser.add_argument('-b', '--branch', help='branch to build"')

args = parser.parse_args()

BASE_URI = "http://localhost:8010"
API_URI = f"{BASE_URI}/api/v2"
FORCE_URI = f"{API_URI}/forceschedulers/force"

print(FORCE_URI)
result = requests.post(FORCE_URI, json={
    "jsonrpc": "2.0",
    "method": "force",
    "owner": args.username,
    "id": "force",
    "params": {
        "username": args.username,
        "reason": f"Testing branch {args.branch}",
        "branch": args.branch,
        "project": "suricata",
    },
})
print(result.text)

