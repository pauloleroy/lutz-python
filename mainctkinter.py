import tkinter as tk
import tkinter.messagebox
import customtkinter as ctk

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    w = 1180 #save user resolution
    h = 620

    def __init__(self):
        super().__init__()

        self.title("Lutz ERP")
        self.geometry(f"{App.w}x{App.h}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed
        
        #Window Frames Layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
                
        self.top_frame = ctk.CTkFrame(master=self, height= App.w*0.08)
        self.top_frame.grid(row=0, column=0, sticky="nswe", padx=10,pady = 5)
        self.middle_frame = ctk.CTkFrame(master=self, height= App.w*0.05)
        self.middle_frame.grid(row=1, column=0, sticky="nswe", padx=10,pady = 5)
        self.main_frame = ctk.CTkFrame(master=self)
        self.main_frame.grid(row=2, column=0, sticky="nswe", padx=10,pady = 5)

        #Configure Top Frame (2x8)
        
        self.top_frame.grid_rowconfigure(1, weight=1)
        
        self.top_frame.grid_columnconfigure(0)
        self.top_frame.grid_columnconfigure(1)
        self.top_frame.grid_columnconfigure(2)
        self.top_frame.grid_columnconfigure(5,weight=1)
        self.top_frame.grid_columnconfigure(6)
        
        self.main_label = ctk.CTkLabel(master=self.top_frame, text='Menu',text_font=("Roboto Medium", 20))
        self.main_label.grid(row=0, column=0)
        self.prod_button = ctk.CTkButton(master = self.top_frame,text='Produção',command = self.load_prod)
        self.prod_button.grid(row=1, column=0, padx =4, pady =3)
        self.comp_button = ctk.CTkButton(master = self.top_frame, text='Compras', command= self.load_comp)
        self.comp_button.grid(row=1, column=1, padx =4)
        self.est_button = ctk.CTkButton(master = self.top_frame, text='Estoque', command = self.load_est)
        self.est_button.grid(row=1, column=2, padx =4)
        self.ven_button = ctk.CTkButton(master = self.top_frame, text='Vendas', command= self.load_ven)
        self.ven_button.grid(row=1, column=3, padx =4)
        self.limpar_side_menu = ctk.CTkButton(master = self.top_frame, text='Limpar Menu',command= self.clear_side_menu)
        self.limpar_side_menu.grid(row=1, column=6,padx =4)


        #Configure Middle Fame (2x8)
        self.middle_frame.grid_rowconfigure(0, weight=1)
        self.middle_frame.grid_rowconfigure(1, weight=1)

        #Configure Middle Frame Entities
        self.sidemenu_label = ctk.CTkLabel(self.middle_frame, text='',text_font=("Roboto Medium", 13))
        self.sidemenu_label.grid(row=0,column=0)
        
        #Producao Buttons
        self.new_op_button = ctk.CTkButton(self.middle_frame, text='Cadastrar OP', command=lambda: print('Nova OP'))
        self.proc_op_button = ctk.CTkButton(self.middle_frame, text='Procurar OP', command=lambda: print('Editar OP'))
        self.new_prod_button = ctk.CTkButton(self.middle_frame, text='Cadastrar Produto', command=lambda: print('Proc Prod'))
        self.proc_prod_button = ctk.CTkButton(self.middle_frame, text='Procurar Produto', command=lambda: print('Ficha Prod'))
        #Compras Buttons
        self.new_mat = ctk.CTkButton(self.middle_frame, text='Novo Material', command=lambda: print(''))
        self.reg_comp = ctk.CTkButton(self.middle_frame, text='Registrar Compra', command=lambda: print(''))
        self.new_forn = ctk.CTkButton(self.middle_frame, text='Cadastrar Fornecedor', command=lambda: print(''))
        self.proc_forn = ctk.CTkButton(self.middle_frame, text='Procurar Fornecedor', command=lambda: print(''))
        #Estoque Buttons
        self.est_prod = ctk.CTkButton(self.middle_frame, text='Estoque Produtos', command=lambda: print(''))
        self.est_ins = ctk.CTkButton(self.middle_frame, text='Estoque Insumos', command=lambda: print(''))
        #Vendas Buttons
        self.cont_custos = ctk.CTkButton(self.middle_frame, text='Controle de Custos', command=lambda: print(''))

    def load_prod(self):
        self.clear_side_menu()
        self.sidemenu_label.configure(text='Produção')
        self.new_op_button.grid(row=1, column=0, padx =4, pady =3)
        self.proc_op_button.grid(row=1, column=1, padx =4)
        self.new_prod_button.grid(row=1, column=2, padx =4)
        self.proc_prod_button.grid(row=1, column=3, padx =4)
    def load_comp(self):
        self.clear_side_menu()
        self.sidemenu_label.configure(text='Compras')
        self.new_mat.grid(row=1, column=0, padx =4, pady =3)
        self.reg_comp.grid(row=1, column=1, padx =4)
        self.new_forn.grid(row=1, column=2, padx =4)
        self.proc_forn.grid(row=1, column=3, padx =4)
    def load_est(self):
        self.clear_side_menu()
        self.sidemenu_label.configure(text='Estoque')
        self.est_prod.grid(row=1, column=0, padx =4, pady =3)
        self.est_ins.grid(row=1, column=1, padx =4)
    def load_ven(self):
        self.clear_side_menu()
        self.sidemenu_label.configure(text='Vendas')
        self.cont_custos.grid(row=3, column=0, padx =4, pady =3)

    def clear_side_menu(self):
        self.sidemenu_label.configure(text='')
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
    
        

    def on_closing(self, event=0):
        self.destroy()


if __name__== '__main__':
    app = App()
    app.mainloop()