# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DraftArticle(models.Model):
    _name = "draft.article"
    _description = "Draft Article"
    _rec_name = "name"

    name = fields.Char(string="Name", required=True)

    service_id = fields.Many2one(
        comodel_name="api.service",
        string="API Type",
        required=True,
    )

    response_json = fields.Text(string="Response JSON", required=True)


class ApiService(models.Model):
    _name = "api.service"
    _description = "API Service"
    _rec_name = "name"

    name = fields.Char(string="Name", required=True)

    param_ids = fields.One2many(
        comodel_name="api.param",
        inverse_name="service_id",
        string="Parameters",
    )

class ApiParam(models.Model):
    _name = "api.service.param"
    _description = "API Parameter"
    _rec_name = "name"

    service_id = fields.Many2one(
        comodel_name="api.service",
        string="API Type",
        required=True,
    )
    param_name = fields.Char(string="Parameter Name", required=True)
    json_equivalent = fields.Char(string="JSON Equivalent", required=True)
    


