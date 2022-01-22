def convert_coverage(data):
    codecov_report = {"coverage": data['files']}
    for file in data['files']:
        file_object = data['files'][file]
        executed_lines = max(file_object['executed_lines']) if file_object['executed_lines'] else 0
        missing_lines = max(file_object['missing_lines']) if file_object['missing_lines'] else 0
        total_lines = max(executed_lines, missing_lines)
        print(total_lines)
        print(file_object)
    return codecov_report
