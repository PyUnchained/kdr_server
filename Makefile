test:
	export KDR_SETTINGS_MODULE=tests.settings && \
	coverage run --source=. --omit="*/tests/*" -m pytest ./tests && \
	coverage html