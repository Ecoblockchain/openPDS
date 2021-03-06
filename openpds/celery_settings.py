from celery.schedules import crontab

CELERY_ACKS_LATE = True
CELERYD_PREFETCH_MULTIPLIER = 1

CELERY_IMPORTS = ('openpds.questions.tasks',"openpds.questions.socialhealth_tasks", "openpds.questions.places_tasks", "openpds.meetup.tasks", "openpds.questions.probedatavisualization_tasks", "openpds.questions.mitfit_tasks", "openpds.questions.gfsa_tasks", "openpds.questions.auth_tasks", "openpds.questions.hotspots_tasks")
BROKER_URL = "mongodb://celery:celery@localhost:27017/lpd_celery_broker"
CELERYBEAT_SCHEDULE = {
#    "check-data-and-notify": {
#        "task": "openpds.questionstasks.checkDataAndNotify", 
#        "schedule": crontab(hour="*", minute="0")
#    },
    "compute-social-health-scores": {
        "task": "openpds.questions.socialhealth_tasks.recentSocialHealthScores",
        "schedule": crontab(hour="*", minute="0")
     },
    "ensure-funf-indexes": {
        "task": "openpds.questions.tasks.ensureFunfIndexes",
        "schedule": crontab(hour="*/2", minute="5")
    },
    "find-recent-places": {
        "task": "openpds.questions.places_tasks.findRecentPlaces", 
        "schedule": crontab(hour="*/2", minute="15")
    },
    "find-hourly-places": { 
        "task": "openpds.questions.places_tasks.findHourlyPlaces",  
        "schedule": crontab(hour="*/2", minute="20") 
    },
    "probe-summaries": {
        "task": "openpds.questions.probedatavisualization_tasks.recentProbeDataScores", 
        "schedule": crontab(hour="*", minute="25")
    },
    "high-active-locations": {
        "task": "openpds.questions.mitfit_tasks.findActiveLocationsTask",
        "schedule": crontab(hour="*", minute="30")
    },
    "high-active-times": {
        "task": "openpds.questions.mitfit_tasks.findActiveTimesTask",
        "schedule": crontab(hour="*", minute="35")
    },
    "leaderboard-computation": {
        "task": "openpds.questions.mitfit_tasks.leaderboardComputationTask",
        "schedule": crontab(hour="*", minute="40")
    },
    "wifi-auth-fingerprints": {
        "task": "openpds.questions.auth_tasks.computeAllFingerprints",
        "schedule": crontab(hour="*/2", minute="45")
    },
    "compute-gfsa": {
        "task": "openpds.questions.gfsa_tasks.recentGfsaScores",
        "schedule": crontab(hour="*", minute="55")
    },
    "hotspots-computation": {
        "task": "openpds.questions.hotspots_tasks.findHotSpotsTask",
        "schedule": crontab(hour="*", minute="30")
    },
}

