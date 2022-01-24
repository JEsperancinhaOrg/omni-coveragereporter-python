import coveragepy_parser


def convert_coverage(data, report=None):
    if report:
        codecov_files = report['coverage']
        codecov_report = report
    else:
        codecov_files = {}
        codecov_report = {"coverage": codecov_files}
    for file in data['files']:
        file_object = data['files'][file]
        total_lines = coveragepy_parser.total_lines(file_object)
        codecov_file = codecov_files[file] if file in codecov_files else None
        if codecov_file is None:
            codecov_file = {}
            codecov_files[file] = codecov_file
        for i in range(1, total_lines):
            if str(i) in codecov_file:
                curr = 0 if codecov_file[str(i)] is None else codecov_file[str(i)]
                offset = 1 if i in file_object['executed_lines'] else 0
                codecov_file[str(i)] = curr + offset
            else:
                codecov_file[str(i)] = 1 if i in file_object['executed_lines'] else None
            if codecov_file[str(i)] is None:
                codecov_file[str(i)] = 0 if i in file_object['missing_lines'] else None
    return codecov_report