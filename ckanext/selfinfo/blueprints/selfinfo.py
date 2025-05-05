from flask import Blueprint
from ckanext.selfinfo.views.selfinfo import SelfinfoView, selfinfo_get_ram


selfinfo_bp = Blueprint("selfinfo", __name__, url_prefix="/ckan-admin/selfinfo")

# Ruta principal
selfinfo_bp.add_url_rule(
    "/", view_func=SelfinfoView.as_view("index")
)

# Ruta auxiliar
selfinfo_bp.add_url_rule("/get-ram", view_func=selfinfo_get_ram)
