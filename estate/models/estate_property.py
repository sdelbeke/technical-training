from email.policy import default

from odoo import fields, models


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"

    name = fields.Char(required=True)
    description = fields.Text()
    date_availability = fields.Date(copy=False, default=fields.Date.add(fields.date.today(), months=3))
    expected_price = fields.Float()
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    garden = fields.Boolean()
    garden_orientation = fields.Selection([("north", "North"),("south", "South"), ("east", "East"),("west", "West")])
    active= fields.Boolean(default=True)
    state = fields.Selection(selection = [("new","New"),("offer_received","Offer Received"),
                              ("offer_accepted","Offer Accepted"),("sold","Sold"),("cancelled","Cancelled")],
                             default="new",
                             copy=False,
                             required=True)
    postcode = fields.Char()