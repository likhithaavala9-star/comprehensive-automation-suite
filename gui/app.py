import tkinter as tk
from tkinter import ttk, messagebox
from automation_suite.modules.file_organizer import FileOrganizer
from tkinter import filedialog

class FileOrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Automation Suite – File Organizer")
        self.root.geometry("400x250")

        self.organizer = None
        self.is_running = False

        title = ttk.Label(
            root,
            text="File Organizer",
            font=("Segoe UI", 16, "bold")
        )
        title.pack(pady=10)

        self.status_label = ttk.Label(
            root,
            text="Status: Stopped",
            foreground="red"
        )
        self.status_label.pack(pady=5)

        btn_frame = ttk.Frame(root)
        btn_frame.pack(pady=20)

        self.select_btn = ttk.Button(
             root,
             text="Select Watch Folder",
             command=self.select_watch_folder
        )
        self.select_btn.pack(pady=5)


        self.start_btn = ttk.Button(
            btn_frame,
            text="Start",
            command=self.start_monitoring
        )
        self.start_btn.grid(row=0, column=0, padx=10)

        self.stop_btn = ttk.Button(
            btn_frame,
            text="Stop",
            command=self.stop_monitoring
        )
        self.stop_btn.grid(row=0, column=1, padx=10)

    def start_monitoring(self):
        if self.is_running:
            messagebox.showinfo("Info", "Already running!")
            return

        try:
            self.organizer = FileOrganizer()
            self.organizer.start()
            self.is_running = True

            self.status_label.config(text="Status: Running", foreground="green")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def stop_monitoring(self):
        if not self.is_running:
            messagebox.showinfo("Info", "Already stopped!")
            return

        if self.organizer:
            self.organizer.stop()

        self.is_running = False
        self.status_label.config(text="Status: Stopped", foreground="red")

    def select_watch_folder(self):
        folder = filedialog.askdirectory()
        print("Selected folder:", folder)


if __name__ == "__main__":
    root = tk.Tk()
    app = FileOrganizerApp(root)
    root.mainloop()
