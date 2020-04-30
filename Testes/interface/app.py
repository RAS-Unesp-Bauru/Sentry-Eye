import tkinter as tk
from buttons import Buttons

button = Buttons() 

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Nome:").pack(side="left", fill="x", pady=10)
        self.entry = tk.Entry(self, bd=2)
        self.entry.pack()
        tk.Button(self, text="Enviar",
                  command=lambda: [button.criar_pasta(), button.fecha(self.entry.get(), self), master.switch_frame(PageOne)]).pack()

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Cadastro").pack(side="top", fill="x", padx=30, pady=30)

        # openWebcam = tk.Button(self, text='Webcam', command=button.openWebcam(entry))
        # openWebcam.pack()
        openImage = tk.Button(self, text='Image', padx=10, pady=5, fg='white', bg='#263D42', command=button.openImage)
        openImage.pack()
        tk.Button(self, text="Voltar",
                  command=lambda: master.switch_frame(StartPage)).pack()

# class PageTwo(tk.Frame):
#     def __init__(self, master):
#         tk.Frame.__init__(self, master)
#         tk.Label(self, text="This is page two").pack(side="top", fill="x", pady=10)
#         tk.Button(self, text="Return to start page",
#                   command=lambda: master.switch_frame(StartPage)).pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
