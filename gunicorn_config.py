bind = "unix:/home/ec2-user/copal/gunicorn.sock"
workers = 3
umask = 0o007  # Définit les permissions du socket pour le groupe (lecture/écriture)