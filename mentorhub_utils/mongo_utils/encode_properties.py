from datetime import datetime
from bson import ObjectId


def encode_document(document, id_properties, date_properties):
    """Encode ObjectId and datetime values for MongoDB"""
    
    def encode_value(key, value):
        """Encode identified values"""
        if key in id_properties:
            if isinstance(value, str):
                return ObjectId(value)
            if isinstance(value, list):
                return [ObjectId(item) if isinstance(item, str) else item for item in value]
        if key in date_properties:
            if isinstance(value, str):
                
                return datetime.fromisoformat(value)
            if isinstance(value, list):
                return [datetime.fromisoformat(item) if isinstance(item, str) else item for item in value]
        return value

    # Traverse the document and encode relevant properties
    for key, value in document.items():
        if isinstance(value, dict):
            encode_document(value, id_properties, date_properties)  
        elif isinstance(value, list):
            if all(isinstance(item, dict) for item in value):
                document[key] = [encode_document(item, id_properties, date_properties) for item in value]
            else:
                document[key] = [encode_value(key, item) for item in value]
        else:
            document[key] = encode_value(key, value)  

    return document