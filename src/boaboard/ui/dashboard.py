from nicegui import APIRouter, ui

dashboard_router = APIRouter(prefix="/dashboard")


@dashboard_router.page("/")
def index_page() -> None:
    ui.markdown("# Dashboard")
