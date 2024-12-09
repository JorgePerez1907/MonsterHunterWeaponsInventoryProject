import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import MonsterHunterWeapons
from collections import defaultdict, deque
from PIL import Image, ImageTk
from datetime import datetime
import os

class MonsterHunterGUI:
    def __init__(self, master):
        self.master = master
        master.title("Monster Hunter Crafting Table")
        master.geometry("1000x700")

        self.material_inventory = defaultdict(int)

        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.weapons_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.weapons_frame, text="Weapons")

        self.inventory_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.inventory_frame, text="Material Inventory")

        self.craftable_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.craftable_frame, text="Craftable Weapons")

        self.setup_weapons_tab(self.weapons_frame)

        self.setup_inventory_tab(self.inventory_frame)

        self.setup_craftable_tab(self.craftable_frame)

        self.crafting_queue = MonsterHunterWeapons.CraftingQueue()

        self.crafting_history = MonsterHunterWeapons.CraftingHistory()

    def setup_weapons_tab(self, parent):
        search_frame = ttk.Frame(parent)
        search_frame.pack(fill=tk.X, pady=(0, 10))

        search_label = ttk.Label(search_frame, text="Search Weapon:")
        search_label.pack(side=tk.LEFT, padx=(0, 5))

        self.search_entry = ttk.Entry(search_frame, width=40)
        self.search_entry.pack(side=tk.LEFT, padx=(0, 10))
        self.search_entry.bind('<KeyRelease>', self.filter_weapons)

        tree_frame = ttk.Frame(parent)
        tree_frame.pack(fill=tk.BOTH, expand=True)

        tree_scroll = ttk.Scrollbar(tree_frame)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.weapon_tree = ttk.Treeview(
            tree_frame,
            columns=('Weapon', 'Materials'),
            show='headings',
            yscrollcommand=tree_scroll.set
        )
        self.weapon_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        tree_scroll.config(command=self.weapon_tree.yview)

        self.weapon_tree.heading('Weapon', text='Weapon Name')
        self.weapon_tree.heading('Materials', text='Crafting Materials')

        self.weapon_tree.column('Weapon', width=300)
        self.weapon_tree.column('Materials', width=500)

        details_frame = ttk.Frame(parent)
        details_frame.pack(fill=tk.X, pady=(10, 0))

        details_label = ttk.Label(details_frame, text="Weapon Details:")
        details_label.pack(side=tk.TOP, anchor='w')

        self.details_text = tk.Text(details_frame, height=5, width=100, wrap=tk.WORD)
        self.details_text.pack(fill=tk.X)
        self.details_text.config(state=tk.DISABLED)

        self.populate_weapons()

        self.weapon_tree.bind('<<TreeviewSelect>>', self.show_weapon_details)

        add_to_queue_button = ttk.Button(parent, text="Add to Queue", command=self.add_to_queue)
        add_to_queue_button.pack(pady=10)

        remove_from_queue_button = ttk.Button(parent, text="Remove from Queue", command=self.remove_from_queue)
        remove_from_queue_button.pack(pady=10)

        craft_queue_button = ttk.Button(parent, text="Craft Queue", command=self.craft_queue)
        craft_queue_button.pack(pady=10)

    def setup_inventory_tab(self, parent):
        title_label = ttk.Label(parent, text="Material Inventory", font=('Helvetica', 16, 'bold'))
        title_label.pack(pady=(10, 20))

        button_frame = ttk.Frame(parent)
        button_frame.pack(fill=tk.X, padx=10, pady=(0, 10))

        add_button = ttk.Button(button_frame, text="Add Material", command=self.add_material)
        add_button.pack(side=tk.LEFT, padx=5)

        remove_button = ttk.Button(button_frame, text="Remove Material", command=self.remove_material)
        remove_button.pack(side=tk.LEFT, padx=5)

        tree_frame = ttk.Frame(parent)
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=10)

        tree_scroll = ttk.Scrollbar(tree_frame)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.inventory_tree = ttk.Treeview(
            tree_frame,
            columns=('Material', 'Quantity'),
            show='headings',
            yscrollcommand=tree_scroll.set
        )
        self.inventory_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        tree_scroll.config(command=self.inventory_tree.yview)

        self.inventory_tree.heading('Material', text='Material Name')
        self.inventory_tree.heading('Quantity', text='Quantity')

        self.inventory_tree.column('Material', width=600)
        self.inventory_tree.column('Quantity', width=100)

    def setup_craftable_tab(self, parent):
        title_label = ttk.Label(parent, text="Craftable Weapons", font=('Helvetica', 16, 'bold'))
        title_label.pack(pady=(10, 20))

        search_frame = ttk.Frame(parent)
        search_frame.pack(fill=tk.X, padx=10, pady=(0, 10))

        search_label = ttk.Label(search_frame, text="Filter by Material:")
        search_label.pack(side=tk.LEFT, padx=(0, 5))

        self.material_search_entry = ttk.Entry(search_frame, width=40)
        self.material_search_entry.pack(side=tk.LEFT, padx=(0, 10))
        self.material_search_entry.bind('<KeyRelease>', self.filter_craftable_weapons)

        tree_frame = ttk.Frame(parent)
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=10)

        tree_scroll = ttk.Scrollbar(tree_frame)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.craftable_tree = ttk.Treeview(
            tree_frame,
            columns=('Weapon', 'Materials', 'Possible'),
            show='headings',
            yscrollcommand=tree_scroll.set
        )
        self.craftable_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        tree_scroll.config(command=self.craftable_tree.yview)

        self.craftable_tree.heading('Weapon', text='Weapon Name')
        self.craftable_tree.heading('Materials', text='Required Materials')
        self.craftable_tree.heading('Possible', text='Craftable')

        self.craftable_tree.column('Weapon', width=300)
        self.craftable_tree.column('Materials', width=400)
        self.craftable_tree.column('Possible', width=100)

    def filter_craftable_weapons(self, event=None):
        filter_material = self.material_search_entry.get().strip()
        if filter_material:
            self.check_craftable_weapons(filter_material)
        else:
            self.check_craftable_weapons()

    def populate_weapons(self):
        for i in self.weapon_tree.get_children():
            self.weapon_tree.delete(i)

        recipes = MonsterHunterWeapons.crafting_table.display_all_recipes()

        sorted_recipes = sorted(recipes, key=lambda x: x[0])

        for weapon, materials in sorted_recipes:
            self.weapon_tree.insert('', 'end', values=(weapon, ', '.join(materials)))

    def filter_weapons(self, event=None):
        search_term = self.search_entry.get().lower()

        for i in self.weapon_tree.get_children():
            self.weapon_tree.delete(i)

        recipes = MonsterHunterWeapons.crafting_table.display_all_recipes()

        for weapon, materials in recipes:
            if search_term in weapon.lower():
                self.weapon_tree.insert('', 'end', values=(weapon, ', '.join(materials)))

    def show_weapon_details(self, event):
        self.details_text.config(state=tk.NORMAL)
        self.details_text.delete(1.0, tk.END)

        selected_item = self.weapon_tree.selection()
        if not selected_item:
            self.details_text.insert(tk.END, "Select a weapon to see details.")
            self.details_text.config(state=tk.DISABLED)
            return
   
        weapon = self.weapon_tree.item(selected_item[0])['values'][0]

        upgrade_details = []
        for item, materials in MonsterHunterWeapons.crafting_table.display_all_recipes():
            if item == weapon:
                upgrade = MonsterHunterWeapons.crafting_table.get_upgrade(item)

                details = f"Weapon: {item}\n"
                details += "Materials: " + ', '.join(materials) + "\n"
                if upgrade:
                    details += f"Upgrades to: {upgrade}"

                self.details_text.insert(tk.END, details)
                break

        self.details_text.config(state=tk.DISABLED)

    def add_material(self):
        material = simpledialog.askstring("Add Material", "Enter material name:")
        if not material:
            return

        quantity = simpledialog.askinteger("Add Material", f"Enter quantity of {material}:", minvalue=1)
        if quantity is None:
            return

        self.material_inventory[material] += quantity

        self.update_inventory_view()

    def remove_material(self):
        material = simpledialog.askstring("Remove Material", "Enter material name:")
        if not material:
            return

        if material not in self.material_inventory or self.material_inventory[material] == 0:
            messagebox.showinfo("Error", f"No {material} in inventory.")
            return

        max_quantity = self.material_inventory[material]
        quantity = simpledialog.askinteger("Remove Material",
            f"Enter quantity to remove (max {max_quantity}):",
            minvalue=1,
            maxvalue=max_quantity
        )
        if quantity is None:
            return

        self.material_inventory[material] -= quantity
        if self.material_inventory[material] <= 0:
            del self.material_inventory[material]

        self.update_inventory_view()

    def update_inventory_view(self):
        for i in self.inventory_tree.get_children():
            self.inventory_tree.delete(i)

        sorted_materials = sorted(self.material_inventory.items())

        for material, quantity in sorted_materials:
            if quantity > 0:
                self.inventory_tree.insert('', 'end', values=(material, quantity))

        self.check_craftable_weapons()

    def check_craftable_weapons(self, filter_material=None):
        for i in self.craftable_tree.get_children():
            self.craftable_tree.delete(i)

        recipes = MonsterHunterWeapons.crafting_table.display_all_recipes()

        sorted_recipes = sorted(recipes, key=lambda x: x[0])

        for weapon, materials in sorted_recipes:
            required_materials = {}
            for material_entry in materials:
                parts = material_entry.split()
                qty = int(parts[0])
                material_name = ' '.join(parts[1:])
                required_materials[material_name] = qty

            if filter_material and not any(filter_material in mat for mat in required_materials):
                continue

            craftable = True
            missing_materials = {}
            for material, req_qty in required_materials.items():
                if material not in self.material_inventory or self.material_inventory[material] < req_qty:
                    craftable = False
                    missing_qty = req_qty - self.material_inventory.get(material, 0)
                    missing_materials[material] = missing_qty

            materials_str = ', '.join([f"{qty} {mat}" for mat, qty in required_materials.items()])

            status = "Yes" if craftable else "No"
            if not craftable:
                materials_str += " (Missing: " + ', '.join([f"{qty} {mat}" for mat, qty in missing_materials.items()]) + ")"
           
            self.craftable_tree.insert('', 'end', values=(weapon, materials_str, status))

    def add_to_queue(self):
        selected_item = self.weapon_tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a weapon to add to queue")
            return

        weapon = self.weapon_tree.item(selected_item[0])['values'][0]
        self.crafting_queue.add_to_queue(weapon)
        messagebox.showinfo("Queue", f"{weapon} added to crafting queue")

    def remove_from_queue(self):
        queue_window = tk.Toplevel(self.master)
        queue_window.title("Crafting Queue")
        queue_window.geometry("400x300")

        queue_tree = ttk.Treeview(queue_window, columns=('Weapon',), show='headings')
        queue_tree.heading('Weapon', text='Weapon in Queue')
        queue_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        queue_items = list(self.crafting_queue._queue)
        for weapon in queue_items:
            queue_tree.insert('', 'end', values=(weapon,))

        def delete_selected():
            selected_item = queue_tree.selection()
            if not selected_item:
                messagebox.showwarning("Warning", "Please select a weapon to remove")
                return

            weapon = queue_tree.item(selected_item[0])['values'][0]

            new_queue = deque()
            removed = False
            for item in self.crafting_queue._queue:
                if item == weapon and not removed:
                    removed = True
                    continue
                new_queue.append(item)
    
            self.crafting_queue._queue = new_queue

            queue_tree.delete(selected_item)

            messagebox.showinfo("Queue", f"{weapon} removed from crafting queue")

        remove_button = ttk.Button(queue_window, text="Remove Selected", command=delete_selected)
        remove_button.pack(pady=10)

        close_button = ttk.Button(queue_window, text="Close", command=queue_window.destroy)
        close_button.pack(pady=10)

    def remove_last_from_queue(self):
        if self.crafting_queue._queue:
            removed_weapon = self.crafting_queue._queue.pop()
            messagebox.showinfo("Queue", f"{removed_weapon} removed from the end of crafting queue")
        else:
            messagebox.showwarning("Warning", "Crafting queue is empty")

    def craft_queue(self):
        if not self.crafting_queue._queue:
            messagebox.showinfo("Queue", "Crafting queue is empty")
            return
        
        while self.crafting_queue._queue:
            self.start_crafting()

        messagebox.showinfo("Queue", "All weapons in queue have been crafted")

    def start_crafting(self):
        next_weapon = self.crafting_queue.next_to_craft()
        if next_weapon:
            materials = MonsterHunterWeapons.crafting_table.get_materials(next_weapon)

            if self.check_materials_available(materials):
                craft_window = tk.Toplevel(self.master)
                craft_window.title("Crafting Complete")
                craft_window.geometry("400x300")

                ttk.Label(craft_window, text=f"Successfully crafted: {next_weapon}", font=('Helvetica', 14, 'bold')).pack(pady=10)

                materials_frame = ttk.Frame(craft_window)
                materials_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

                ttk.Label(materials_frame, text="Materials Used:", font=('Helvetica', 12)).pack()

                materials_listbox = tk.Listbox(materials_frame)
                materials_listbox.pack(fill=tk.BOTH, expand=True)

                for material in materials:
                    materials_listbox.insert(tk.END, material)

                close_button = ttk.Button(craft_window, text="Close", command=craft_window.destroy)
                close_button.pack(pady=10)

                self.deduct_materials(materials)
                self.crafting_history.add_craft(next_weapon)
            
            if self.check_materials_available(materials):
                self.deduct_materials(materials)
                self.crafting_history.add_craft(next_weapon)
                messagebox.showinfo("Crafting", f"Crafted {next_weapon}")
            else:
                messagebox.showwarning("Warning", f"Not enough materials to craft {next_weapon}")
                self.crafting_queue._queue.popleft()

    def check_materials_available(self, materials):
        for material_entry in materials:
            parts = material_entry.split()
            qty = int(parts[0])
            material_name = ' '.join(parts[1:])
            
            if material_name not in self.material_inventory or self.material_inventory[material_name] < qty:
                return False
        return True
    
    def deduct_materials(self, materials):
        for material_entry in materials:
            parts = material_entry.split()
            qty = int(parts[0])
            material_name = ' '.join(parts[1:])
            
            self.material_inventory[material_name] -= qty

        self.update_inventory_view()

    def load_queue(self):
        for i in self.queue_tree.get_children():
            self.queue_tree.delete(i)

        cursor = self.conn.cursor()
        cursor.execute("SELECT item, quantity, status FROM crafting_queue")
        for row in cursor.fetchall():
            self.queue_tree.insert("", "end", values=row)

    def load_history(self):
        for i in self.history_tree.get_children():
            self.history_tree.delete(i)

        cursor = self.conn.cursor()
        cursor.execute("SELECT item, quantity, status, timestamp FROM crafting_history ORDER BY timestamp DESC")
        for row in cursor.fetchall():
            self.history_tree.insert("", "end", values=row)

    def __del__(self):
        self.conn.close()

def main():
    root = tk.Tk()
    app = MonsterHunterGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()
