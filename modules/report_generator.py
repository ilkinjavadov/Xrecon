# modules/report_generator.py

def generate_markdown_report(findings, output_path):
    with open(output_path, 'w') as f:
        f.write("# XRecon GitHub Scan Report\n\n")

        if not findings:
            f.write("✅ No sensitive files found.\n")
            return

        f.write(f"**{len(findings)} potentially sensitive file(s) found.**\n\n")

        for item in findings:
            f.write(f"- 🔍 **Repository**: `{item['repository']}`\n")
            f.write(f"  - 📄 File: `{item['file']}`\n")
            f.write(f"  - 🔗 [View File]({item['url']})\n\n")
