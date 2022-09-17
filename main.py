
import tkinter as tk

def search():
    print('searching')

def main():
    root = tk.Tk()
    msg = tk.Label(root, text='Which stock are you looking for today?')
    msg.grid(column=0, row=0, padx=20,pady=20, sticky=(tk.E, tk.W, tk.N, tk.S))
    searchButton = tk.Button(root, text='Search', command=search)
    searchButton.grid(column=0, row=1, padx=20, pady=20)
    root.mainloop()

if __name__ == '__main__':
    main()