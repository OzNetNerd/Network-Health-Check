import sys
import os
from concurrent.futures import ThreadPoolExecutor
from subprocess import check_output, CalledProcessError
import logging
import time
from pathlib import Path


LOG_LEVEL = logging.DEBUG

CURRENT_DIR = os.getcwd()
OUTPUT_DIR = f'{CURRENT_DIR}/outputs'
LOG_OUTPUT_PATH = f'{OUTPUT_DIR}/logs.txt'
START_TIME = time.time()
MAX_THREADS = 5
INPUT_FILENAME = sys.argv[1] if len(sys.argv) > 1 else 'ips.txt'
PING_COMMAND = 'ping -q -c 3 -W 1 -4'
TRACEROUTE_COMMAND = 'traceroute'

formatter = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(filename=LOG_OUTPUT_PATH, format=formatter, level=LOG_LEVEL)


def title(section_name):
    section_title = '\n' + '*' * 100 + f'\n{section_name}\n' + '*' * 100 + '\n'

    return section_title


def health_checks(ip):
    ping_cmd = f'{PING_COMMAND} {ip}'
    trace_cmd = f'{TRACEROUTE_COMMAND} {ip}'

    ping_status = run_command(ping_cmd)
    trace_status = run_command(trace_cmd)

    filename = f'{OUTPUT_DIR}{os.sep}{ip}.txt'
    with open(filename, 'w') as f:
        f.write(title('Ping Results'))
        f.write(ping_status)

        f.write(title('Trace Results'))
        f.write(trace_status)

    logging.info(f'Wrote outputs to: {filename}')
    logging.debug(ping_status)
    logging.debug(trace_status)


def run_command(command):
    logging.info(f'running: {command}')

    split_cmd = command.split()

    try:
        output = check_output(split_cmd).decode('utf-8')

    except CalledProcessError:
        return 'FAILED'

    return output


def main():
    print('Running health checks...')
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

    with open(INPUT_FILENAME, 'r') as f:
        ips = f.read().splitlines()

    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        [executor.submit(health_checks, ip) for ip in ips]

    end_time = time.time() - START_TIME
    num_ips = len(ips)
    logging.info(f'Checked {num_ips} hosts in {round(end_time)} seconds.')


if __name__ == '__main__':
    main()
