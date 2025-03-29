from typing import List

from django.utils import timezone

# from apps.project.models import (
#
# )
from apps.project.utils.util_reporte_d import custom_export_report_by_name


def format_float(value):
    if value is None:
        return "-"
    else:
        return f"{value:.2f}"
