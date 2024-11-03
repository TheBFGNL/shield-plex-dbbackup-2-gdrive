format:
	black shield_plex_dbbackup_2_gdrive
	isort shield_plex_dbbackup_2_gdrive

lint-check:
	pylint shield_plex_dbbackup_2_gdrive

type-check:
	mypy shield_plex_dbbackup_2_gdrive

security-check:
	bandit -r shield_plex_dbbackup_2_gdrive

check-all: lint-check type-check security-check

fix-sh-scripts:
	sudo dos2unix *.sh
	sudo chmod +x *.sh
