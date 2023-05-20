import requests
from bs4 import BeautifulSoup
import re
import tkinter as tk
from tkinter import messagebox

def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)
    names = re.findall(r'[A-Z][a-z]+', text)
    surnames = re.findall(r'[A-Z][a-z]+', text)
    phone_numbers = re.findall(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', text)
    return emails, names, surnames, phone_numbers

def scrape_data_gui():
    def scrape():
        website = entry.get()
        scraped_emails, scraped_names, scraped_surnames, scraped_phone_numbers = scrape_data(website)
        result = "Emails:\n" + "\n".join(scraped_emails) + "\n\n" + \
                 "Names:\n" + "\n".join(scraped_names) + "\n\n" + \
                 "Surnames:\n" + "\n".join(scraped_surnames) + "\n\n" + \
                 "Phone Numbers:\n" + "\n".join(scraped_phone_numbers)
        messagebox.showinfo("Results", result)

    # Tworzenie okna
    window = tk.Tk()
    window.title("Web Data Scraper")
    window.geometry("400x200")

    # Etykieta i pole tekstowe do wprowadzania adresu URL
    label = tk.Label(window, text="Enter the website URL:")
    label.pack()
    entry = tk.Entry(window)
    entry.pack()

    # Przycisk do rozpoczęcia przeszukiwania
    button = tk.Button(window, text="Scrape", command=scrape)
    button.pack()

    # Uruchomienie pętli głównej GUI
    window.mainloop()

# Uruchomienie programu
scrape_data_gui()
