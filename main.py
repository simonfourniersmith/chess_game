from about import WesnothDialogAbout, WesnothTitleAbout, WesnothLabelAbout
from dialog import WesnothDialog, WesnothTitle
from gui_chess import Chess, pyglet
from rules import WesnothDialogRules
from scrollbox_rules import WesnothScrollBoxRules

_my_game = Chess()


def _add_last_move_to_scrollbox():
    _my_game.get_scrollbox().update_label_text(_my_game.get_history().format_move())


def _delete_last_move():
    _my_game.get_scrollbox().delete_label_last_line()
    _my_game.get_history().delete_move()


def _show_new_game_dialog():
    _dialog = WesnothDialog()
    _label = WesnothTitle()
    _dialog.add(_label)
    _my_game.get_gui().add(_dialog)
    _dialog.get_publisher().register(_dialog.EVENT_BLACK_BUTTON_CLICKED, "main", _set_player_turn_black)
    _dialog.get_publisher().register(_dialog.EVENT_WHITE_BUTTON_CLICKED, "main", _set_player_turn_white)
    _dialog.get_publisher().register(_dialog.EVENT_DIALOG_CLOSED, "main", _unblock_screen)

    _my_game.set_block_screen(True)


def _show_rules_dialog():
    _rules = WesnothDialogRules()
    _scrollbox_rules = WesnothScrollBoxRules()
    _rules.add(_scrollbox_rules)
    _my_game.get_gui().add(_rules)
    _rules.get_publisher().register(_rules.EVENT_CANCEL_BUTTON, "main", _unblock_screen)

    _my_game.set_block_screen(True)


def _show_about_dialog():
    _about = WesnothDialogAbout()
    _label_title = WesnothTitleAbout()
    _label_about = WesnothLabelAbout()
    _about.add(_label_title)
    _about.add(_label_about)
    _my_game.get_gui().add(_about)
    _about.get_publisher().register(_about.EVENT_CANCEL_BUTTON, "main", _unblock_screen)

    _my_game.set_block_screen(True)


def _set_player_turn_black():
    _my_game.reset(False)
    _my_game.set_block_screen(False)


def _set_player_turn_white():
    _my_game.reset()
    _my_game.set_block_screen(False)


def _unblock_screen():
    _my_game.set_block_screen(False)


_my_game.get_publisher().register(_my_game.EVENT_PIECE_MOVED, "main", _add_last_move_to_scrollbox)
_my_game.get_publisher().register(_my_game.EVENT_MOVE_UNDONE, "main", _delete_last_move)
_my_game.get_publisher().register(_my_game.EVENT_NEW_GAME, "main", _show_new_game_dialog)
_my_game.get_publisher().register(_my_game.EVENT_ABOUT_GAME, "main", _show_about_dialog)
_my_game.get_publisher().register(_my_game.EVENT_RULES_GAME, "main", _show_rules_dialog)
pyglet.clock.schedule_interval(_my_game.update, 1 / 60.)
pyglet.app.run()
