from parser import parse_log
from analyzer1 import generate_summary

logs = parse_log('nginx', 'sample_logs/nginx_error.log')

generate_summary(logs)
