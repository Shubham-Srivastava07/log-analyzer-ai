from parser import parse_log

all_results = []
all_results.extend(parse_log('nginx', 'sample_logs/nginx_error.log'))
all_results.extend(parse_log('jenkins', 'sample_logs/jenkins_failure.log'))
print(all_results)
