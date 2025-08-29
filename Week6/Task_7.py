#Task_7:
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os
#--------------------------
#Auto-generate a sample CSV file:
#--------------------------
def create_sample_csv():
    if not os.path.exists("sample_data.csv"):
        data = {
            "Name": ["Rohma", "Sumaya", "Umair", "Ali", "Hina"],
            "Age": [21, 22, 20, 23, 21],
            "Marks": [85, 90, 78, 88, 95]}
        df = pd.DataFrame(data)
        df.to_csv("sample_data.csv", index=False)
        print("Sample CSV file 'sample_data.csv' created automatically!")
create_sample_csv()
#--------------------------
#Main Application Class:
#--------------------------
class DataAnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📊 Data Analysis Application")
        self.root.geometry("900x600")
        self.df = None
        #Title
        title = tk.Label(root, text="Data Analysis Application", font=("Arial", 18, "bold"), bg="navy", fg="white")
        title.pack(fill="x")
        #Buttons Frame
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="📂 Upload CSV", command=self.load_csv, width=15, bg="lightblue").grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="📑 Show Data", command=self.show_data, width=15, bg="lightgreen").grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="📊 Show Stats", command=self.show_stats, width=15, bg="khaki").grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="📈 Plot Graph", command=self.plot_graph, width=15, bg="salmon").grid(row=0, column=3, padx=5)
        tk.Button(btn_frame, text="💾 Export CSV", command=self.export_csv, width=15, bg="lightpink").grid(row=0, column=4, padx=5)
        #Output area
        self.text_area = tk.Text(root, height=15, wrap="word", font=("Courier", 10))
        self.text_area.pack(fill="both", expand=True, padx=10, pady=10)
    #--------------------------
    #Functions:
    #--------------------------
    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.df = pd.read_csv(file_path)
            messagebox.showinfo("Success", f"CSV file loaded successfully!\n{file_path}")
    def show_data(self):
        if self.df is not None:
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, str(self.df.head(10)))  # Show first 10 rows
        else:
            messagebox.showwarning("Warning", "Please upload a CSV file first!")
    def show_stats(self):
        if self.df is not None:
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, str(self.df.describe()))
        else:
            messagebox.showwarning("Warning", "Please upload a CSV file first!")
    def plot_graph(self):
        if self.df is not None:
            if "Age" in self.df.columns and "Marks" in self.df.columns:
                fig, ax = plt.subplots(figsize=(5,4))
                self.df.plot(kind="bar", x="Name", y="Marks", ax=ax, color="skyblue", legend=False)
                ax.set_title("Student Marks", fontsize=14)
                #plot:
                chart_window = tk.Toplevel(self.root)
                chart_window.title("📈 Data Visualization")
                canvas = FigureCanvasTkAgg(fig, master=chart_window)
                canvas.draw()
                canvas.get_tk_widget().pack(fill="both", expand=True)
            else:
                messagebox.showerror("Error", "Dataset must contain 'Name', 'Age', and 'Marks' columns!")
        else:
            messagebox.showwarning("Warning", "Please upload a CSV file first!")
    def export_csv(self):
        if self.df is not None:
            save_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                                     filetypes=[("CSV files", "*.csv")])
            if save_path:
                self.df.to_csv(save_path, index=False)
                messagebox.showinfo("Success", f"CSV exported successfully!\n{save_path}")
        else:
            messagebox.showwarning("Warning", "No data available to export!")
#--------------------------
#Run Application:
#--------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = DataAnalysisApp(root)
    root.mainloop()