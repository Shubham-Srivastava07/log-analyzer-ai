from parser import parse_log
from analyzer import analyze_log

raw_data = parse_log('nginx', 'sample_logs/nginx_error.log')
analyzed_data = [analyze_log(entry) for entry in raw_data]

print(analyzed_data)

