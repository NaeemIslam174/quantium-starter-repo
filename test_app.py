from app import app


def test_header_present(dash_duo):
    """The header should render when the app loads."""
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#header", timeout=10)
    assert dash_duo.find_element("#header").text == \
        "Soul Foods — Pink Morsel Sales Visualiser"


def test_visualisation_present(dash_duo):
    """The line chart should render when the app loads."""
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales-line-chart", timeout=10)
    assert dash_duo.find_element("#sales-line-chart") is not None


def test_region_picker_present(dash_duo):
    """The radio button region picker should render when the app loads."""
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-filter", timeout=10)
    assert dash_duo.find_element("#region-filter") is not None