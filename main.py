
import customtkinter as ctk
from tkinter import filedialog
import threading
from beat_analyzer import get_bpm

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Beats Meter")
        self.geometry("400x200")

        self.grid_columnconfigure(0, weight=1)

        self.select_button = ctk.CTkButton(self, text="Select Song", command=self.select_song)
        self.select_button.grid(row=0, column=0, padx=20, pady=20)

        self.file_label = ctk.CTkLabel(self, text="No song selected")
        self.file_label.grid(row=1, column=0, padx=20, pady=10)

        self.bpm_label = ctk.CTkLabel(self, text="BPM: --")
        self.bpm_label.grid(row=2, column=0, padx=20, pady=10)

    def select_song(self):
        file_path = filedialog.askopenfilename(
            title="Select a song file",
            filetypes=[
                ("Audio Files", "*.mp3 *.wav *.flac *.m4a"),
                ("All files", "*.*"),
            ]
        )
        if file_path:
            # Update UI to show processing has started
            self.file_label.configure(text=file_path.split("/")[-1])
            self.bpm_label.configure(text="BPM: Analyzing...")
            self.select_button.configure(state="disabled")

            # Run the analysis in a separate thread to keep the GUI responsive
            analysis_thread = threading.Thread(
                target=self.run_bpm_analysis,
                args=(file_path,),
                daemon=True
            )
            analysis_thread.start()

    def run_bpm_analysis(self, file_path):
        """Runs the BPM analysis and schedules the UI update."""
        bpm = get_bpm(file_path)
        # Schedule the UI update to run on the main thread
        self.after(0, self.update_ui_with_results, bpm)

    def update_ui_with_results(self, bpm):
        """Updates the GUI with the BPM result from the main thread."""
        if bpm:
            self.bpm_label.configure(text=f"BPM: {bpm}")
        else:
            self.bpm_label.configure(text="BPM: Error")
        self.select_button.configure(state="normal") # Re-enable the button

if __name__ == "__main__":
    app = App()
    app.mainloop()
