from sloth.app.dashboard import Dashboard
from .models import *

class AppDashboard(Dashboard):
    
    def load(self, request):
        self.header(logo='/static/images/logo.png', title=None, text='Take your time!', shadow=False)
        self.footer(title='© 2022 Sloth', text='Todos os direitos reservados', version='1.0.0')

