from odoo import fields, models


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"


    name = fields.Char(required=True)
    description = fields.Text()
    date_availability = fields.Date()
    expected_price = fields.Float()
    bedrooms = fields.Integer()
    garden = fields.Boolean()
    garden_orientation = fields.Selection([("north", "North"),("south", "South"), ("east", "East"),("west", "West")])