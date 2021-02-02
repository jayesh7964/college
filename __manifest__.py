{

    'name': 'College System',
    'summary': 'A mosule that manages all the process of college',
    'version': '1.0',
    'author': 'Techultra Solution',
    'website': 'www.techultrasolutions.com',

    'depend':['base'],
    'data':[
        'security/college_security.xml',
        'security/ir.model.access.csv',

        'views/college_branch_views.xml',
        'views/college_student_views.xml',
        'views/college_staff_views.xml',
        'views/college_job_position_views.xml',
        'views/college_event_views.xml',
        'views/college_semester.xml',
        'views/college_event_registration_views.xml',
        'views/college_event_participant_views.xml',
        'views/college_event_category_views.xml',
     ],

    'application': True,
    'auto_install':False,
}