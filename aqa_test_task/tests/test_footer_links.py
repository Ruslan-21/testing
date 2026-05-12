from aqa_test_task.pages.inventory_page import InventoryPage


def test_footer_links(login):

    inventory = InventoryPage(login)

    twitter_page = inventory.open_twitter()

    assert "twitter" in twitter_page.url or "x.com" in twitter_page.url

    twitter_page.close()

    facebook_page = inventory.open_facebook()

    assert "facebook" in facebook_page.url

    facebook_page.close()

    linkedin_page = inventory.open_linkedin()

    assert "linkedin" in linkedin_page.url

    linkedin_page.close()