from payex.pxagreement import (
        PxCreateAgreement3Handler, PxAutoPay3Handler, PxDeleteAgreementHandler,
        PxAgreementCheckHandler
        )
from payex.pxorder import (
        PxOrderInitialize7Handler, PxOrderCompleteHandler, PxOrderCapture5Handler,
        PxOrderGetTransactionDetails2Handler, PxCancel2Handler,
        )

class Payex(object):
    """
    Base Payex service, with handlers.
    """
    
    def __init__(self, merchant_number, encryption_key, production=False):
        
        # Set account credentials
        self.accountNumber = merchant_number
        self.encryption_key = encryption_key
        self.production = production
        
        # Add agreement handlers
        self.add_resource('create_agreement', PxCreateAgreement3Handler)
        self.add_resource('delete_agreement', PxDeleteAgreementHandler)
        self.add_resource('check_agreement', PxAgreementCheckHandler)
        self.add_resource('autopay', PxAutoPay3Handler)
        
        # Add order handlers
        self.add_resource('initialize', PxOrderInitialize7Handler)
        self.add_resource('complete', PxOrderCompleteHandler)
        self.add_resource('capture', PxOrderCapture5Handler)
        self.add_resource('cancel', PxCancel2Handler)
        self.add_resource('get_transaction_details', PxOrderGetTransactionDetails2Handler)
    
    def add_resource(self, name, handler):
        """
        Initializes the handler with this service instance.
        """
        
        setattr(self, name, handler(self))
