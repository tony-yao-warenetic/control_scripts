import tkinter as tk
import requests
import os

server_url = "https://no-more-waiting-4-lunch-atest20061206.replit.app/"

test_url = "https://80755081-e125-4a75-b806-06998c36e03c-00-s7c32woc0kef.worf.replit.dev/"


window = tk.Tk()
window.title("Lane Control")

# label_left_status = tk.Label(window, text="Program Status: Off", font=("Arial", 12), fg="red")
# label_left_status.pack(pady=5)


def start_program():
	url = server_url + "/start_program/YaoyutongaiWangjiayuan"
	try:
		response = requests.post(url)
		response.raise_for_status()
	except Exception as e:
		print(f"Error while starting program: {e}")

def stop_program():
	url = server_url + "/stop_program/YaoyutongaiWangjiayuan"
	try:
		response = requests.post(url)
		response.raise_for_status()
	except Exception as e:
		print(f"Error while stopping program: {e}")


def quit_program():
	stop_program()
	os._exit(0)


start_button = tk.Button(window, text="Start Program", width=20, height=2, command=start_program)
start_button.pack(pady=10)

stop_button = tk.Button(window, text="Stop Program", width=20, height=2, command=stop_program)
stop_button.pack(pady=10)

quit_button = tk.Button(window, text="Quit Program", width=20, height=2, command=quit_program)
quit_button.pack(pady=10)


window.mainloop()