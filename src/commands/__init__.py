# Registro central de comandos
from .admin import register_admin_commands
from .fun import register_fun_commands
from .products import register_product_commands
from .utils import register_util_commands


def register_commands(bot):
    register_util_commands(bot)
    register_admin_commands(bot)
    register_fun_commands(bot)
    register_product_commands(bot)
