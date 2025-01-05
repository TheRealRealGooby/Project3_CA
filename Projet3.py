import tkinter as tk

tab = tk.Tk()
tab.title("WIKIBOOKS")
tab.geometry("350x200")

label=tk.Label(tab, text="Searching for a book?")
label.pack(pady=5)

tbox=tk.Entry(tab, width=37)
tbox.pack(pady=5)

BOOKS=["To Kill a Mockingbird", "1984", "The Great Gatsby", "The Catcher in the Rye", "Moby-Dick", "Pride and Prejudice", "War and Peace", "The Lord of the Rings", "The Hobbit", "Harry Potter and the Sorcerer's Stone", "Crime and Punishment", "The Brothers Karamazov", "Brave New World", "The Kite Runner", "The Alchemist", "One Hundred Years of Solitude", "The Picture of Dorian Gray", "The Count of Monte Cristo", "Les Misérables", "A Tale of Two Cities"]


'''
lframe = tk.Frame(tab)
lframe.pack(pady=5)

# Function to display lines of text
def add_line():
    user_input = tbox.get()
    if user_input:  # Add a new label for each input
        new_line = tk.Label(lframe, text=user_input)
        new_line.pack(anchor="w")  # Align labels to the left

# Button to simulate adding a new line
button = tk.Button(tab, text="Add Line", command=add_line)
button.pack(pady=5)
'''

tab.mainloop()