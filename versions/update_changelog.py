import os
import sys
import json
from datetime import date
from argparse import ArgumentParser

def main():
  parser = ArgumentParser()
  parser.add_argument("--af-version", dest="af_version", required=True)
  parser.add_argument("--build-version", dest="build_version", required=True)
  parser.add_argument("--changelog-new", dest="changelog_new", required=True)
  parser.add_argument("--changelog-fixes", dest="changelog_fixes", required=True)
  args = parser.parse_args()

  args.changelog_new = json.loads(args.changelog_new)
  args.changelog_fixes = json.loads(args.changelog_fixes)

  cl_path = os.path.join("versions", args.af_version, "CHANGELOG.md")
  if os.path.exists(cl_path):
    with open(cl_path) as f:
      cl_lines = f.readlines()
      cl_lines = [line.rstrip('\n') for line in cl_lines]
  else:
    cl_lines = ["# Changelog"]

  if cl_lines[0] != "# Changelog":
    sys.exit("Invalid changelog format to modify")

  to_insert = []
  if len(args.changelog_new) != 0:
    to_insert += ["### New"] + args.changelog_new
  if len(args.changelog_fixes) != 0:
    to_insert += ["### Fixed"] + args.changelog_fixes

  if len(to_insert) == 0:
    sys.exit("At least one changelog line should be specified")

  today_date = date.today().strftime("%d.%m.%y")
  to_insert = [
    f"DoubleCloud Airflow Base Image {args.af_version}-{args.build_version}, {today_date}",
    "----------------------------------------",
    "",
  ] + to_insert

  cl_lines = cl_lines[:1] + [""] + to_insert + cl_lines[1:]
  with open(cl_path, 'w') as f:
    f.writelines([x + "\n" for x in cl_lines])

if __name__ == '__main__':
  main()
