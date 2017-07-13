import random
from pprint import pprint

from custemoji import Emoji

TEST = "{} Test".format(Emoji.ANCHOR)
BACK_TO_MENU = "{} Back to Menu".format(Emoji.LEFTWARDS_BLACK_ARROW)
EXIT = "🔙 Exit"
REFRESH = "🔄 Refresh"
ADD_BOT = "➕ Add new bot"
EDIT_BOT = "🛠 Edit Bot"
SEND_BOTLIST = "☑ Update BotList"
BACK = "{} Back".format(Emoji.BACK_WITH_LEFTWARDS_ARROW_ABOVE)
BACK_TO_CATEGORY = "{} to Category".format(Emoji.BACK_WITH_LEFTWARDS_ARROW_ABOVE)
APPROVE_BOTS = "Approve Bots"
SEND_CONFIG_FILES = "Config files"
FIND_OFFLINE = "Find offline bots"
APPROVE_SUGGESTIONS = "Approve Suggestions"
SUGGESTION_PENDING_EMOJI = "👓"
CHANGE_SUGGESTION = "📝 Make Changes"
DONE = "🔚 Done"
SHARE = "Share"

# main menu
CATEGORIES = "📚 Explore ᴄᴀᴛᴇɢᴏʀɪᴇs"
NEW_BOTS = "🆕 New Bots"
SEARCH = "🔎 Search"
CONTRIBUTING = "📤 Contributing"
EXAMPLES = "📝 Examples"
HELP = "❔ Help"
ADMIN_MENU = "🛃 Admin Menu"
SWITCH_PRIVATE = "📖️ Continue in private"
FAVORITES = "💖 My Favorites"
ADD_FAVORITE = "➕ Add"
REMOVE_FAVORITE = "➖ Remove"
ADD_TO_FAVORITES = "Add to 💖 Favorites"
PIN = "📍 Pin"


def random_done_delete():
    CHOICES = ["I'm done", "Okay, done with this", "Okay, clear this mess", "I got what I wanted",
               "Don't need this anymore", "Keep this group spam-free"]
    return '🗑 {}'.format(random.choice(CHOICES))
