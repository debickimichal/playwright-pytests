from pages.example_page import ExamplePage

def test_example_page_basic_flow(page):
    example = ExamplePage(page)
    example.open()
    assert example.get_heading_text() == "Example Domain"
    assert example.is_main_paragraph_visible()

    example.click_more_information()
    assert "iana.org" in page.url
