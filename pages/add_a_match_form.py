from pages.base_page import BasePage

class Dashboard(BasePage):
    menu_scouts_panel_button_xpath = "//*[@aria-label='menu']"
    main_page_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[1]"
    players_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[2]"
    matches_button_xpath= "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]"
    reports_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[3]"
    language_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[3]/div[1]"
    sign_out_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[3]/div[2]"
    my_team_field_xpath = "//*[@name='myTeam']"
    enemy_field_xpath = "//*[@name='enemyTeam']"
    my_team_score_xpath = "//*[@name='myTeamScore']"
    enemy_team_score_xpath = "//*[@name='enemyTeamScore']"


pass