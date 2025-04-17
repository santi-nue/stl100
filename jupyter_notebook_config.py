# Jupyterlab icons can be created here to launch apps
# that are included in the user's image.
c.ServerProxy.servers = {
 #  'vscode': {
 #    'command': [
	# 	'code-server',
	# 	'--auth', 'none',
	# 	'--bind-addr', '0.0.0.0',
	# 	'--port', '5000'
	# ],
 #    'port': 5000,
 #    'absolute_url': False,
 #    'new_browser_tab': True,
 #    'timeout': 10,
 #    'launcher_entry': {
 #        'title': 'VSCode',
 #        },
 #  },
  'app': {
    'command': [
		'sh', 'start.sh'
	],
    'port': 8501,
    'absolute_url': False,
    'new_browser_tab': True,
    'timeout': 30,
    'launcher_entry': {
        'title': 'Streamlit',
        },
  },
}
