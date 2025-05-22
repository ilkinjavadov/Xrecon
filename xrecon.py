# xrecon.py

import argparse
from modules import github_scanner, report_generator


def main():
    parser = argparse.ArgumentParser(description="XRecon - GitHub Recon Tool")
    parser.add_argument("--target", required=True, help="GitHub organization or username")
    parser.add_argument("--token", required=True, help="GitHub Personal Access Token")
    parser.add_argument("--output", default="output/results.md", help="Path to save the report")
    args = parser.parse_args()

    print("[+] Starting GitHub scan for target:", args.target)
    results = github_scanner.scan_github(args.target, args.token)

    print("[+] Generating report...")
    report_generator.generate_markdown_report(results, args.output)
    print(f"[+] Scan complete. Report saved to {args.output}")


if __name__ == "__main__":
    main()
