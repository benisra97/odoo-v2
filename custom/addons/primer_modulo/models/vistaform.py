from odoo import fields, models

class Vistaform(models.Model):
        _inherit = 'sale.order'

        entrega_tiempo = fields.Char(string="Tiempo de entrega")
        vendedor_ini = fields.Char(string="Iniciales del vendedor")
        estado_pago= fields.Selection([('not_paid','No pagado'),('yes_paid','Pagado')], default='not_paid')


