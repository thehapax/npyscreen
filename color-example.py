import npyscreen

""" 
This is the read me example 
"""
class MyForm(npyscreen.FormWithMenus):
    def create(self):
        self.add(npyscreen.TitleText, name = "Text:", value= "Just some text." )
        self.how_exited_handers[npyscreen.wgwidget.EXITED_ESCAPE]  = self.exit_application

        # BoxTitle used multiline
        obj = self.add(npyscreen.BoxTitle, name="test", custom_highlighting=True, values=["first line", "second line"])

        # get colors
        color1 = self.theme_manager.findPair(self, 'DANGER')
        color2 = self.theme_manager.findPair(self, 'IMPORTANT')

        # fill line
        obj.entry_widget.highlighting_arr_color_data = [[color1, color1, color2], [color2, color1, color2, color2]]

        # The menus are created here.
        self.m1 = self.add_menu(name="Main Menu", shortcut="^M")
        self.m1.addItemsFromList([
            ("Display Text", self.whenDisplayText, None, None, ("some text",)),
            ("Exit", self.exit_application, "é"),
        ])

    def whenDisplayText(self, argument):
       npyscreen.notify_confirm(argument)

    def exit_application(self):
        self.parentApp.setNextForm(None)
        self.editing = False
        self.parentApp.switchFormNow()


class App(npyscreen.NPSAppManaged):
    def onStart(self):
        self.registerForm("MAIN", MyForm())
 #       self.addForm("MAIN", MyForm)


if __name__ == '__main__':
    obj = App()
    obj.run()