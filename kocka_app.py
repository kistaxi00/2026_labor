import kocka_class
import tkinter as tk
from tkinter import ttk, messagebox
import csv

class KockaApp(kocka_class.Kockadobas):
    def __init__(self, root):
        super().__init__(root)
        self.mentes_gomb = ttk.Button(root, text='Mentés - TEXT', command=self.mentes)
        self.mentes_gomb.grid(column=0, row=3)
        self.mentes_csv_gomb = ttk.Button(root, text = 'Mentés - CSV' ,command=self.mentes_csv)
        self.mentes_csv_gomb.grid(column=1, row=3)
        self.mentes_sql_gomb = ttk.Button(root, text='Mentés - SQL,,', command=self.mentes_sql)
        self.mentes_sql_gomb.grid(column=2, row=3)

    def mentes_sql(self):
        pass

    def mentes_csv(self):
        if sum(self.eredmenyek.values()) == 0:
            messagebox.showwarning(title='Dobas', message='Eloszor dobjon')
            return
        fajlnev = 'mentes.csv'
        print(self.eredmenyek)
        try:
            with open(fajlnev, mode='a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(self.eredmenyek.values())
            messagebox.showinfo(title='Mentes', message='Sikeres volt a Mentes')
        except OSError:
            messagebox.showerror(title='Hiba', message='Nem sikerült a Mentes')

    def mentes(self):
        if sum(self.eredmenyek.values()) == 0:
            messagebox.showwarning(title= 'Dobas', message= 'Eloszor dobjon')
            return
        sor = f'{self.eredmenyek}\n'
        try:
            with open('mentes.txt','a', encoding='utf-8') as f:
                f.write(sor)
            messagebox.showinfo('Mentes', 'Sikeres volt a Mentes')
        except OSError:
            messagebox.showerror('Hiba', 'Nem sikerült a Mentes')

if __name__ == "__main__":
    root = tk.Tk()
    app = KockaApp(root)
    root.mainloop()
