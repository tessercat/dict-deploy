{
    'ADMINS': (
        ('Dictionary admin', '{{ admin_email }}'),
     ),
    'ALLOWED_HOST': '{{ dictionary_domain }}',
    'SERVER_EMAIL': 'noreply@{{ dictionary_domain }}',
    'TIME_ZONE': '{{ timezone }}',
}
