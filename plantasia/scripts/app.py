import tkinter as tk
import shutil
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter import Menu
from tkinter import messagebox as msg
import tkinter.font as tkFont
from tkinter.filedialog import askopenfilename
from general_funcs import *
from PIL import Image, ImageTk

class Fonts:
    def __init__(self):
        self.font0 = tkFont.Font(size=25, weight='bold', family='Ink Free', underline=0)
        self.font1 = tkFont.Font(size=10, slant='italic', family='Malgun Ghotic')
        self.font2 = tkFont.Font(size=11, weight='bold', family='Malgun Ghotic')
        self.font3 = tkFont.Font(size=8, weight='bold', family='Narkisim')

class Text:
    def __init__(self):
        self.description = "Plantasia, all your plants and muchrooms in one place!"
        self.generate_tags()

    def generate_tags(self):
        self.properties_tag ="\n\nProperties:"
        self.side_effects_tag ="\n\nSide Effects:"

class App:
    def __init__(self):
        self.df = df
        self.win = tk.Tk()
        self.radVar = tk.IntVar()
        self.win.title('Plantasia')
        self.win.iconbitmap(f"{PATH_UTILS}growth.ico")
        self.canvas = tk.Canvas(self.win, width=580, height=640, bg='#62AC3D')
        self.canvas.pack(expand=True)
        self.win.minsize(580,640)
        self.win.maxsize(580,640)
        self.create_main_frame()
        self.create_description()
        self.main_page()
        self.create_menu_bar()

    def main_page(self):
        self.create_search_frame()
        self.set_options()
        self.set_button()
        self.front_image()

    def create_main_frame(self):
        self.main_frame = tk.Frame(self.win, bg='#FFFEC7')
        self.main_frame.place(relwidth=0.9, relheight=0.9, rely=0.05,  relx=0.05)

    def front_image(self):
        img_init = Image.open(f"{PATH_UTILS}bg_img.png")
        img_init = img_init.resize((520, 280))
        self.imgTK = ImageTk.PhotoImage(img_init)
        self.label1 = tk.Label(self.main_frame, image = self.imgTK, bg = '#FFFEC7')
        self.label1.pack()

    def create_description(self):
        self.intro_frame = tk.Frame(self.main_frame, bg='#FFFEC7')
        self.intro_frame.pack()
        self.label_title = tk.Label(self.intro_frame, text="Plantasia", foreground='#5A8A29', bg='#FFFEC7')
        self.label_title['font'] = Fonts().font0
        self.label_title.pack(side='top', pady=10)
        self.label_intro_frame = tk.Label(self.intro_frame, text=Text().description, bg='#FFFEC7')
        self.label_intro_frame['font'] = Fonts().font1
        self.label_intro_frame.pack(side='top', pady=10)

    def create_search_frame(self):
        self.search_frame = tk.Frame(self.main_frame, bg='#FFFEC7')
        self.search_frame.pack(side='top', pady=10)
        self.label_search_frame = tk.Label(self.search_frame, text='Search for:', bg='#FFFEC7')
        self.label_search_frame['font'] = Fonts().font2
        self.label_search_frame.grid(sticky="s", column=0, row=0, pady=5)

    def set_options(self):
        self.options_arr = []
        for i in range(len(options_labels)):
            self.options = tk.Radiobutton(self.search_frame, text=options_labels[i], value=i, variable=self.radVar, state='normal', bg='#FFFEC7')
            self.options.select()
            self.options.grid(column=0, row=1 + i, sticky='w', pady=2)
            self.options_arr.append(self.options)

    def set_button(self):
        self.button1 = tk.Button(self.search_frame, text='  Ready   ', command=self.click_me, bg='#62AC3D', activebackground='#5A8A29', fg='#FFFFFF')
        self.button1['font'] = Fonts().font3
        self.button1.grid(sticky="s", column=0, row=len(options_labels) + 1, pady=20)

    def set_species_frame(self):
        self.species_frame_label = tk.Label(self.search_frame, text='Select Specie:', bg='#FFFEC7')
        self.species_frame_label['font'] = Fonts().font2
        self.species_frame_label.grid(sticky="s", column=0, row=0, pady=5)
        self.combobox_species = ttk.Combobox(self.search_frame, values=species, width=20, state='normal')
        self.combobox_species.current(0)  # to give first element in species array
        self.combobox_species.grid(sticky="s", column=0, row=1, pady=5, padx=5)
        self.button_select = tk.Button(self.search_frame, text=' Select ', command= self.click_species, bg='#62AC3D', activebackground='#5A8A29', fg='#FFFFFF')
        self.button_select['font'] = Fonts().font3
        self.button_select.grid(sticky="s", column=0, row=2, pady=10)
        specie_img = Image.open(f"{PATH_UTILS}specie_img.png")
        specie_img = specie_img.resize((200, 200))
        self.imgTK = ImageTk.PhotoImage(specie_img)
        self.label1 = tk.Label(self.search_frame, image = self.imgTK, bg = '#FFFEC7')
        self.label1.grid(sticky="s", column=0, row=3, pady=20)
        self.button_back = tk.Button(self.search_frame, text=' Back ', bg='#156823', command=self.click_back, activebackground='#5A8A29', fg='#FFFFFF')
        self.button_back['font'] = Fonts().font3
        self.button_back.grid(sticky="s", column=0, row=4, pady=30)

    def set_families_frame(self):
        self.families_frame_label = tk.Label(self.search_frame, text='Select Family:', bg='#FFFEC7')
        self.families_frame_label['font'] = Fonts().font2
        self.families_frame_label.grid(sticky="s", column=0, row=0, pady=5)
        self.combobox_families = ttk.Combobox(self.search_frame, values=families, width=20, state='normal')
        self.combobox_families.current(0)
        self.combobox_families.grid(sticky="s", column=0, row=1, pady=5, padx=5)
        self.button_select = tk.Button(self.search_frame, text=' Select ', command= self.click_families, bg='#62AC3D', activebackground='#5A8A29', fg='#FFFFFF')
        self.button_select['font'] = Fonts().font3
        self.button_select.grid(sticky="s", column=0, row=2, pady=10)
        family_img = Image.open(f"{PATH_UTILS}family_img.png")
        family_img = family_img.resize((100, 200))
        self.imgTK = ImageTk.PhotoImage(family_img)
        self.label1 = tk.Label(self.search_frame, image = self.imgTK, bg = '#FFFEC7')
        self.label1.grid(sticky="s", column=0, row=3, pady=20)
        self.button_back = tk.Button(self.search_frame, text=' Back ', bg='#156823', command=self.click_back, activebackground='#5A8A29', fg='#FFFFFF')
        self.button_back['font'] = Fonts().font3
        self.button_back.grid(sticky="s", column=0, row=4, pady=30)

    def set_properties_frame(self):
        self.properties_frame_label = tk.Label(self.search_frame, text='Select Properties:', bg='#FFFEC7')
        self.properties_frame_label['font'] = Fonts().font2
        self.properties_frame_label.grid(sticky="s", column=0, row=0, pady=5)
        self.combobox_properties = ttk.Combobox(self.search_frame, values=properties, width=20, state='normal')
        self.combobox_properties.current(0)
        self.combobox_properties.grid(sticky="s", column=0, row=1, pady=5, padx=5)
        self.button_select = tk.Button(self.search_frame, text=' Select ', command= self.click_properties, bg='#62AC3D', activebackground='#5A8A29', fg='#FFFFFF')
        self.button_select['font'] = Fonts().font3
        self.button_select.grid(sticky="s", column=0, row=2, pady=10)
        properties_img = Image.open(f"{PATH_UTILS}properties_img.png")
        properties_img = properties_img.resize((250, 150))
        self.imgTK = ImageTk.PhotoImage(properties_img)
        self.label1 = tk.Label(self.search_frame, image = self.imgTK, bg = '#FFFEC7')
        self.label1.grid(sticky="s", column=0, row=3, pady=20)
        self.button_back = tk.Button(self.search_frame, text=' Back ', bg='#156823', command=self.click_back, activebackground='#5A8A29', fg='#FFFFFF')
        self.button_back['font'] = Fonts().font3
        self.button_back.grid(sticky="s", column=0, row=4, pady=30)

    def click_me(self):
        val = self.radVar.get()
        if val == 0 or val == 1 or val == 2:
             for i in range(len(self.options_arr)):
                 self.label_search_frame.destroy()
                 self.options_arr[i].destroy()
                 self.button1.destroy()
                 if val == 0:
                    self.set_species_frame()
                 if val == 1:
                    self.set_families_frame()
                 if val == 2:
                    self.set_properties_frame()

    def click_back(self):
        self.create_main_frame()
        self.create_description()
        self.main_page()

    def click_species(self):
        if self.combobox_species.get() == str_no_species:
            msg.showerror('Error', 'Please you need to add a specie first')
            return
        else:
            title = self.combobox_species.get()
            self.main_frame.destroy()
            self.create_main_frame()
            self.label_species_title = tk.Label(self.main_frame, text=title, foreground='#5A8A29', bg='#FFFEC7')
            self.label_species_title['font'] = Fonts().font0
            self.label_species_title.pack(side='top', pady = 5)
            img = Image.open(f"{PATH_IMG}\{title}.jpg")
            img = img.resize((300, 270))
            self.imgTK = ImageTk.PhotoImage(img)
            self.label1 = tk.Label(self.main_frame, image = self.imgTK)
            self.label1.pack()
            self.st = ScrolledText(self.main_frame, width=35, height=10)
            self.st.pack(fill=tk.BOTH, expand=True, side='top', pady = 5, padx = 40)
            specie_row = df.loc[df[labels[0]] == title] #takes row of the title's index
            self.specie_description = specie_row['description'].tolist()[0]
            self.properties_text = specie_row['properties'].tolist()[0]
            self.properties_text = convert_list(self.properties_text)
            self.side_effects_text = specie_row['side_effects'].tolist()[0]
            self.side_effects_text = convert_list(self.side_effects_text)
            self.text_specie = self.specie_description + Text().properties_tag + self.properties_text + Text().side_effects_tag + self.side_effects_text
            self.st.insert(tk.INSERT, self.text_specie)
            self.button_back = tk.Button(self.main_frame, text=' Back ', bg='#156823', command=self.click_back, activebackground='#5A8A29', fg='#FFFFFF')
            self.button_back['font'] = Fonts().font3
            self.button_back.pack(side='top', pady = 5)

    def click_families(self):
        global title
        if self.combobox_families.get() == str_no_species:
            msg.showerror('Error', 'Please you need to add a specie first')
            return
        else:
            title = self.combobox_families.get()
            species_by_families = get_species_by_family(df, title)
            self.main_frame.destroy()
            self.create_main_frame()
            self.label_families_title = tk.Label(self.main_frame, text=title, foreground='#5A8A29', bg='#FFFEC7')
            self.label_families_title['font'] = Fonts().font0
            self.label_families_title.pack(side = 'top', pady = 10)
            self.search_species_by_families = tk.Frame(self.main_frame, bg='#FFFEC7')
            self.search_species_by_families.pack(side = 'top', pady = 30)
            self.label_search_species_by_families = tk.Label(self.search_species_by_families,
            text='Species within this family:', bg='#FFFEC7')
            self.label_search_species_by_families['font'] = Fonts().font2
            self.label_search_species_by_families.pack(side = 'top', pady = 10)
            self.combobox_species = ttk.Combobox(self.search_species_by_families, values=species_by_families, width=20, state='normal')
            self.combobox_species.current()
            self.combobox_species.pack(side = 'top', pady = 0)
            self.button_select = tk.Button(self.search_species_by_families, text=' Select ', command= self.click_species, bg='#62AC3D', activebackground='#5A8A29', fg='#FFFFFF')
            self.button_select['font'] = Fonts().font3
            self.button_select.pack(side = 'top', pady = 10)
            self.button_back = tk.Button(self.search_species_by_families, text=' Back ', bg='#156823', command=self.click_back, activebackground='#5A8A29', fg='#FFFFFF')
            self.button_back['font'] = Fonts().font3
            self.button_back.pack(side = 'top', pady = 150)

    def click_properties(self):
        if self.combobox_properties.get() == str_no_species:
            msg.showerror('Error', 'Please you need to add a specie first')
            return
        else:
            title = self.combobox_properties.get()
            species_by_properties = get_species_by_properties(df, title)
            self.main_frame.destroy()
            self.create_main_frame()
            self.label_properties_title = tk.Label(self.main_frame, text=title, foreground='#5A8A29', bg='#FFFEC7')
            self.label_properties_title['font'] = Fonts().font0
            self.label_properties_title.pack(side = 'top', pady = 30)
            self.search_species_by_properties = tk.Frame(self.main_frame, bg='#FFFEC7')
            self.search_species_by_properties.pack(side = 'top', pady = 10)
            self.label_search_species_by_properties = tk.Label(self.search_species_by_properties,
            text='Species with this property:', bg='#FFFEC7')
            self.label_search_species_by_properties['font'] = Fonts().font2
            self.label_search_species_by_properties.pack(side = 'top', pady = 10)
            self.combobox_species = ttk.Combobox(self.search_species_by_properties, values=species_by_properties, width=20, state='normal')
            self.combobox_species.current(0)
            self.combobox_species.pack(side = 'top', pady = 0)
            self.button_select = tk.Button(self.search_species_by_properties, text=' Select ', command= self.click_species, bg='#62AC3D', activebackground='#5A8A29', fg='#FFFFFF')
            self.button_select['font'] = Fonts().font3
            self.button_select.pack(side = 'top', pady = 10)
            self.button_back = tk.Button(self.search_species_by_properties, text=' Back ', bg='#156823', command=self.click_back, activebackground='#5A8A29', fg='#FFFFFF')
            self.button_back['font'] = Fonts().font3
            self.button_back.pack(side = 'top', pady = 150)

    def create_specie(self):
        self.main_frame.destroy()
        self.create_main_frame()
        self.label_new_specie = tk.Label(self.main_frame, text='New Specie', foreground='#5A8A29', bg='#FFFEC7')
        self.label_new_specie['font'] = Fonts().font0
        self.label_new_specie.grid(sticky='n', pady = 20, column = 0, row = 0)
        self.sub_frame = tk.Frame(self.main_frame, bg='#FFFEC7')
        self.sub_frame.grid(sticky = 'nw', column = 0, row = 1)
        self.frame_new_specie = tk.LabelFrame(self.sub_frame, bg='#FFFEC7', text= "Details", relief= tk.RIDGE)
        self.frame_new_specie.grid(sticky = 'nw', column = 0, row = 0, pady = 5, padx = 5)
        self.frame_right = tk.Frame(self.sub_frame, bg='#FFFEC7')
        self.frame_right.grid(sticky = 'n', column = 1, row = 0, pady = 5, padx = 20)
        self.frame_description = tk.LabelFrame(self.frame_right, bg='#FFFEC7', text= "Description", relief= tk.RIDGE)
        self.frame_description.grid(sticky = 'nw', column = 0, row = 0, pady = 5, padx = 20)
        self.frame_image = tk.LabelFrame(self.frame_right, bg='#FFFEC7', text= "Upload an Image", relief= tk.RIDGE)
        self.frame_image.grid(sticky = 'nw', column = 0, row = 1, pady = 15, padx = 20)

        #name
        self.specie_name_label = tk.Label(self.frame_new_specie, text="Name:", bg='#FFFEC7')
        self.specie_name_label.grid(sticky = 'nw', column = 0, row = 0, pady = 10, padx = 5)
        self.specie_name_entry = tk.Entry(self.frame_new_specie)
        self.specie_name_entry.grid(sticky = 'nw', column = 1, row = 0, pady = 10, padx = 5)

        #family
        self.specie_family_label = tk.Label(self.frame_new_specie, text="Family:", bg='#FFFEC7')
        self.specie_family_label.grid(sticky = 'nw', column = 0, row = 1, pady = 10, padx = 5)
        self.specie_family_combobox = ttk.Combobox(self.frame_new_specie, values=families, state='normal', width= 17)
        self.specie_family_combobox.grid(sticky = 'nw', column = 1, row = 1, pady = 10, padx = 5)

        #description
        self.specie_description_st = ScrolledText(self.frame_description, width=25, height=5)
        self.specie_description_st.grid(sticky = 'nw', column = 0, row = 0, pady = 10, padx = 5)

        #properties
        self.properties_container = tk.Label(self.frame_new_specie, bg='#FFFEC7')
        self.properties_container.grid(sticky = 'nw', column = 1, row = 2, pady = 10, padx = 4)
        self.specie_properties_label = tk.Label(self.frame_new_specie, text="Properties:", bg='#FFFEC7')
        self.specie_properties_label.grid(sticky = 'nw', column = 0, row = 2, pady = 10, padx = 4)
        self.properties_entries = []
        for i in range(7):
            self.specie_properties_combobox = ttk.Combobox(self.properties_container, values=properties, state='normal', width = 17)
            self.specie_properties_combobox.grid(sticky = 'nw', column = 1, row = i, pady = 0)
            self.properties_entries.append(self.specie_properties_combobox)

        #sideeffects
        self.sides_container = tk.Label(self.frame_new_specie, bg='#FFFEC7')
        self.sides_container.grid(sticky = 'nw', column = 1, row = 3, pady = 10, padx = 4)
        self.specie_sides_label = tk.Label(self.frame_new_specie, text="Side Effects:", bg='#FFFEC7')
        self.specie_sides_label.grid(sticky = 'nw', column = 0, row = 3, pady = 10, padx = 3)
        self.sides_entries = []
        for i in range(7):
            self.specie_sides_combobox = ttk.Combobox(self.sides_container, values=side_effects, state='normal', width = 17)
            self.specie_sides_combobox.grid(sticky = 'nw', column = 1, row = i, pady = 0)
            self.sides_entries.append(self.specie_sides_combobox)

        #image
        img = Image.open(f"{PATH_UTILS}upload.png")
        img = img.resize((40, 40))
        self.imgTK = ImageTk.PhotoImage(img)
        self.button_img = tk.Button(self.frame_image, image = self.imgTK, bg='#FFFEC7', command=self.upload_image)
        self.button_img.grid(sticky = 'n', column=0, row=0, pady=5, padx=10)
        self.label_img = tk.Label(self.frame_image, text="*please name the picture \n exactly as the specie's name", foreground='#FF0000', bg='#FFFEC7')
        self.label_img.grid(sticky = 'n', column = 0, row = 1)

        #submit
        self.button_select = tk.Button(self.frame_right, text=' Submit ', command= self.upload_specie, bg='#62AC3D', activebackground='#5A8A29', fg='#FFFFFF')
        self.button_select['font'] = Fonts().font3
        self.button_select.grid(sticky = 'w', column = 0, row = 2, pady = 10, padx=80)

        #back
        self.button_back = tk.Button(self.main_frame, text=' Back ', bg='#156823', command=self.click_back, activebackground='#5A8A29', fg='#FFFFFF')
        self.button_back['font'] = Fonts().font3
        self.button_back.grid(sticky = 'n', row = 2, pady = 10, column = 0)

    def callback(self):
        self.main_frame.destroy()
        self.create_main_frame()
        self.search_frame = tk.Frame(self.main_frame, bg='#FFFEC7')
        self.search_frame.pack(side='top', pady=10)
        self.species_frame_label = tk.Label(self.search_frame, text='Select specie to remove:', bg='#FFFEC7')
        self.species_frame_label['font'] = Fonts().font2
        self.species_frame_label.grid(sticky="s", column=0, row=0, pady=5)
        self.combobox_species_remove = ttk.Combobox(self.search_frame, values=species, width=20, state='normal')
        self.combobox_species_remove.current(0)  # to give first element in species array
        self.combobox_species_remove.grid(sticky="s", column=0, row=1, pady=5, padx=5)
        self.button_select = tk.Button(self.search_frame, text=' Select ', command= self.remove_specie, bg='#62AC3D', activebackground='#5A8A29', fg='#FFFFFF')
        self.button_select['font'] = Fonts().font3
        self.button_select.grid(sticky="s", column=0, row=2, pady=10)
        self.button_back = tk.Button(self.search_frame, text=' Back ', bg='#156823', command=self.click_back, activebackground='#5A8A29', fg='#FFFFFF')
        self.button_back['font'] = Fonts().font3
        self.button_back.grid(sticky="s", column=0, row=3, pady=230)

    def remove_specie(self):
        global species
        global families
        global descriptions
        global properties
        global side_effects
        global df
        if self.combobox_species_remove.get() == str_no_species:
            msg.showerror('Error', 'Please you need to add a specie first')
            return
        else:
            result = msg.askyesno(title='Warning', message='Are you sure you want to remove this specie?')
            if result:
                remove_specie = self.combobox_species_remove.get()
                row_to_remove = df.loc[df['specie'] == remove_specie].index
                df = df.drop(row_to_remove[0])
                df.to_json(PATH_DATA)
                df = pd.read_json(PATH_DATA)
                species = get_species_array(df)
                descriptions = get_descriptions_array(df)
                properties = get_properties_array(df)
                families = get_families_array(df)
                side_effects = get_side_effects_array(df)
                os.remove(PATH_IMG + remove_specie + '.jpg')
                self.callback()
            else:
                return

    def create_menu_bar(self):
        self.menu_bar = Menu(self.win)
        self.win.config(menu = self.menu_bar)
        self.add = Menu(self.menu_bar, tearoff = 0)
        self.menu_bar.add_command(label = 'New', command= self.create_specie)
        self.menu_bar.add_cascade(label  = 'Remove', command= self.callback)

    def upload_image(self):
        global set_file
        self.files = [('.jpg', '*.jpg')]
        self.image = askopenfilename(filetypes = self.files, defaultextension = self.files)
        self.img_split = self.image.split('/')
        self.file = self.img_split[len(self.img_split)-1]
        shutil.copyfile(self.image, PATH_IMG + self.file)
        self.filename = self.file.split('.')
        self.filename = self.filename[0]
        set_file = 1

    def upload_specie(self):
        global species
        global families
        global descriptions
        global properties
        global side_effects
        global df
        self.properties_array = []
        self.sides_array = []
        for combobox in self.properties_entries:
            get_combobox = combobox.get()
            self.properties_array.append(get_combobox)
        for combobox in self.sides_entries:
            get_combobox = combobox.get()
            self.sides_array.append(get_combobox)
        if set_file == 0:
            self.file = ''
            self.filename = ''
        self.error = 1
        while self.error == 1:
            if self.specie_name_entry.get() == '' or self.specie_family_combobox.get() == '' or self.properties_entries[0] == '' or self.sides_entries[0] == '' or self.specie_description_st.get("1.0",'end-1c') == '' or self.file == '':
                msg.showerror('Error', 'Missing field!')
                return
            elif self.filename != self.specie_name_entry.get():
                os.remove(PATH_IMG + self.file)
                msg.showerror('Error', "Please save the image with the specie name.")
                return
            elif self.specie_name_entry.get() in species:
                msg.showerror('Error', "This Specie's name already exists. Please insert a different one.")
                return
            else:
                self.properties_array = list(set(i for i in self.properties_array if i != ""))
                self.sides_array = list(set(i for i in self.sides_array if i != ""))
                self.specie_description_st = self.specie_description_st.get("1.0",'end-1c').split('  ')
                self.specie_description_st = self.specie_description_st[0]
                self.new_row = {
                    labels[0]:self.specie_name_entry.get(),
                    labels[1]:self.specie_family_combobox.get(),
                    labels[2]:self.specie_description_st,
                    labels[3]:self.properties_array,
                    labels[4]:self.sides_array}
                df = df.append(self.new_row, ignore_index=True)
                df.to_json(PATH_DATA, orient='split')
                df = pd.read_json(PATH_DATA, orient='split')
                species = get_species_array(df)
                descriptions = get_descriptions_array(df)
                properties = get_properties_array(df)
                families = get_families_array(df)
                side_effects = get_side_effects_array(df)
                self.error = 0
                msg.showinfo(title='Info', message='A Specie has been added to the list!')
                self.create_specie()
                return

app = App()
app.win.mainloop()
