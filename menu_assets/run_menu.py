from menu_assets.logics import Logics

g = Logics()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()
