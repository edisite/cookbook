# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.http import route


from odoo.addons.portal.controllers.portal import CustomerPortal

class CustomerPortalInherit(CustomerPortal):

    OPTIONAL_BILLING_FIELDS = ["zipcode", "state_id", "vat", "company_name","age"]

    @route(['/my/account'], type='http', auth='user', website=True)
    def account(self, redirect=None, **post):
        print('-----print inherit controllers--------------',post.get('age'))
        print('-----print inherit controllers--------------')

        values = self._prepare_portal_layout_values()
        partner = request.env.user.partner_id
        values.update({
            'error': {},
            'error_message': [],
        })

        if post and request.httprequest.method == 'POST':
            error, error_message = self.details_form_validate(post)
            values.update({'error': error, 'error_message': error_message})
            values.update(post)
            if not error:
                values = {key: post[key] for key in self.MANDATORY_BILLING_FIELDS}
                values.update({key: post[key] for key in self.OPTIONAL_BILLING_FIELDS if key in post})
                values.update({'country_id': int(values.pop('country_id', 0))})
                values.update({'zip': values.pop('zipcode', '')})
                if values.get('state_id') == '':
                    values.update({'state_id': False})
                partner.sudo().write(values)
                if redirect:
                    return request.redirect(redirect)
                return request.redirect('/my/home')

        countries = request.env['res.country'].sudo().search([])
        states = request.env['res.country.state'].sudo().search([])

        values.update({
            'partner': partner,
            'countries': countries,
            'states': states,
            'has_check_vat': hasattr(request.env['res.partner'], 'check_vat'),
            'redirect': redirect,
            'page_name': 'my_details',
        })

        response = request.render("portal.portal_my_details", values)
        response.headers['X-Frame-Options'] = 'DENY'
        return response



class FirstModule(http.Controller):
    @http.route('/cars', auth='public', type='http', website='True')
    def display_car(self, **kw):
        print('first route -------------------')
        cars = request.env['car.cars'].search([])
        vals = {
            'car' : cars
        }
        return request.render('first_module.display_cars',vals)

    @http.route('/cars/create/', auth='public',type='http', website='True')
    def redirect_to_form_car_create(self, **kw):

        return request.render('first_module.create_car_form')

    @http.route('/cars/save/', auth='public',type='http', website='True')
    def redirect_to_form_car_save(self, **kw):
        print('---------redirect_to_form_car_create-----')
        print('kw', kw)
        print(kw.get('doors_number'))

        request.env['car.cars'].create(
            {
                'name':kw.get('name'),
                'doors_number':kw.get('doors_number'),
                'hoors_power':kw.get('hoors_power'),
                'driver_id':kw.get('driver_id'),
            }
        )
        return request.redirect('/cars')

    @http.route('/cars/edit/', auth='public',type='http', website='True')
    def redirect_to_form_car_edit(self, **kw):
        print('------------- car id =',kw.get('id'))
        vals = {}
        car_object = request.env['car.cars'].search([('id','=',kw.get('id'))])
        vals.update({
            'car':car_object
        })
        return request.render('first_module.update_car_form',vals)


    @http.route('/cars/update/', auth='public',type='http', website='True')
    def redirect_to_form_car_update(self, **kw):
        print('------------- car id =',kw.get('id'))
        id = int(kw.get('id'))
        request.env['car.cars'].search([('id','=',id)]).write(
            {
                'name':kw.get('name'),
                'doors_number':kw.get('doors_number'),
                'hoors_power':kw.get('hoors_power')
            })
        return request.redirect('/cars')

    @http.route('/cars/delete/', auth='public',type='http', website='True')
    def redirect_to_form_car_delete(self, **kw):
        print('------------- car id =',kw.get('id'))
        car_id = int(kw.get('id'))
        request.env['car.cars'].search([('id','=',car_id)]).unlink()

        return request.redirect('/cars')
#     @http.route('/first_module/first_module/objects/<model("first_module.first_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('first_module.object', {
#             'object': obj
#         })
