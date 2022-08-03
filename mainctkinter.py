import tkinter as tk
import tkinter.messagebox
from turtle import width
import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    w = 1180 #save user resolution
    h = 620

    def __init__(self):
        super().__init__()
        self.state("zoomed")
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
        self.top_frame.grid_columnconfigure(5,weight=1)

        
        self.main_label = ctk.CTkLabel(master=self.top_frame, text='Menu',text_font=("Roboto Medium", 22))
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
        self.sidemenu_label = ctk.CTkLabel(self.middle_frame, text='',text_font=("Roboto Medium", 14))
        self.sidemenu_label.grid(row=0,column=0)
        
        #Producao Buttons
        self.new_op_button = ctk.CTkButton(self.middle_frame, text='Cadastrar OP', command=lambda: print('Nova OP'))
        self.proc_op_button = ctk.CTkButton(self.middle_frame, text='Procurar OP', command= self.load_proc_op)
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
    
    def load_proc_op(self):
        self.main_frame.grid_rowconfigure(4, weight=1)
        self.main_frame.grid_columnconfigure(4, weight=1)            
        self.top_label = ctk.CTkLabel(master=self.main_frame, text='Procurar OP',text_font=("Roboto Medium", 12))
        self.top_label.grid(row=0, column=0,padx =3, pady =1)
        self.nop_label = ctk.CTkLabel(master=self.main_frame, text='Número da OP')
        self.nop_label.grid(row=1, column=0,padx =3, pady =3)
        self.ref_label = ctk.CTkLabel(master=self.main_frame, text='REF')
        self.ref_label.grid(row=1, column=1,padx =3,pady =3)
        self.dt_in_label = ctk.CTkLabel(master=self.main_frame, text='Data Inicial')
        self.dt_in_label.grid(row=1, column=2,padx =3)
        self.dt_fin_label = ctk.CTkLabel(master=self.main_frame, text='Data Final')
        self.dt_fin_label.grid(row=1, column=3,padx =3)
        self.status_op_label = ctk.CTkLabel(master=self.main_frame, text='Status OP')
        self.status_op_label.grid(row=1, column=4, columnspan =2,sticky="ew",padx =3)
        self.tipo_prod_label = ctk.CTkLabel(master=self.main_frame, text='Tipo Produto')
        self.tipo_prod_label.grid(row=1, column=6,padx =3)
        self.finalizado_label = ctk.CTkLabel(master=self.main_frame, text='Finalizado')
        self.finalizado_label.grid(row=1, column=7,padx =3)
        self.cancelado_label = ctk.CTkLabel(master=self.main_frame, text='Cancelado')
        self.cancelado_label.grid(row=1, column=8,padx =3)
        
        self.nop_eb = ctk.CTkEntry(master=self.main_frame)
        self.nop_eb.grid(row=2, column=0, pady =3)
        self.ref_eb = ctk.CTkEntry(master=self.main_frame)
        self.ref_eb.grid(row=2, column=1)
        self.dt_in_eb = ctk.CTkEntry(master=self.main_frame)
        self.dt_in_eb.grid(row=2, column=2)
        self.dt_fin_eb = ctk.CTkEntry(master=self.main_frame)
        self.dt_fin_eb.grid(row=2, column=3)
        self.status_op_eb = ctk.CTkComboBox(master=self.main_frame)
        self.status_op_eb.grid(row=2, column=4, columnspan =2,sticky="ew")
        self.tipo_prod_eb = ctk.CTkComboBox(master=self.main_frame)
        self.tipo_prod_eb.grid(row=2, column=6)
        self.finalizado_eb = ctk.CTkComboBox(master=self.main_frame)
        self.finalizado_eb.grid(row=2, column=7)
        self.cancelado_eb = ctk.CTkComboBox(master=self.main_frame)
        self.cancelado_eb.grid(row=2, column=8)

        self.uptd_list_button = ctk.CTkButton(master=self.main_frame, text = 'Atualizar Lista')
        self.uptd_list_button.grid(row=3, column=0, pady =3)
        self.limp_fil_button = ctk.CTkButton(master=self.main_frame, text = 'Limpar Filtros')
        self.limp_fil_button.grid(row=3, column=1)

        self.list_op = tk.Listbox(master=self.main_frame)
        self.list_op.grid(row=4,column=0,columnspan=9, sticky="nswe",padx = 5,pady=3)

        self.editar_op_button = ctk.CTkButton(master=self.main_frame, text = 'Editar OP')
        self.editar_op_button.grid(row=5, column=0, pady =3)
        self.imp_op_button = ctk.CTkButton(master=self.main_frame, text = 'Imprimir OP')
        self.imp_op_button.grid(row=5, column=1)



    def on_closing(self, event=0):
        self.destroy()


if __name__== '__main__':
    app = App()
    app.mainloop()