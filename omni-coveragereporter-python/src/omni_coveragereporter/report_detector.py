def total_lines(file_name):
    f = open(file_name)
    data = f.readlines()
    f.close()
    return len(data)


def is_coverage_py(report_text):
    if report_text.startswith("{") and report_text.endswith(
            "}") and "\"meta\":" in report_text and "\"files\":" in report_text:
        return True
    return False


def is_coverage_go(report_text):
    if report_text.startswith("mode:") and "go:" in report_text:
        return True
    return False


def is_clover(report_text):
    if "coverage generated" in report_text and "project timestamp" in report_text:
        return True
    return False
