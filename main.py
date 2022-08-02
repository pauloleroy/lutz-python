import tkinter as tk


class MainWindow:
    def __init__(self, master):  
        self.master = master  
        self.frame = tk.Frame(self.master)
        #1st Row - Main labels
        self.main_label = tk.Label(self.master, text='Menu')
        self.main_label.grid(row=0, column=0, columnspan=5,padx=100,pady=10)
        self.prod_button = tk.Button(self.master,text='Produção', padx =10,command = self.load_prod)
        self.prod_button.grid(row=1, column=0, sticky='EW')
        self.comp_button = tk.Button(self.master, text='Compras', command= self.load_comp)
        self.comp_button.grid(row=1, column=1,sticky='EW')
        self.est_button = tk.Button(self.master, text='Estoque', command = self.load_est)
        self.est_button.grid(row=1, column=2,sticky='EW')
        self.ven_button = tk.Button(self.master, text='Vendas', command= self.load_ven)
        self.ven_button.grid(row=1, column=3,sticky='EW')
        self.limpar_side_menu = tk.Button(self.master, text='Limpar Menu',command= self.clear_side_menu)
        self.limpar_side_menu.grid(row=1, column=6,sticky='EW')
        

        #2nd row - sidemenu labels
        self.sidemenu_label = tk.Label(self.master, text='')
        self.sidemenu_label.grid(row=2,column=0)
        
        #3rd row - sidemenu buttons
        self.place_holder = tk.Label(self.master, text="")
        self.place_holder.grid(row=3, column=0,sticky='EW')
        #Producao Buttons
        self.new_op_button = tk.Button(self.master, text='Cadastrar OP', command=lambda: print('Nova OP'))
        self.proc_op_button = tk.Button(self.master, text='Procurar OP', command=lambda: print('Editar OP'))
        self.new_prod_button = tk.Button(self.master, text='Cadastrar Produto', command=lambda: print('Proc Prod'))
        self.proc_prod_button = tk.Button(self.master, text='Procurar Produto', command=lambda: print('Ficha Prod'))
        #Compras Buttons
        self.new_mat = tk.Button(self.master, text='Novo Material', command=lambda: print(''))
        self.reg_comp = tk.Button(self.master, text='Registrar Compra', command=lambda: print(''))
        self.new_forn = tk.Button(self.master, text='Cadastrar Fornecedor', command=lambda: print(''))
        self.proc_forn = tk.Button(self.master, text='Procurar Fornecedor', command=lambda: print(''))
        #Estoque Buttons
        self.est_prod = tk.Button(self.master, text='Estoque Produtos', command=lambda: print(''))
        self.est_ins = tk.Button(self.master, text='Estoque Insumos', command=lambda: print(''))
        #Vendas Buttons
        self.cont_custos = tk.Button(self.master, text='Controle de Custos', command=lambda: print(''))
        
                
        #Frame
        self.frame = tk.LabelFrame(self.master, text='Lutz', width=1280, height=500)
        self.frame.grid(row=4,column=0, columnspan=7)

    def clear_side_menu(self):
        self.sidemenu_label.config(text='')
        self.frame.config(text='Lutz')
        self.new_op_button.grid_forget()
        self.proc_op_button.grid_forget()
        self.new_prod_button.grid_forget()
        self.proc_prod_button.grid_forget()
        self.new_mat.grid_forget()
        self.reg_comp.grid_forget()
        self.new_forn.grid_forget()
        self.proc_forn.grid_forget()
        self.est_prod.grid_forget()
        self.est_ins.grid_forget()
        self.cont_custos.grid_forget()
        self.place_holder.grid(row=3, column=0,sticky='EW')

    def load_prod(self):
        self.clear_side_menu()
        self.sidemenu_label.config(text='Produção')
        self.new_op_button.grid(row=3, column=0,sticky='EW')
        self.proc_op_button.grid(row=3, column=1,sticky='EW')
        self.new_prod_button.grid(row=3, column=2,sticky='EW')
        self.proc_prod_button.grid(row=3, column=3,sticky='EW')

    def load_comp(self):
        self.clear_side_menu()
        self.sidemenu_label.config(text='Compras')
        self.new_mat.grid(row=3, column=0,sticky='EW')
        self.reg_comp.grid(row=3, column=1,sticky='EW')
        self.new_forn.grid(row=3, column=2,sticky='EW')
        self.proc_forn.grid(row=3, column=3,sticky='EW')

    def load_est(self):
        self.clear_side_menu()
        self.sidemenu_label.config(text='Estoque')
        self.est_prod.grid(row=3, column=0,sticky='EW')
        self.est_ins.grid(row=3, column=1,sticky='EW')
    
    def load_ven(self):
        self.clear_side_menu()
        self.sidemenu_label.config(text='Vendas')
        self.cont_custos.grid(row=3, column=0,sticky='EW')






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
    root.state('zoomed')
    app = MainWindow(root)
    
    root.mainloop()
