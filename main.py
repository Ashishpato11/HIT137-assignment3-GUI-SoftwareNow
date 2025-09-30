from gui.app_view import AppView
from controllers.app_controller import AppController

def main(): 
    v = AppView()
    c = AppController(v)
    v.text_entry.bind('<KeyRelease>', lambda e: c.set_text_input(v.get_text_input()))
    v.mainloop()

if __name__ == '__main__': 
    main()
