import tkinter as tk
from tkinter import *

def remove_match_character(list1, list2):
    for i in list1[:]:  # Loop over a copy to avoid modification issues
        if i in list2:
            list1.remove(i)
            list2.remove(i)
            return [list1 + ["*"] + list2, True]
    return [list1 + ["*"] + list2, False]

def tell_st():
    p1 = player1.get()
    p1 = p1.lower().replace(" ", "")
    p1_list = list(p1)

    p2 = player2.get()
    p2 = p2.lower().replace(" ", "")
    p2_list = list(p2)

    pro = True
    while pro:
        ret_list = remove_match_character(p1_list, p2_list)
        con_list = ret_list[0]
        pro = ret_list[1]
        star_index = con_list.index("*")
        p1_list = con_list[:star_index]
        p2_list = con_list[star_index + 1:]

    count = len(p1_list) + len(p2_list)

    result = ["Friends", "Love", "Affection", "Marraige", "Enemy", "Siblings"]

    while len(result) > 1:
        split_index = (count % len(result)) - 1

        if split_index >= 0:
            right = result[split_index + 1:]
            left = result[:split_index]
            result = right + left
        else:
            result = result[:len(result) - 1]

    st.insert(10, result[0])

def clear_fun():
    player1.delete(0, END)
    player2.delete(0, END)
    st.delete(0, END)
    player1.focus_set()

if __name__ == '__main__':
    window = Tk()
    window.configure(background="light green")
    window.geometry("500x350")
    window.title("Flames game")

    label1 = Label(window, text="Name of Player 1 :", fg="black", bg="beige", font=("Arial", 20, "bold"))
    label2 = Label(window, text="Name of Player 2 :", fg="black", bg="beige", font=("Arial", 20, "bold"))
    label3 = Label(window, text="Status :", fg="black", bg="light blue", font=("Arial", 20, "bold"))

    label1.grid(row=1, column=0)
    label2.grid(row=2, column=0)
    label3.grid(row=4, column=0)

    player1 = Entry(window)
    player2 = Entry(window)
    st = Entry(window)

    player1.grid(row=1, column=1, ipadx="50")
    player2.grid(row=2, column=1, ipadx="50")
    st.grid(row=4, column=1, ipadx="50")

    button1 = Button(window, text="Submit", bg="red", fg="black", font=("Arial", 20, "bold"), command=tell_st)
    button2 = Button(window, text="Clear", bg="red", fg="black", font=("Arial", 20, "bold"), command=clear_fun)

    button1.grid(row=3, column=1)
    button2.grid(row=5, column=1)

    window.mainloop()
