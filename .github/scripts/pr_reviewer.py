import os
import re
import sys

def analyze_feature_file(file_path):
    issues = []
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    inside_scenario = False
    first_step_seen = False
    prev_step = ""

    for line_num, raw_line in enumerate(lines, start=1):
        line = raw_line.strip()
        if line.startswith("Scenario:") or line.startswith("Scenario Outline:"):
            inside_scenario = True
            first_step_seen = False
            prev_step = ""
            continue

        if inside_scenario:
            step_match = re.match(r'^(Given|When|Then|And|But)\s+(.*)', line)
            if step_match:
                keyword, step_text = step_match.groups()
                if not first_step_seen and keyword in ["And", "But"]:
                    issues.append(f"Line {line_num}: Scenario starts with '{keyword}'. Use 'Given' or 'When'.")
                first_step_seen = True

                if line == prev_step:
                    issues.append(f"Line {line_num}: Duplicate consecutive step -> '{line}'")
                prev_step = line

            if "/html/body" in line or "//div[" in line:
                issues.append(f"Line {line_num}: Brittle XPath detected.")

    return issues

def main():
    total_issues = []
    for root, _, files in os.walk("features"):
        for file in files:
            if file.endswith(".feature"):
                issues = analyze_feature_file(os.path.join(root, file))
                if issues:
                    total_issues.extend(issues)

    if total_issues:
        print("\n❌ PR Review Agent Failed:\n" + "\n".join(total_issues))
        sys.exit(1)
    else:
        print("\n✅ PR Review Passed!\n")
        sys.exit(0)

if __name__ == "__main__":
    main()