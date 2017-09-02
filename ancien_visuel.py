
from openerp import api, fields, models, _


class AncienVisuelPhoto(models.Model):
    _name = "ancien.visuel.photo"

    ancien = fields.Many2one('geoengine.demo.automatic.retailing.machine')
    ancien_description = fields.Char(string="Ancien description", index=True, required=False)
    date_debut = fields.Date(string="Date debut", index=True, required=False)
    date_fin = fields.Date(string="Date fin", index=True, required=False)
    lien_image = fields.Char(string="Lien", index=True, required=False)
    nouveau_description = fields.Char(string="Nouveau description",required=False )