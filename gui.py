from tkinter import *
from tkinter import ttk, messagebox
from controller import Controller


class CafeGUI:

    def __init__(self, root):

        self.controller = Controller()

        self.root = root
        self.root.title("Cafe Management System")
        self.root.geometry("1000x600")
        self.root.configure(bg="#ecf0f1")

        # TITLE
        title = Label(
            self.root,
            text="Cafe Management System",
            font=("Arial", 24, "bold"),
            bg="#6f4e37",
            fg="white",
            pady=15
        )

        title.pack(fill=X)

        # MAIN FRAME
        main_frame = Frame(
            self.root,
            bg="#ecf0f1"
        )

        main_frame.pack(
            fill=BOTH,
            expand=True,
            padx=20,
            pady=20
        )

        # LEFT FRAME
        left_frame = Frame(
            main_frame,
            bg="white",
            bd=2,
            relief=RIDGE
        )

        left_frame.place(
            x=0,
            y=0,
            width=350,
            height=500
        )

        # RIGHT FRAME
        right_frame = Frame(
            main_frame,
            bg="white",
            bd=2,
            relief=RIDGE
        )

        right_frame.place(
            x=370,
            y=0,
            width=580,
            height=500
        )

        # FORM TITLE
        Label(
            left_frame,
            text="Menu Details",
            font=("Arial", 18, "bold"),
            bg="white",
            fg="#6f4e37"
        ).pack(pady=20)

        # ITEM NAME
        Label(
            left_frame,
            text="Item Name",
            font=("Arial", 12, "bold"),
            bg="white"
        ).pack(anchor=W, padx=20)

        self.name_entry = Entry(
            left_frame,
            font=("Arial", 12),
            bd=2
        )

        self.name_entry.pack(
            fill=X,
            padx=20,
            pady=10
        )

        # QUANTITY
        Label(
            left_frame,
            text="Quantity",
            font=("Arial", 12, "bold"),
            bg="white"
        ).pack(anchor=W, padx=20)

        self.quantity_entry = Entry(
            left_frame,
            font=("Arial", 12),
            bd=2
        )

        self.quantity_entry.pack(
            fill=X,
            padx=20,
            pady=10
        )

        # PRICE
        Label(
            left_frame,
            text="Price",
            font=("Arial", 12, "bold"),
            bg="white"
        ).pack(anchor=W, padx=20)

        self.price_entry = Entry(
            left_frame,
            font=("Arial", 12),
            bd=2
        )

        self.price_entry.pack(
            fill=X,
            padx=20,
            pady=10
        )

        # BUTTONS
        btn_frame = Frame(
            left_frame,
            bg="white"
        )

        btn_frame.pack(pady=20)

        Button(
            btn_frame,
            text="Add Item",
            font=("Arial", 11, "bold"),
            bg="#27ae60",
            fg="white",
            width=14,
            cursor="hand2",
            command=self.add_item
        ).grid(row=0, column=0, padx=10)

        Button(
            btn_frame,
            text="Delete Item",
            font=("Arial", 11, "bold"),
            bg="#c0392b",
            fg="white",
            width=14,
            cursor="hand2",
            command=self.delete_item
        ).grid(row=0, column=1, padx=10)

        Button(
            left_frame,
            text="Refresh Data",
            font=("Arial", 11, "bold"),
            bg="#2980b9",
            fg="white",
            width=30,
            cursor="hand2",
            command=self.load_items
        ).pack(pady=10)

        # TABLE
        table_frame = Frame(
            right_frame,
            bg="white"
        )

        table_frame.pack(fill=BOTH, expand=True)

        scroll_y = Scrollbar(
            table_frame,
            orient=VERTICAL
        )

        self.cafe_table = ttk.Treeview(
            table_frame,
            columns=(
                "ID",
                "Item",
                "Quantity",
                "Price"
            ),
            yscrollcommand=scroll_y.set
        )

        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_y.config(
            command=self.cafe_table.yview
        )

        self.cafe_table.heading("ID", text="ID")
        self.cafe_table.heading("Item", text="Item Name")
        self.cafe_table.heading("Quantity", text="Quantity")
        self.cafe_table.heading("Price", text="Price")

        self.cafe_table["show"] = "headings"

        self.cafe_table.column("ID", width=50)
        self.cafe_table.column("Item", width=180)
        self.cafe_table.column("Quantity", width=100)
        self.cafe_table.column("Price", width=100)

        self.cafe_table.pack(
            fill=BOTH,
            expand=True
        )

        self.load_items()

    def add_item(self):

        try:

            item_name = self.name_entry.get()

            quantity = int(
                self.quantity_entry.get()
            )

            price = float(
                self.price_entry.get()
            )

            self.controller.add_item(
                item_name,
                quantity,
                price
            )

            messagebox.showinfo(
                "Success",
                "Item Added Successfully"
            )

            self.load_items()

            self.clear_fields()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def load_items(self):

        for row in self.cafe_table.get_children():
            self.cafe_table.delete(row)

        items = self.controller.get_items()

        for item in items:

            self.cafe_table.insert(
                "",
                END,
                values=item
            )

    def delete_item(self):

        try:

            selected = self.cafe_table.focus()

            data = self.cafe_table.item(selected)

            item_id = data["values"][0]

            self.controller.remove_item(
                item_id
            )

            messagebox.showinfo(
                "Deleted",
                "Item Deleted Successfully"
            )

            self.load_items()

        except:

            messagebox.showerror(
                "Error",
                "Select item first"
            )

    def clear_fields(self):

        self.name_entry.delete(0, END)
        self.quantity_entry.delete(0, END)
        self.price_entry.delete(0, END)