# Initialisation du package views
# Permet d'importer directement depuis le package views

from .client_views import ClientViews
from .components import (
    render_job_card,
    render_candidate_card,
    render_success_message,
    render_error_message,
    render_info_message
)

__all__ = [
    'ClientViews',
    'AdminViews',
    'render_job_card',
    'render_candidate_card',
    'render_success_message',
    'render_error_message',
    'render_info_message'
]