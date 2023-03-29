import sys
import frida

def read_file_all(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

def on_message(message, data):
    if message['type'] == 'error':
        print("[!] " + message['stack'])
    elif message['type'] == 'send':
        print(message['payload'])
        if data is not None:
            print("[data] " + format_bytes(data))
    else:
        print(message)

def format_bytes(byte_array):
    string = '['
    for b in byte_array:
        string = string + str(b) + ','
    return string[:len(string) - 1] + "]"

if __name__ == '__main__':
    device = frida.get_usb_device()
    process = device.attach("apptobehook")
    js_code = read_file_all("hook.js")
    script = process.create_script(js_code)
    script.on('message', on_message)
    script.load()
    sys.stdin.read()
