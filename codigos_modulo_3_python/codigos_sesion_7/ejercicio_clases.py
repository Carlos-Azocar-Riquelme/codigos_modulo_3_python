
class MobilePhone:
    
    def __init__(self, manufacturer, screen_size, num_cores):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores=num_cores
        self.status = False
        self.apps = []
    
    def power_on(self):
        self.status= True
        print('Hola')
    
    def power_off(self):
        self.status = False
        print('Adios')
        
    def install_app(self, app):
        self.apps.append(app)
        print('Instalando', app)

    
    def uninstall_app(self,app):
        # if app in self.apps:
        self.apps.remove(app)
        print('Desinstalando', app)
    
    

Celular = MobilePhone('Manufactura', '1920 X 1080', '4', )

Celular.install_app('whatsapp')
Celular.install_app('Facebook')


print(Celular.apps)

print(Celular.uninstall_app('Whatsapp'))
print(Celular.apps)

