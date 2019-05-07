from subprocess import Popen, PIPE, STDOUT
import os


def call_script(file_script_name):
    script_dir = os.path.expanduser('~')  # <-- absolute dir the script is in
    rel_path = file_script_name
    abs_file_path = os.path.join(script_dir, rel_path)
    command = ["bash", abs_file_path]

    try:
        process = Popen(command, stdout=PIPE, stderr=STDOUT)
        output = process.stdout.read()
        status = process.poll()

        if status == 0:
                result = {"status": "Success", "output": output}
        else:
                result = {"status": "Failed", "output": output}

    except Exception as e:
        result = {"status": "Failed", "output": bytearray(str(e), 'utf-8')}

    return result


call_back = call_script("sample.sh")
if call_back.get("status") is not 'Failed':
    for line in call_back.get('output').decode('ascii').strip().split(','):
        print(line)

call_back = call_script("sample_error.sh")
if call_back.get("status") is 'Failed':
    print(call_back.get('output').decode('ascii').strip().split(','))

call_back = call_script('not_found.sh')
if call_back.get("status") is 'Failed':
    print(call_back.get('output').decode('ascii').strip().split(','))