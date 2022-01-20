
{
    "name": "Twillio SMS Integeration",
    "version": "1.1",
    "summary": "send sms through Twillio(Repair Module) ",
  
    'license': 'OPL-1',
    "category": "sales",
    'author': 'Hunain Ak',
    "installable": True,
    "depends": ['repair'],
    "data": [
       
       'security/ir.model.access.csv',
       'security/security.xml',
        'views/sms_sending.xml',
        
    
    ],
}
