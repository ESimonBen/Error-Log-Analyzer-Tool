from log_parser import analyze_logs

def run(input_data):
    log_text = input_data.get("log_text", "")

    result = analyze_logs(log_text)

    return result