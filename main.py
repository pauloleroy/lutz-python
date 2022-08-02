import tkinter as tk


class MainWindow:
    def __init__(self, master):  
        self.master = master  
        self.frame = tk.Frame(self.master)  
        self.main_label = tk.Label(self.master, text='Menu')
        self.main_label.grid(row=0, column=0, columnspan=5,padx=100,pady=10)
        self.op_button = tk.Button(self.master, text='OP',command = self.load_op)
        self.op_button.grid(row=1, column=0, sticky='EW')
        self.prod_button = tk.Button(self.master, text='Produto', command= self.load_produto)
        self.prod_button.grid(row=1, column=1,sticky='EW')
        self.ins_button = tk.Button(self.master, text='Insumos')
        self.ins_button.grid(row=1, column=2,sticky='EW')
        self.forn_button = tk.Button(self.master, text='Fornecedores')
        self.forn_button.grid(row=1, column=3,sticky='EW')
        self.cust_button = tk.Button(self.master, text='Controle de Custo')
        self.cust_button.grid(row=1, column=4,sticky='EW')
        self.limpar_side_menu = tk.Button(self.master, text='Limpar Menu',command= self.clear_side_menu)
        self.limpar_side_menu.grid(row=1, column=5,sticky='EW')
        
        #sidemenu buttons
        self.nova_op_button = tk.Button(self.master, text='Nova OP', command=lambda: print('Nova OP'))
        self.editar_op_button = tk.Button(self.master, text='Editar OP', command=lambda: print('Editar OP'))
        self.imp_op_button = tk.Button(self.master, text='Imprimir OP', command=lambda: print('Imprimir OP'))
        self.proc_prod_button = tk.Button(self.master, text='Procurar Prod', command=lambda: print('Proc Prod'))
        self.imp_prod_button = tk.Button(self.master, text='Ficha Prod', command=lambda: print('Ficha Prod'))
        
        #Frame
        self.frame = tk.LabelFrame(self.master, text='titulo', width=400, height=400)
        self.frame.grid(row=3,column=0, columnspan=7)

    def clear_side_menu(self):
        self.nova_op_button.grid_forget()
        self.editar_op_button.grid_forget()
        self.imp_op_button.grid_forget()
        self.proc_prod_button.grid_forget()
        self.imp_prod_button.grid_forget()

    def load_produto(self):
        self.clear_side_menu()
        self.proc_prod_button.grid(row=2, column=0,sticky='EW')
        self.imp_prod_button.grid(row=2, column=1,sticky='EW')

    def load_op(self):
        self.clear_side_menu()
        self.nova_op_button.grid(row=2, column=0,sticky='EW')
        self.editar_op_button.grid(row=2, column=1,sticky='EW')
        self.imp_op_button.grid(row=2, column=2,sticky='EW')

    def open_op(self):         
        self.newWindow = tk.Toplevel(self.master)            
        self.app = OpWindow(self.newWindow)
        self.newWindow.grab_set()
    
    def open_produto(self):         
        self.newWindow = tk.Toplevel(self.master)            
        self.app = ProdWindow(self.newWindow)
        self.newWindow.grab_set()



class OpWindow:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.main_label = tk.Label(self.master, text='Menu')
        self.main_label.grid(row=0, column=0, columnspan=2,padx=100,pady=10)

class ProdWindow:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.main_label = tk.Label(self.master, text='Produto')
        self.main_label.grid(row=0, column=0, columnspan=2,padx=100,pady=10)

    

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    
    root.mainloop()
