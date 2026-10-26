from json import JSONDecodeError

import kocka_class
import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os
import json
import sqlite3
from datetime import datetime

class KockaApp:
    def __init__(self, root):
        self.root = root

class KockaApp(kocka_class.Kockadobas):
    def __init__(self, root):
        super().__init__(root)
        self.mentes_gomb = ttk.Button(root, text='Mentés - TEXT', command=self.mentes)
        self.mentes_gomb.grid(column=0, row=3)
        self.mentes_csv_gomb = ttk.Button(root, text = 'Mentés - CSV' ,command=self.mentes_csv)
        self.mentes_csv_gomb.grid(column=1, row=3)
        self.mentes_json_gomb = ttk.Button(root, text='Mentés - JSON,,', command=self.mentes_json)
        self.mentes_json_gomb.grid(column=2, row=3)
        self.mentes_sql_gomb = ttk.Button(root, text='Mentés - SQL,,', command=self.mentes_sql)
        self.mentes_sql_gomb.grid(column=3, row=3)

    def mentes_sql(self):
        if sum(self.eredmenyek.values()) == 0:
            messagebox.showwarning(title='Dobas', message='Eloszor dobjon')
            return

        datum = datetime.now().strftime('%Y.%m.%d')

        try:
            with sqlite3.connect('mentes.db') as conn:
                cursor = conn.cursor()
                cursor.execute("""
                        CREATE TABLE IF NOT EXISTS dobasok (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            datum TEXT,
                            egy INTEGER,
                            ketto INTEGER,
                            harom INTEGER,
                            negy INTEGER,
                            ot INTEGER,
                            hat INTEGER
                        )    
                    """)
                print(self.eredmenyek.keys())

                cursor.execute("""
                        INSERT INTO dobasok
                        (datum, egy, ketto, harom, negy, ot, hat) VALUES (?, ?, ?,?,?,?,?)
                    """, (datum, *self.eredmenyek.values()))
                conn.commit()

            messagebox.showinfo(title='Mentes', message='Sikeres volt a Mentes')

        except (sqlite3.Error):
            messagebox.showerror(title='Hiba', message='Nem sikerült a Mentes')

    def mentes_json(self):
        if sum(self.eredmenyek.values()) == 0:
            messagebox.showwarning(title='Dobas', message='Eloszor dobjon')
            return
        fajlnev = 'mentes.json'
        adatok = self.eredmenyek.copy()
        adatok['Dátum'] = datetime.now().strftime('%Y.%m.%d')
        try:
            try:
                with open(fajlnev, mode='r', newline='', encoding='utf-8') as f:
                    mentett_adatok = json.load(f)
            except FileNotFoundError:
                mentett_adatok = []

            mentett_adatok.append(adatok)

            with open(fajlnev, mode='w', newline='', encoding='utf-8') as f:
                json.dump(mentett_adatok, f, ensure_ascii=False, indent=4)

                messagebox.showinfo(title='Mentes', message='Sikeres volt a Mentes')

        except (OSError, JSONDecodeError):
            messagebox.showinfo(title='Mentes', message='Nem sikerült a Mentes')

    def mentes_csv(self):
        if sum(self.eredmenyek.values()) == 0:
            messagebox.showwarning(title='Dobas', message='Eloszor dobjon')
            return
        fajlnev = 'mentes.csv'
        adatok = self.eredmenyek.copy()
        adatok['Dátum'] = datetime.now().strftime('%Y.%m.%d')
        fejlec_kell= not os.path.exists(fajlnev) or os.path.getmtime(fajlnev) == 0
        try:
            with open(fajlnev, mode='a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                if fejlec_kell:
                    writer.writerow(adatok.keys())
                writer.writerow(adatok.values())
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
