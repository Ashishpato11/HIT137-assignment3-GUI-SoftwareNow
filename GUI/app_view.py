import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk

class AppView(tk.Tk):
    def __init__(self): 
        tk.Tk.__init__(self)
        self.title('Tkinter AI GUI')
        self.geometry('900x700')
        self.configure(bg='#f0f0f0')
        
        # Variables
        self.model_var = tk.StringVar()
        self.input_type_var = tk.StringVar(value="Text")
        self.selected_file_path = None
        self._run = None
        
        # Create menu bar
        self.create_menu()
        
        # Create main interface
        self.create_interface()
        
    def create_menu(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New")
        file_menu.add_command(label="Open")
        file_menu.add_command(label="Save")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        
        # Models menu
        models_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Models", menu=models_menu)
        models_menu.add_command(label="Load Model")
        models_menu.add_command(label="Model Info")
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About")
        
    def create_interface(self):
        # Main container
        main_frame = tk.Frame(self, bg='#f0f0f0')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Top section - Model Selection
        top_frame = tk.Frame(main_frame, bg='#f0f0f0')
        top_frame.pack(fill=tk.X, pady=5)
        
        tk.Label(top_frame, text="Model Selection:", bg='#f0f0f0', font=('Arial', 10)).pack(side=tk.LEFT)
        
        self.model_combo = ttk.Combobox(top_frame, textvariable=self.model_var, state="readonly", width=20)
        self.model_combo.pack(side=tk.LEFT, padx=(10, 10))
        self.model_combo.bind('<<ComboboxSelected>>', self.on_model_changed)
        
        self.load_model_btn = tk.Button(top_frame, text="Load Model", bg='#e0e0e0')
        self.load_model_btn.pack(side=tk.LEFT)
        
        # Middle section - Input and Output
        middle_frame = tk.Frame(main_frame, bg='#f0f0f0')
        middle_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Left side - User Input Section
        left_frame = tk.LabelFrame(middle_frame, text="User Input Section", bg='#f0f0f0', font=('Arial', 10, 'bold'))
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        # Radio buttons for input type
        radio_frame = tk.Frame(left_frame, bg='#f0f0f0')
        radio_frame.pack(fill=tk.X, pady=5)
        
        self.text_radio = tk.Radiobutton(radio_frame, text="Text", variable=self.input_type_var, 
                                        value="Text", bg='#f0f0f0', command=self.on_input_type_change)
        self.text_radio.pack(side=tk.LEFT)
        
        self.image_radio = tk.Radiobutton(radio_frame, text="Image", variable=self.input_type_var, 
                                         value="Image", bg='#f0f0f0', command=self.on_input_type_change)
        self.image_radio.pack(side=tk.LEFT, padx=(10, 0))
        
        self.browse_btn = tk.Button(radio_frame, text="Browse", command=self.browse_file, bg='#e0e0e0')
        self.browse_btn.pack(side=tk.RIGHT)
        
        # Input area
        self.text_entry = tk.Text(left_frame, height=10, width=30)
        self.text_entry.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Right side - Model Output Section
        right_frame = tk.LabelFrame(middle_frame, text="Model Output Section", bg='#f0f0f0', font=('Arial', 10, 'bold'))
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        
        tk.Label(right_frame, text="Output Display:", bg='#f0f0f0').pack(anchor=tk.W, pady=(5, 0))
        
        self.out = tk.Text(right_frame, height=10, width=30)
        self.out.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Initialize with welcome message
        self.out.insert(tk.END, "Model: Text\nResult:\nReady to process input...")
        
        # Button section
        button_frame = tk.Frame(main_frame, bg='#f0f0f0')
        button_frame.pack(fill=tk.X, pady=5)
        
        self.run_btn1 = tk.Button(button_frame, text="Run Model 1", command=lambda: self._on_run("Text Sentiment Analysis"), 
                                 bg='#d0d0d0', width=15)
        self.run_btn1.pack(side=tk.LEFT, padx=2)

        self.run_btn2 = tk.Button(button_frame, text="Run Model 2", command=lambda: self._on_run("Image Classification"), 
                                 bg='#d0d0d0', width=15)
        self.run_btn2.pack(side=tk.LEFT, padx=2)
        
        self.run_btn3 = tk.Button(button_frame, text="Run Model 3", command=lambda: self._on_run("Text-to-Image Generation"), 
                                 bg='#d0d0d0', width=15)
        self.run_btn3.pack(side=tk.LEFT, padx=2)

        self.clear_btn = tk.Button(button_frame, text="Clear", command=self.clear_output, 
                                  bg='#d0d0d0', width=12)
        self.clear_btn.pack(side=tk.LEFT, padx=2)
        
        self.open_images_btn = tk.Button(button_frame, text="Open Images", command=self.open_images_folder, 
                                        bg='#d0d0d0', width=12)
        self.open_images_btn.pack(side=tk.LEFT, padx=2)        # Bottom section - Model Information
        bottom_frame = tk.LabelFrame(main_frame, text="Model Information & Explanation", 
                                   bg='#f0f0f0', font=('Arial', 10, 'bold'))
        bottom_frame.pack(fill=tk.X, pady=(10, 5))
        
        info_container = tk.Frame(bottom_frame, bg='#f0f0f0')
        info_container.pack(fill=tk.X, padx=5, pady=5)
        
        # Left column - Selected Model Info
        left_info = tk.Frame(info_container, bg='#f0f0f0')
        left_info.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        tk.Label(left_info, text="Selected Model Info:", bg='#f0f0f0', font=('Arial', 9, 'bold')).pack(anchor=tk.W)
        
        # Dynamic model info that will be updated
        self.model_info_label = tk.Label(left_info, text="• Select a model to see details", 
                                        bg='#f0f0f0', justify=tk.LEFT, font=('Arial', 9))
        self.model_info_label.pack(anchor=tk.W, pady=(5, 0))
        
        # Right column - OOP Concepts
        right_info = tk.Frame(info_container, bg='#f0f0f0')
        right_info.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        tk.Label(right_info, text="OOP Concepts Explanation:", bg='#f0f0f0', font=('Arial', 9, 'bold')).pack(anchor=tk.W)
        
        oop_text = """• Multiple Inheritance: Models inherit from 
  BaseModelAdapter + LoggingMixin + ValidatorMixin
• Polymorphism: All models implement predict() 
  differently but share same interface
• Method Overriding: Models override info(), 
  preprocess_data(), postprocess_result()
• Encapsulation: Private attributes (__mid, __task) 
  accessed via properties
• Multiple Decorators: @log_action, @timing_decorator, 
  @error_handler, @validate_input applied together"""
        
        tk.Label(right_info, text=oop_text, bg='#f0f0f0', justify=tk.LEFT, font=('Arial', 8)).pack(anchor=tk.W, pady=(5, 0))
        
        # Notes section
        notes_frame = tk.Frame(main_frame, bg='#f0f0f0')
        notes_frame.pack(fill=tk.X, pady=(5, 0))
        
        tk.Label(notes_frame, text="Notes", bg='#f0f0f0', font=('Arial', 10, 'bold')).pack(anchor=tk.W)
        notes_text = """This GUI demonstrates advanced OOP concepts: Multiple inheritance (3+ mixins), 
Multiple decorators (4 types), Polymorphism (different predict() implementations), 
Method overriding (info(), preprocess_data()), and Encapsulation (private attributes with properties).
Models: HuggingFace Transformers for NLP and Vision tasks."""
        tk.Label(notes_frame, text=notes_text, bg='#f0f0f0', 
                font=('Arial', 8), wraplength=600).pack(anchor=tk.W)
    def populate_models(self, n): 
        self.model_combo['values'] = n
        if n:
            self.model_var.set(n[0])
            self.update_model_info(n[0])  # Update info for the first model
        
    def on_run_clicked(self, h): 
        self._run = h
    
    def get_text_input(self): 
        return self.text_entry.get('1.0', tk.END).strip()
    
    def get_selected_file(self):
        return self.selected_file_path
    
    def get_input_type(self):
        return self.input_type_var.get()
    
    def render_output(self, r): 
        self.out.delete('1.0', tk.END)
        
        # Handle different types of output
        if isinstance(r, dict) and 'image' in r:
            # Display real AI image result
            self.out.insert(tk.END, f"🤖 REAL AI IMAGE GENERATED! 🤖\n\n")
            self.out.insert(tk.END, f"Model: {r.get('model', 'Unknown')}\n")
            self.out.insert(tk.END, f"Prompt: {r.get('prompt', 'N/A')}\n")
            self.out.insert(tk.END, f"Type: {r.get('type', 'Generated')}\n")
            self.out.insert(tk.END, f"Status: REAL AI image created successfully!\n\n")
            self.out.insert(tk.END, f"📁 Saved to: {r.get('image_path', 'N/A')}\n\n")
            if 'image_path' in r:
                self.out.insert(tk.END, f"👁️ To view: Click 'Open Images' button\n")
                self.out.insert(tk.END, f"or open: {r['image_path']}")
        elif isinstance(r, dict) and r.get('status') == 'error':
            # Display error with helpful info
            self.out.insert(tk.END, f"❌ ERROR: {r.get('message', 'Unknown error')}\n\n")
            if 'diffusers' in str(r.get('message', '')):
                self.out.insert(tk.END, "💡 Solution: Install missing dependencies:\n")
                self.out.insert(tk.END, "pip install diffusers accelerate\n\n")
                self.out.insert(tk.END, "This will enable REAL AI image generation!")
        else:
            # Display text result
            self.out.insert(tk.END, str(r))
            
    def clear_output(self):
        self.out.delete('1.0', tk.END)
        self.text_entry.delete('1.0', tk.END)
        
    def browse_file(self):
        file_types = [
            ('Image files', '*.png *.jpg *.jpeg *.gif *.bmp'),
            ('Text files', '*.txt'),
            ('All files', '*.*')
        ]
        
        filename = filedialog.askopenfilename(
            title="Select a file",
            filetypes=file_types
        )
        
        if filename:
            self.selected_file_path = filename
            # Show file name in text area for reference
            self.text_entry.delete('1.0', tk.END)
            self.text_entry.insert('1.0', f"Selected file: {filename}")
            
    def on_input_type_change(self):
        input_type = self.input_type_var.get()
        if input_type == "Image":
            self.browse_btn.config(state='normal')
        else:
            self.browse_btn.config(state='normal')  # Keep browse enabled for text files too
    
    def on_model_changed(self, event=None):
        """Update model information when model selection changes"""
        selected_model = self.model_var.get()
        self.update_model_info(selected_model)
        
    def update_model_info(self, model_name):
        """Update the model information display"""
        if model_name == "Text Sentiment Analysis":
            info_text = """• Model Name: DistilBERT
• Category: Text, NLP
• Short Description: Sentiment analysis model
• Input: Text data
• Output: Positive/Negative sentiment"""
        elif model_name == "Image Classification":
            info_text = """• Model Name: Vision Transformer
• Category: Vision, Classification  
• Short Description: Image classification model
• Input: Image files (JPG, PNG)
• Output: Object class labels"""
        elif model_name == "Text-to-Image Generation":
            info_text = """• Model Name: Stable Diffusion
• Category: Text-to-Image, Generative
• Short Description: Generate images from text
• Input: Text descriptions
• Output: Generated images"""
        else:
            info_text = "• Select a model to see details"
        
        self.model_info_label.config(text=info_text)