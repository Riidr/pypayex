from payex.pxagreement import (
        PxCreateAgreement3Handler, PxAutoPay2Handler, PxDeleteAgreementHandler,
        PxAgreementCheckHandler
        )
from payex.pxorder import (
    PxOrderInitialize8Handler, PxOrderCompleteHandler, PxOrderCapture5Handler,
    PxOrderGetTransactionDetails2Handler, PxCancel2Handler, PxOrderCheck2Handler,
    PxOrderAddSingleOrderLine2)

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
        self.add_resource('autopay', PxAutoPay2Handler)
        
        # Add order handlers
        self.add_resource('initialize', PxOrderInitialize8Handler)
        self.add_resource('complete', PxOrderCompleteHandler)
        self.add_resource('capture', PxOrderCapture5Handler)
        self.add_resource('cancel', PxCancel2Handler)
        self.add_resource('get_transaction_details', PxOrderGetTransactionDetails2Handler)
        self.add_resource('check', PxOrderCheck2Handler)
        self.add_resource('order_line', PxOrderAddSingleOrderLine2)

    def add_resource(self, name, handler):
        """
        Initializes the handler with this service instance.
        """
        
        setattr(self, name, handler(self))
