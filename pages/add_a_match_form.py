from pages.base_page import BasePage

class Dashboard(BasePage):
    menu_scouts_panel_button_xpath = "//*[@aria-label='menu']"
    main_page_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[1]"
    players_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[2]"
    language_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]"
    sign_out_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]"
    download_csv_button.xpath = "//*[contains(@aria-label, 'CSV')]"
    print_button.xpath = "//*[contains( @ aria - label,'Print')]"
    view_columns_button-xpath = "//*[contains(@data-testid, 'olumn')]"
    filter_table_button_xpath = "//*[contains(@data-testid, 'Filt')]"
    netx_page_button_xpath= "//*[@id='pagination-next']"

pass