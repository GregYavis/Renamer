import os
import random
import tkinter as tk
from tkinter import filedialog


class FolderSelect:
    def __init__(self, master):
        self.select_path = None
        self.master = master
        self.frame = tk.Frame(self.master)
        select_button = tk.Button(self.master, text='Select folder', fg='black', width=40, command=self.select_folder)
        select_button.pack()
        self.frame.pack()
        self.valid_images_formats = ['.jpg', '.gif', '.png']
        self.rename_template = 'DIM_'

    def select_folder(self):
        self.select_path = filedialog.askdirectory()
        self._get_images()
        self.rename_images()
        self.master.destroy()

    def _get_images(self):
        # for file in os.listdir(self.select_path):
        self.images_names = self.get_images()

        self.digit_len_foundation = '0' * (len(str(len(self.images_names))))

    def get_images(self):
        return [file for file in os.listdir(self.select_path) if self.file_extension(file) in self.valid_images_formats]

    @staticmethod
    def file_extension(file):
        return os.path.splitext(file)[1]

    def get_full_path(self, filename):
        return os.path.join(self.select_path, filename)

    def _index_for_name(self, ind: int):
        ind = str(ind)
        if len(ind) < len(self.digit_len_foundation):
            return ''.join(['0' * (len(self.digit_len_foundation) - len(ind)), ind])
        else:
            return ind

    def rename_images(self):
        for index, file in enumerate(sorted(self.get_images(), key=lambda k: random.random())):
            old_name = self.get_full_path(file)
            new_name = self.get_full_path(
                filename=''.join(['tmp', self._index_for_name(index), self.file_extension(file)]))
            os.rename(old_name, new_name)
        
        for index, file in enumerate(self.get_images()):
            os.rename(self.get_full_path(file), self.get_full_path(
                filename=''.join([self.rename_template, self._index_for_name(index), self.file_extension(file)])))


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Select directory')
    FolderSelect(root)
    root.mainloop()
