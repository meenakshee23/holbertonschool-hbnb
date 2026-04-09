#!/usr/bin/python3

from flask_restx import Namespace, Resource, fields
from app.services import facade
from flask_jwt_extended import jwt_required, get_jwt
from flask import request

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name of the user'),
    'last_name': fields.String(required=True, description='Last name of the user'),
    'email': fields.String(required=True, description='Email of the user')
})


@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def post(self):
        """Register a new user"""
        user_data = api.payload
        current_user = get_jwt()
        
        # If 'is_admin' is part of the identity payload
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403
        
        email = user_data.get('email')
        if facade.get_user_by_email(email):
            return {'error': 'Email already registered'}, 400
        
        new_user = facade.create_user(user_data)

        return {
            'id': new_user.id,
            'first_name': new_user.first_name,
            'last_name': new_user.last_name,
            'email': new_user.email
        }, 201

    @api.response(200, 'List of users retrieved successfully')
    def get(self):
        """Retrieve list of all users"""
        users = facade.get_all_users()
        return [{'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email} for user in users], 200


@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'User details retrieved successfully')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get user details by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}, 200

    @api.expect(user_model, validate=True)
    @api.response(200, 'User successfully updated')
    @api.response(404, 'User not found')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def put(self, user_id):
        """Update a user by ID"""
        
        current_user = get_jwt()
        if not current_user.get('is_admin'):
            return {'error': 'Admin privileges required'}, 403
    
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404

        data = api.payload
        
        email = data.get('email')
        if email:
            existing = facade.get_user_by_email(email)
            if existing and existing.id != user_id:
                return {'error': 'Email already in use'}, 400
            
            password = data.get('password')
            if password:
                user.password = facade.hash_password(password)

        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        user.email = data.get('email', user.email)

        return {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email}, 200
