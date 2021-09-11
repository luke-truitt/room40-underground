import uuid
import datetime

from app.main import db
from app.main.model.document import Document

def save_new_document(data):
    try:
        new_document = Document(
            title=data['title'],
	    contents=data['contents'],
	    created_by=data['login_user_id'],
	    modified_by=data['login_user_id'],
	    created_time=data['action_time'],
	    modified_time=data['action_time'],
	    is_deleted=False,
	    is_active=True
        )
        save_changes(new_document)
        response_object = {
                'status': 'success',
                'message': 'Successfully registered.',
            }
        return response_object, 201

    except Exception as e:
        print(e)
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401

def update_document(document_id, data):
    try:
        document = get_a_document(document_id)
        document.title=data['title'],
        document.contents=data['contents'],
        document.modified_by=data['login_user_id'],
        document.modified_time=data['action_time'],
        document.is_active=data['is_active'],
        save_changes(document)
        response_object = {
                    'status': 'success',
                    'message': 'Successfully registered.',
                }
        return response_object, 201

    except Exception as e:
        print(e)
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def delete_a_document(document_id, data):
    try:
        del_documents=Document.query.filter_by(id=document_id).all()
        for document in del_documents:
            document.is_deleted=True
            document.modified_by=data['login_user_id'],
            document.modified_time=data['action_time'],
        db.session.commit()
        response_object = {
                    'status': 'success',
                    'message': 'Successfully registered.',
                }
        return response_object, 201

    except Exception as e:
        print(e)
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def get_all_documents():
    documents=Document.query.filter_by(is_deleted=False).filter_by(is_active=True)
    return documents.all()

def get_all_deleted_documents():
    documents=Document.query.filter_by(is_deleted=True)
    return documents.all()

def get_a_document(document_id):
    return Document.query.filter_by(id=document_id).filter_by(is_deleted=False).filter_by(is_active=True).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()
