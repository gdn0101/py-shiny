import pytest
from controls import OutputDataFrame
from playwright.sync_api import Page
from utils.deploy_utils import (
    create_deploys_app_url_fixture,
    reruns,
    reruns_delay,
    skip_if_not_chrome,
)

app_url = create_deploys_app_url_fixture("shiny-express-dataframe")


@skip_if_not_chrome
@pytest.mark.flaky(reruns=reruns, reruns_delay=reruns_delay)
def test_express_dataframe_deploys(page: Page, app_url: str) -> None:
    page.goto(app_url)

    dataframe = OutputDataFrame(page, "sample_data_frame")
    dataframe.expect_n_row(6)
